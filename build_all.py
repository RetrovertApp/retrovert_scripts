from asyncio import subprocess
import os
import platform
import sys

def build_cmake(entry, cmake_target):
    p0 = os.path.join(entry, "CMakeLists.txt")
    if os.path.exists(p0):
        if not os.path.exists(os.path.join(entry, "build")):
            os.mkdir(os.path.join(entry, "build"))

        os.chdir(os.path.join(entry, "build"))
        cmd = "cmake .." + " -G \"" + cmake_target + "\""
        v = os.system(cmd)
        if v != 0:
            sys.exit(v)

        v = os.system("cmake --build .")
        if v != 0:
            sys.exit(v)

        os.chdir("../..")

def build_cargo(entry):
    p = os.path.join(entry, "Cargo.toml")
    if os.path.exists(p):
        print("Building " + entry)
        os.chdir(entry)
        v = os.system("cargo build")
        if v != 0:
            sys.exit(v)
        os.chdir("..")

def get_cmake_target_for_platform():
    if platform.system() == "Windows":
        return "Visual Studio 19 2022"
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        v = os.system("ninja --version")
        if v == 0:
            return "Ninja"
        else:
            return "Unix Makefiles"
    else:
        return None

cmake_target = get_cmake_target_for_platform()

with os.scandir(".") as it:
    for entry in it:
        if not entry.name.startswith('.') and not entry.name.startswith('_') and entry.is_dir():
            abs_path = os.path.abspath(entry.name)
            build_cmake(abs_path, cmake_target)
            build_cargo(abs_path)
