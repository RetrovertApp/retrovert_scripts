import os
import shutil

for subdir, dirs, files in os.walk("."):
    for dir in dirs:
        v = os.path.join(dir, "retrovert_api")
        if os.path.exists(v) and dir != "retrovert_api":
            git_dir = os.path.join(dir, "retrovert_api/.git")
            print("Copy from retrovert_api to " + v)
            shutil.rmtree(v)
            shutil.copytree("retrovert_api", v)
            shutil.rmtree(git_dir)
            shutil.copy2("retrovert_scripts/tundra.lua", dir)
            shutil.copy2("retrovert_scripts/.clang-format", dir)
    break

