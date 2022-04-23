import os
from distutils.dir_util import copy_tree
import shutil

for subdir, dirs, files in os.walk("."):
    for dir in dirs:
        if dir.startswith("rv_"):
            v = os.path.join(dir, "retrovert_api")
            git_dir = os.path.join(dir, "retrovert_api/.git")
            copy_tree("retrovert_api", v)
            shutil.rmtree(git_dir)
            shutil.copy2("retrovert_scripts/tundra.lua", dir)
            shutil.copy2("retrovert_scripts/.clang-format", dir)
    break

