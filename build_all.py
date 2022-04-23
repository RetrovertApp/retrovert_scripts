from asyncio import subprocess
import os
import platform
import sys

def build_tundra(entry):
    p0 = os.path.join(entry.name, "tundra.lua")
    p1 = os.path.join(entry.name, "units.lua")
    if os.path.exists(p0) and os.path.exists(p1):
        os.chdir(entry.name)
        v = os.system("tundra2 linux-gcc-debug")
        if v != 0:
            sys.exit(v)
        os.chdir("..")

def build_cargo(entry):
    p = os.path.join(entry.name, "Cargo.toml")
    if os.path.exists(p):
        os.chdir(entry.name)
        v = os.system("cargo build")
        if v != 0:
            sys.exit(v)
        os.chdir("..")

with os.scandir(".") as it:
    for entry in it:
        if not entry.name.startswith('.') and not entry.name.startswith('_') and entry.is_dir():
            build_tundra(entry)
            build_cargo(entry)