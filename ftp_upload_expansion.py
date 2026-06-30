#!/usr/bin/env python3
"""Upload new expansion icons + rebuilt agentiscript.json to FTP."""

import ftplib
import os
from pathlib import Path

FTP_HOST = "5.183.10.156"
FTP_USER = "u993527396"
FTP_PASS = "Victoria2026!"
BASE_DIR = Path("/Users/colin/seo/agentiscript")
ICONS_DIR = BASE_DIR / "icons"

NEW_SLUGS = [
    "zero-knowledge-ml",
    "verifiable-inference",
    "attention-economy",
    "creator-economy",
    "gig-economy",
    "platform-economy",
    "service-mesh",
    "api-gateway",
    "circuit-breaker",
    "bulkhead-pattern",
    "saga-pattern",
    "event-sourcing",
    "cqrs",
    "distributed-tracing",
    "observability-platform",
    "chaos-engineering",
    "blue-green-deployment",
    "canary-deployment",
    "feature-flag",
]

def upload_file(ftp, local_path, remote_path):
    remote_dir = "/".join(remote_path.split("/")[:-1])
    try:
        ftp.mkd(remote_dir)
    except ftplib.error_perm:
        pass
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_path}", f)

print(f"Connecting to {FTP_HOST}...")
ftp = ftplib.FTP(FTP_HOST)
ftp.login(FTP_USER, FTP_PASS)
print(f"Connected. Current dir: {ftp.pwd()}")

# Find remote icons dir
try:
    ftp.cwd("public_html/icons")
    ftp.cwd("..")
    remote_base = "public_html"
except:
    try:
        ftp.cwd("icons")
        ftp.cwd("..")
        remote_base = ""
    except:
        remote_base = "public_html"

ftp.cwd("/")
print(f"Remote base: /{remote_base}")

uploaded = 0
errors = []

# Upload new icon files
for slug in NEW_SLUGS:
    for ext in ["json", "svg"]:
        local_path = ICONS_DIR / f"{slug}.{ext}"
        if not local_path.exists():
            print(f"  WARNING: {local_path} not found")
            continue
        remote_path = f"/{remote_base}/icons/{slug}.{ext}".replace("//", "/")
        try:
            with open(local_path, "rb") as f:
                ftp.storbinary(f"STOR {remote_path}", f)
            uploaded += 1
            print(f"  ✓ {slug}.{ext}")
        except Exception as e:
            errors.append(f"{slug}.{ext}: {e}")
            print(f"  ✗ {slug}.{ext}: {e}")

# Upload rebuilt agentiscript.json
local_json = BASE_DIR / "agentiscript.json"
remote_json = f"/{remote_base}/agentiscript.json".replace("//", "/")
try:
    with open(local_json, "rb") as f:
        ftp.storbinary(f"STOR {remote_json}", f)
    uploaded += 1
    print(f"  ✓ agentiscript.json")
except Exception as e:
    errors.append(f"agentiscript.json: {e}")
    print(f"  ✗ agentiscript.json: {e}")

ftp.quit()

print(f"\nUploaded: {uploaded} files")
if errors:
    print(f"Errors ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
else:
    print("No errors!")
