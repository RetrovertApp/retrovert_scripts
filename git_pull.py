import os

with os.scandir(".") as it:
    for entry in it:
        if entry.is_dir():
            os.chdir(entry)
            os.system("git pull")
            os.chdir("..")
