#!/usr/bin/env python3
"""Upload AgentiScript v1.2 new files to FTP."""

import ftplib, os, sys

HOST = "5.183.10.156"
USER = "u993527396"
PASS = "Victoria2026!"
REMOTE_BASE = "/domains/agentiscript.com/public_html"
LOCAL_BASE = "/Users/colin/seo/agentiscript"

# New files to upload
NEW_SLUGS = [
    "machine-readability","agent-identity","programmable-financial-system",
    "ai-native-data-stack","multi-agent-orchestration","outcome-based-metrics",
    "voice-agent","onchain-rwa-origination","stablecoin-onramp",
    "factory-style-ai-deployment","physical-observability","prompt-free-ai",
    "ai-prediction-market","vertical-ai","agent-scale-infrastructure",
    "zero-trust","digital-identity","cyber-resilience","supply-chain-risk",
    "cryptographic-agility","sovereign-data","federated-identity",
    "critical-infrastructure","privacy-enhancing-technology","algorithmic-accountability",
]

def ensure_dir(ftp, path):
    parts = path.strip("/").split("/")
    cur = ""
    for p in parts:
        cur = cur + "/" + p
        try:
            ftp.mkd(cur)
        except ftplib.error_perm:
            pass  # already exists

def upload_file(ftp, local_path, remote_path):
    remote_dir = "/".join(remote_path.split("/")[:-1])
    ensure_dir(ftp, remote_dir)
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_path}", f)

print(f"Connecting to {HOST}…")
ftp = ftplib.FTP(HOST, USER, PASS, timeout=30)
ftp.set_pasv(True)
print(f"  Connected: {ftp.getwelcome()[:60]}")

uploaded = []
errors = []

# Upload new icon SVG + JSON pairs
for slug in NEW_SLUGS:
    for ext in ("svg", "json"):
        local = os.path.join(LOCAL_BASE, "icons", f"{slug}.{ext}")
        remote = f"{REMOTE_BASE}/icons/{slug}.{ext}"
        try:
            upload_file(ftp, local, remote)
            uploaded.append(f"icons/{slug}.{ext}")
            print(f"  ✓ icons/{slug}.{ext}")
        except Exception as e:
            errors.append((f"icons/{slug}.{ext}", str(e)))
            print(f"  ✗ icons/{slug}.{ext}  — {e}", file=sys.stderr)

# Upload updated master index
for fname in ("agentiscript.json", "index.html"):
    local = os.path.join(LOCAL_BASE, fname)
    if not os.path.exists(local):
        continue
    remote = f"{REMOTE_BASE}/{fname}"
    try:
        upload_file(ftp, local, remote)
        uploaded.append(fname)
        print(f"  ✓ {fname}")
    except Exception as e:
        errors.append((fname, str(e)))
        print(f"  ✗ {fname}  — {e}", file=sys.stderr)

ftp.quit()

print(f"\n✅ Uploaded {len(uploaded)} files")
if errors:
    print(f"⚠️  {len(errors)} errors:")
    for f, e in errors:
        print(f"   {f}: {e}")
