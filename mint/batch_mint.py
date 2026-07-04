#!/usr/bin/env python3
"""
AgentiScript XRPL Batch Pipeline Minter
Submits 20 concurrent NFTokenMint transactions per ledger.
~53 minutes to mint all 15,868 remaining icons.

Usage:
    XRPL_SEED=sYourSeedHere python3 batch_mint.py

Resumes automatically from /tmp/mint_progress.json
"""

import os, sys, json, time, glob, asyncio, logging
from pathlib import Path
from datetime import datetime

import xrpl
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.transactions import NFTokenMint
from xrpl.models.requests import AccountInfo, AccountNFTs
from xrpl.transaction import sign
from xrpl.core.keypairs import derive_classic_address
from xrpl.constants import CryptoAlgorithm
from xrpl.utils import str_to_hex

# ── Config ────────────────────────────────────────────────────────────────────
ICONS_DIR     = Path("/Users/colin/seo/agentiscript/icons")
PROGRESS_FILE = Path("/tmp/mint_progress.json")
LOG_FILE      = Path("/tmp/batch_mint.log")
MAINNET_URL   = "https://xrplcluster.com"
BASE_URI      = "https://agentiscript.com/icons/{slug}.svg"
NFT_FLAGS     = 8        # tfTransferable
TRANSFER_FEE  = 10000   # 10%
TAXON         = 1
BATCH_SIZE    = 20       # concurrent tx per ledger
SAVE_EVERY    = 20       # save progress every N mints

# ── Logging ───────────────────────────────────────────────────────────────────
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
            d = json.loads(PROGRESS_FILE.read_text())
            if 'minted' not in d:
                d['minted'] = {}
            if 'failed' not in d:
                d['failed'] = {}
            return d
        except:
            pass
    return {'minted': {}, 'failed': {}, 'started_at': datetime.utcnow().isoformat()}

def save_progress(p):
    p['updated_at'] = datetime.utcnow().isoformat()
    PROGRESS_FILE.write_text(json.dumps(p, indent=2))

def get_icons():
    """Get all icon slugs from icons directory."""
    slugs = []
    for f in sorted(ICONS_DIR.glob("*.svg")):
        slugs.append(f.stem)
    if not slugs:
        # fallback: read from agentiscript.json
        catalog = json.loads(Path("/Users/colin/seo/agentiscript/agentiscript.json").read_text())
        slugs = [i.get('slug') or i.get('name','') for i in catalog.get('icons', [])[:20521]]
    return slugs

def get_account_info(client, address):
    req = AccountInfo(account=address, ledger_index="current")
    resp = client.request(req)
    return resp.result['account_data']

def submit_tx(client, tx, wallet):
    """Sign and submit without waiting for validation."""
    signed = sign(tx, wallet)
    # xrpl-py 4.x: signed is a Transaction object, get tx_blob via encode
    if hasattr(signed, 'tx_blob'):
        tx_blob = signed.tx_blob
    else:
        from xrpl.core.binarycodec import encode
        tx_blob = encode(signed.to_dict())
    response = client.request(xrpl.models.requests.SubmitOnly(tx_blob=tx_blob))
    return response.result

def main():
    seed = os.environ.get('XRPL_SEED') or os.environ.get('SEED')
    if not seed:
        log.error("XRPL_SEED environment variable required")
        sys.exit(1)

    wallet = Wallet.from_seed(seed, algorithm=CryptoAlgorithm.SECP256K1)
    log.info(f"Wallet: {wallet.classic_address}")

    client = JsonRpcClient(MAINNET_URL)
    log.info(f"Connected to: {MAINNET_URL}")

    # Load progress
    progress = load_progress()
    already_minted = set(progress['minted'].keys())
    log.info(f"Already minted: {len(already_minted)}")

    # Get all icons
    all_slugs = get_icons()
    log.info(f"Total icons: {len(all_slugs)}")

    # Filter remaining
    remaining = [s for s in all_slugs if s not in already_minted]
    log.info(f"Remaining to mint: {len(remaining)}")

    if not remaining:
        log.info("ALL DONE! Nothing left to mint.")
        return

    # Get current sequence
    acct = get_account_info(client, wallet.classic_address)
    sequence = acct['Sequence']
    balance_xrp = int(acct['Balance']) / 1_000_000
    log.info(f"Balance: {balance_xrp:.4f} XRP | Starting sequence: {sequence}")

    total_minted = 0
    total_failed = 0
    start_time = time.time()

    # Process in batches of BATCH_SIZE
    for batch_start in range(0, len(remaining), BATCH_SIZE):
        batch = remaining[batch_start:batch_start + BATCH_SIZE]
        batch_num = batch_start // BATCH_SIZE + 1
        total_batches = (len(remaining) + BATCH_SIZE - 1) // BATCH_SIZE

        log.info(f"Batch {batch_num}/{total_batches} | Slugs: {batch[0]}...{batch[-1]}")

        # Submit all in batch with sequential sequence numbers
        submitted = []
        for i, slug in enumerate(batch):
            uri = BASE_URI.format(slug=slug)
            uri_hex = str_to_hex(uri)

            tx = NFTokenMint(
                account=wallet.classic_address,
                uri=uri_hex,
                flags=NFT_FLAGS,
                transfer_fee=TRANSFER_FEE,
                nftoken_taxon=TAXON,
                sequence=sequence + i,
                fee="12",
                last_ledger_sequence=None,
            )

            try:
                result = submit_tx(client, tx, wallet)
                engine_result = result.get('engine_result', '')
                tx_hash = result.get('tx_json', {}).get('hash', '')

                if engine_result in ('tesSUCCESS', 'terQUEUED'):
                    submitted.append({
                        'slug': slug,
                        'seq': sequence + i,
                        'txid': tx_hash,
                        'result': engine_result
                    })
                else:
                    log.warning(f"  ✗ {slug}: {engine_result}")
                    progress['failed'][slug] = {'result': engine_result, 'seq': sequence + i}
                    total_failed += 1
            except Exception as e:
                log.error(f"  ✗ {slug} exception: {e}")
                progress['failed'][slug] = {'error': str(e)}
                total_failed += 1

        # Wait one ledger for confirmations (~4 seconds)
        time.sleep(4)

        # Record minted
        for s in submitted:
            progress['minted'][s['slug']] = {
                'slug': s['slug'],
                'txid': s['txid'],
                'seq': s['seq'],
                'timestamp': datetime.utcnow().isoformat()
            }
            total_minted += 1
            log.info(f"  ✓ [{len(already_minted) + total_minted}/{len(all_slugs)}] {s['slug']} | tx: {s['txid'][:16]}...")

        # Advance sequence
        sequence += len(batch)

        # Save progress
        save_progress(progress)

        # ETA
        elapsed = time.time() - start_time
        done = batch_start + len(batch)
        rate = done / elapsed if elapsed > 0 else 1
        eta_sec = (len(remaining) - done) / rate if rate > 0 else 0
        log.info(f"  Progress: {done}/{len(remaining)} | Rate: {rate:.1f}/sec | ETA: {eta_sec/60:.1f} min")

    # Final summary
    elapsed = time.time() - start_time
    log.info(f"\n{'='*60}")
    log.info(f"BATCH MINT COMPLETE")
    log.info(f"Minted this run: {total_minted}")
    log.info(f"Failed: {total_failed}")
    log.info(f"Total minted ever: {len(progress['minted'])}")
    log.info(f"Time: {elapsed/60:.1f} minutes")
    log.info(f"{'='*60}")
    save_progress(progress)

if __name__ == '__main__':
    main()
