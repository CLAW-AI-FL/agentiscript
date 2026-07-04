#!/usr/bin/env python3
"""
AgentiScript — America the Beautiful Mint Script
Mints exactly 500 NFTs from the founding-500-manifest.json
Uses xrpl-py 4.x sign_and_submit pattern

Usage:
    XRPL_SEED="sa9sUBYnP1oR1kEPKdXPwvcodXrhg" python3 mint_america.py
"""

import os, sys, json, time, logging
from pathlib import Path

from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.constants import CryptoAlgorithm
from xrpl.models.transactions import NFTokenMint
from xrpl.transaction import sign_and_submit
from xrpl.utils import str_to_hex

# ── Config ──────────────────────────────────────────────────────────────────
MANIFEST      = Path("/Users/colin/seo/agentiscript/mint/founding-500-manifest.json")
PROGRESS_FILE = Path("/Users/colin/seo/agentiscript/mint/mint_america_progress.json")
LOG_FILE      = Path("/Users/colin/seo/agentiscript/mint/mint_america.log")
MAINNET_URL   = "https://xrplcluster.com"
BASE_URI      = "https://agentiscript.com/icons/{slug}.png"
NFT_FLAGS     = 8        # tfTransferable
TRANSFER_FEE  = 10000   # 10% royalty
TAXON         = 1        # America the Beautiful collection

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
log = logging.getLogger(__name__)

def load_progress():
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text())
        except:
            pass
    return {'minted': {}, 'failed': []}

def save_progress(p):
    PROGRESS_FILE.write_text(json.dumps(p, indent=2))

def main():
    seed = os.environ.get('XRPL_SEED') or os.environ.get('SEED')
    if not seed:
        log.error("XRPL_SEED required")
        sys.exit(1)

    wallet = Wallet.from_seed(seed, algorithm=CryptoAlgorithm.SECP256K1)
    log.info(f"Wallet: {wallet.classic_address}")

    if wallet.classic_address != 'rfFbKaT7pQTUsAYyEH8r5a6XTD45rz3aFe':
        log.error(f"WRONG WALLET — STOPPING")
        sys.exit(1)

    client = JsonRpcClient(MAINNET_URL)
    log.info(f"Connected: {MAINNET_URL}")

    # Load manifest
    manifest = json.loads(MANIFEST.read_text())
    all_slugs = [i['slug'] for i in manifest['items']]
    log.info(f"Total NFTs: {len(all_slugs)}")

    # Load progress — resume from where we left off
    progress = load_progress()
    already_minted = set(progress['minted'].keys())
    log.info(f"Already minted: {len(already_minted)}")

    remaining = [s for s in all_slugs if s not in already_minted]
    log.info(f"Remaining: {len(remaining)}")

    if not remaining:
        log.info("ALL 500 MINTED!")
        return

    total_minted = len(already_minted)
    total_failed = 0

    for slug in remaining:
        uri = BASE_URI.format(slug=slug)

        tx = NFTokenMint(
            account=wallet.classic_address,
            uri=str_to_hex(uri),
            flags=NFT_FLAGS,
            transfer_fee=TRANSFER_FEE,
            nftoken_taxon=TAXON,
        )

        try:
            resp = sign_and_submit(tx, client, wallet, autofill=True)
            engine_result = resp.result.get('engine_result', '')

            if engine_result in ('tesSUCCESS', 'terQUEUED'):
                total_minted += 1
                tx_hash = resp.result.get('hash', '')
                progress['minted'][slug] = {'tx_hash': tx_hash, 'uri': uri}
                log.info(f"✓ [{total_minted}/500] {slug} — {engine_result}")
            else:
                total_failed += 1
                progress['failed'].append(slug)
                log.error(f"✗ {slug} — {engine_result}")

        except Exception as e:
            log.error(f"✗ {slug} exception: {e}")
            progress['failed'].append(slug)
            total_failed += 1

        # Save every 10 mints
        if total_minted % 10 == 0:
            save_progress(progress)

        # Pace — 1 tx per ~1s to avoid rate limiting
        time.sleep(1)

    save_progress(progress)
    log.info(f"\n{'='*50}")
    log.info(f"COMPLETE: {total_minted} minted | {total_failed} failed")
    log.info(f"Progress: {PROGRESS_FILE}")

if __name__ == '__main__':
    main()
