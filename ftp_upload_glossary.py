#!/usr/bin/env python3
"""Upload new glossary icons to FTP."""

import ftplib
import os
from pathlib import Path

FTP_HOST = '5.183.10.156'
FTP_USER = 'u993527396'
FTP_PASS = 'Victoria2026!'
ICONS_DIR = Path('/Users/colin/seo/agentiscript/icons')
REMOTE_DIR = '/agentiscript/icons'

# Read list of generated icons
with open('/tmp/generated_icons.txt') as f:
    generated = [line.strip() for line in f if line.strip()]

print(f"Icons to upload: {len(generated)} × 2 files = {len(generated)*2} files")

uploaded = 0
failed = 0

try:
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    print(f"Connected to FTP: {FTP_HOST}")
    print(f"Welcome: {ftp.getwelcome()[:80]}")

    # Ensure remote directory exists
    try:
        ftp.cwd(REMOTE_DIR)
    except ftplib.error_perm:
        # Try to create it
        try:
            ftp.mkd('/agentiscript')
        except:
            pass
        try:
            ftp.mkd(REMOTE_DIR)
        except:
            pass
        ftp.cwd(REMOTE_DIR)

    print(f"Remote dir: {ftp.pwd()}")

    for slug in generated:
        for ext in ['svg', 'json']:
            local_path = ICONS_DIR / f'{slug}.{ext}'
            if not local_path.exists():
                continue
            remote_name = f'{slug}.{ext}'
            try:
                with open(local_path, 'rb') as f:
                    ftp.storbinary(f'STOR {remote_name}', f)
                uploaded += 1
            except Exception as e:
                print(f"  FAIL: {remote_name}: {e}")
                failed += 1

        if (uploaded + failed) % 100 == 0 and uploaded > 0:
            print(f"  Progress: {uploaded} uploaded, {failed} failed...")

    ftp.quit()
    print(f"\n✅ FTP upload complete: {uploaded} files uploaded, {failed} failed")

except Exception as e:
    print(f"❌ FTP error: {e}")
    raise
