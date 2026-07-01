#!/usr/bin/env python3
"""
AgentiScript XRPL NFT Minter
Mints NFTokens for all 20,520 AgentiScript icons on XRPL.

Usage:
    # Testnet (generates a funded faucet wallet automatically):
    python3 mint_nfts.py --testnet --test-run

    # Mainnet (requires XRPL_SEED env var):
    XRPL_SEED="sYourSeedHere" python3 mint_nfts.py --mainnet

    # Resume interrupted run:
    python3 mint_nfts.py --testnet --test-run  (resumes automatically)
"""

import os
import sys
import json
import time
import glob
import argparse
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, List

import xrpl
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet, generate_faucet_wallet
from xrpl.models.transactions import NFTokenMint
from xrpl.models.requests import AccountNFTs
from xrpl.transaction import submit_and_wait
from xrpl.utils import str_to_hex

# ─── Config ──────────────────────────────────────────────────────────────────
ICONS_DIR      = Path("/Users/colin/seo/agentiscript/icons")
PROGRESS_FILE  = Path("/tmp/mint_progress.json")
RESULTS_FILE   = Path("/tmp/mint_test_results.json")
LOG_FILE       = Path("/tmp/mint_nfts.log")

TESTNET_URL    = "https://s.altnet.rippletest.net:51234"
MAINNET_URL    = "https://xrplcluster.com"

BASE_URI       = "https://agentiscript.com/icons/{slug}.svg"
NFT_FLAGS      = 8          # tfTransferable
TRANSFER_FEE   = 10000      # 10% = 10000 basis points (1 basis point = 0.001%)
TAXON          = 1          # AgentiScript collection

BATCH_SIZE     = 50         # icons per save checkpoint
RETRY_LIMIT    = 3          # retries per failed mint
RETRY_DELAY    = 5          # seconds between retries

# ─── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE),
    ]
)
log = logging.getLogger("mint_nfts")


# ─── Helpers ─────────────────────────────────────────────────────────────────

def slug_to_uri_hex(slug: str) -> str:
    """Convert an icon slug to a hex-encoded URI."""
    uri = BASE_URI.format(slug=slug)
    return str_to_hex(uri)


