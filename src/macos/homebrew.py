#!/usr/bin/env python3

import subprocess
import sys
import shutil

def check_homebrew():
    if shutil.which("brew") is not None:
        print("✅ Homebrew is already installed.")
        return

    print("🔧 Homebrew not found. Installing...")

    install_command = [
        "/bin/bash", "-c",
        "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ]

    try:
        subprocess.run(" ".join(install_command), shell=True, check=True)
        print("✅ Homebrew installed successfully.")
    except subprocess.CalledProcessError:
        print("❌ Failed to install Homebrew.")
        sys.exit(1)