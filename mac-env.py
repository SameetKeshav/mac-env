#!/usr/bin/env python3

import subprocess
import sys
import shutil
import os
import platform

from macos.homebrew import check_homebrew

def check_os():
    os_name = platform.system()

    if os_name == "Windows":
        windows()
    elif os_name == "Darwin":
        mac_os()
    elif os_name == "Linux":
        linux()
    else:
        raise Exception("Unknown OS: {os_name}")

def mac_os():
    raise Exception("Macos")

def windows():
    raise Exception("Windows Version of this tool has not been created yet")

def linux():
    raise Exception("Linux Version of this tool has not been created yet")

def main():
    check_homebrew()

if __name__ == "__main__":
    main()