def load_progress() -> dict:
    """Load mint progress from disk."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"minted": {}, "failed": {}, "started_at": datetime.utcnow().isoformat()}


def save_progress(progress: dict):
    """Persist mint progress to disk."""
    progress["updated_at"] = datetime.utcnow().isoformat()
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)
    log.debug(f"Progress saved: {len(progress['minted'])} minted, {len(progress['failed'])} failed")


def load_icon_slugs() -> List[str]:
    """Discover all icon slugs from the icons directory."""
    log.info(f"Scanning icons in {ICONS_DIR} …")
    json_files = sorted(ICONS_DIR.glob("*.json"))
    slugs = []
    for jf in json_files:
        try:
            with open(jf) as f:
                data = json.load(f)
            slug = data.get("slug") or jf.stem
            slugs.append(slug)
        except Exception as e:
            log.warning(f"  Skipping {jf.name}: {e}")
    log.info(f"  Found {len(slugs)} icon slugs")
    return slugs


def get_wallet(client: JsonRpcClient, testnet: bool, seed: Optional[str]) -> Wallet:
    """Return a funded wallet (faucet on testnet, seed on mainnet)."""
    if testnet:
        # If a seed was supplied, use it directly (skip faucet)
        if seed:
            wallet = Wallet.from_seed(seed)
            log.info(f"Testnet wallet (from seed): {wallet.classic_address}")
            return wallet

        # Try faucet with retries
        log.info("Generating testnet faucet wallet …")
        for attempt in range(1, 6):
            try:
                wallet = generate_faucet_wallet(client, debug=True)
                log.info(f"  Testnet wallet: {wallet.classic_address}")
                log.info(f"  Seed:           {wallet.seed}")
                return wallet
            except Exception as e:
                log.warning(f"  Faucet attempt {attempt}/5 failed: {e}")
                if attempt < 5:
                    wait = attempt * 15
                    log.info(f"  Waiting {wait}s before retry …")
                    time.sleep(wait)
        log.error("Faucet unavailable. Use --seed with a pre-funded testnet wallet seed.")
        sys.exit(1)
    else:
        if not seed:
            seed = os.environ.get("XRPL_SEED")
        if not seed:
            log.error("Mainnet requires XRPL_SEED environment variable or --seed flag")
            sys.exit(1)
        wallet = Wallet.from_seed(seed)
        log.info(f"Mainnet wallet: {wallet.classic_address}")
        return wallet


def mint_one(client: JsonRpcClient, wallet: Wallet, slug: str) -> dict:
    """
    Mint a single NFToken for an icon slug.
    Returns a result dict with keys: slug, nftoken_id, txid, fee, timestamp.
    Raises on failure.
    """
    uri_hex = slug_to_uri_hex(slug)

    tx = NFTokenMint(
        account=wallet.classic_address,
        uri=uri_hex,
        flags=NFT_FLAGS,
        transfer_fee=TRANSFER_FEE,
        nftoken_taxon=TAXON,
    )

    response = submit_and_wait(tx, client, wallet)
    result = response.result

    tx_result = result.get("meta", {}).get("TransactionResult", "UNKNOWN")
    if tx_result != "tesSUCCESS":
        raise RuntimeError(f"TX failed: {tx_result}")

    # Extract NFToken ID from metadata
    nftoken_id = None
    for node in result.get("meta", {}).get("AffectedNodes", []):
        created = node.get("CreatedNode", {})
        if created.get("LedgerEntryType") == "NFTokenPage":
            nfts = created.get("NewFields", {}).get("NFTokens", [])
            if nfts:
                nftoken_id = nfts[-1].get("NFToken", {}).get("NFTokenID")
                break
        modified = node.get("ModifiedNode", {})
        if modified.get("LedgerEntryType") == "NFTokenPage":
            final = modified.get("FinalFields", {}).get("NFTokens", [])
            prev  = modified.get("PreviousFields", {}).get("NFTokens", [])
            if final and len(final) > len(prev or []):
                nftoken_id = final[-1].get("NFToken", {}).get("NFTokenID")
                break

    fee_drops = int(result.get("Fee", "12"))

    return {
        "slug":       slug,
        "nftoken_id": nftoken_id,
        "txid":       result.get("hash"),
        "fee_drops":  fee_drops,
        "fee_xrp":    fee_drops / 1_000_000,
        "timestamp":  datetime.utcnow().isoformat(),
        "ledger":     result.get("ledger_index"),
    }


def mint_batch(
    client:   JsonRpcClient,
    wallet:   Wallet,
    slugs:    List[str],
    progress: dict,
    max_mints: Optional[int] = None,
) -> dict:
    """
    Iterate through slugs, skip already-minted, mint the rest in batches.
    Saves progress after every BATCH_SIZE mints.
    """
    already_minted = set(progress["minted"].keys())
    pending = [s for s in slugs if s not in already_minted]

    if max_mints is not None:
        pending = pending[:max_mints]

    total      = len(pending)
    batch_count = 0
    success     = 0
    failed      = 0

    log.info(f"Starting mint: {total} pending icons (already minted: {len(already_minted)})")

    for i, slug in enumerate(pending, 1):
        log.info(f"[{i}/{total}] Minting: {slug}")

        minted = False
        last_error = None
        for attempt in range(1, RETRY_LIMIT + 1):
            try:
                result = mint_one(client, wallet, slug)
                progress["minted"][slug] = result
                log.info(
                    f"  ✓ NFTokenID={result['nftoken_id']}  "
                    f"txid={result['txid']}  fee={result['fee_xrp']:.6f} XRP"
                )
                success  += 1
                minted    = True
                break
            except Exception as e:
                last_error = str(e)
                log.warning(f"  Attempt {attempt}/{RETRY_LIMIT} failed: {e}")
                if attempt < RETRY_LIMIT:
                    time.sleep(RETRY_DELAY)

        if not minted:
            log.error(f"  ✗ FAILED after {RETRY_LIMIT} attempts: {last_error}")
            progress["failed"][slug] = {
                "slug":  slug,
                "error": last_error,
                "timestamp": datetime.utcnow().isoformat(),
            }
            failed += 1

        batch_count += 1
        if batch_count >= BATCH_SIZE:
            save_progress(progress)
            batch_count = 0
            log.info(f"  ── checkpoint: {success} minted, {failed} failed ──")

    # Final save
    save_progress(progress)
    log.info(f"\nDone. Minted: {success}, Failed: {failed}")
    return progress


# ─── CLI ─────────────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="AgentiScript XRPL NFT Minter")
    net = p.add_mutually_exclusive_group(required=True)
    net.add_argument("--testnet",  action="store_true", help="Use XRPL testnet (auto-funded faucet wallet)")
    net.add_argument("--mainnet",  action="store_true", help="Use XRPL mainnet (requires XRPL_SEED)")
    p.add_argument("--seed",      type=str, default=None, help="Wallet seed (overrides XRPL_SEED env var)")
    p.add_argument("--test-run",  action="store_true", help="Mint only 3 icons (smoke test)")
    p.add_argument("--reset",     action="store_true", help="Clear progress and start fresh")
    p.add_argument("--dry-run",   action="store_true", help="List icons only, don't mint")
    return p.parse_args()


def main():
    args = parse_args()

    # Client
    url = TESTNET_URL if args.testnet else MAINNET_URL
    log.info(f"Connecting to: {url}")
    client = JsonRpcClient(url)

    # Progress
    if args.reset and PROGRESS_FILE.exists():
        PROGRESS_FILE.unlink()
        log.info("Progress reset.")
    progress = load_progress()

    # Icons
    slugs = load_icon_slugs()

    if args.dry_run:
        log.info("DRY RUN — not minting. First 5 slugs:")
        for s in slugs[:5]:
            log.info(f"  {s}  →  {BASE_URI.format(slug=s)}")
        return

    # Wallet
    wallet = get_wallet(client, args.testnet, args.seed)

    # Mint
    max_mints = 3 if args.test_run else None
    progress  = mint_batch(client, wallet, slugs, progress, max_mints=max_mints)

    # Test-run: save results separately
    if args.test_run:
        test_results = {
            "network":    "testnet" if args.testnet else "mainnet",
            "wallet":     wallet.classic_address,
            "seed":       wallet.seed if args.testnet else "REDACTED",
            "minted":     list(progress["minted"].values()),
            "failed":     list(progress["failed"].values()),
            "verify_url": "https://testnet.xrpl.org/accounts/" + wallet.classic_address,
            "timestamp":  datetime.utcnow().isoformat(),
        }
        with open(RESULTS_FILE, "w") as f:
            json.dump(test_results, f, indent=2)
        log.info(f"\nTest results saved to {RESULTS_FILE}")
        log.info(f"Verify at: {test_results['verify_url']}")

    # Estimate full run time
    minted_list = list(progress["minted"].values())
    if len(minted_list) >= 2:
        # Rough timing estimate
        t0 = datetime.fromisoformat(minted_list[0]["timestamp"])
        t1 = datetime.fromisoformat(minted_list[-1]["timestamp"])
        elapsed = (t1 - t0).total_seconds()
        n = len(minted_list) - 1
        if n > 0:
            rate = elapsed / n  # seconds per mint
            total_secs = rate * 20520
            hours = total_secs / 3600
            log.info(f"\n📊 Timing estimate for 20,520 mints:")
            log.info(f"   Rate: ~{rate:.1f}s per mint")
            log.info(f"   Est. time: {hours:.1f} hours")


if __name__ == "__main__":
    main()
