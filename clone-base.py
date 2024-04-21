import subprocess
import os

repositories = [
    "retrovert-console",
    "retrovert-core",
    "core-loader",
    "libopenmpt_playback",
]

def clone_repo(repo):
    repo_url = "https://github.com/RetrovertApp/" + repo
    try:
        if not os.path.exists(repo):
            repo_url = "https://github.com/RetrovertApp/" + repo
            print(f"Cloning {repo_url}")
            subprocess.run(["git", "clone", repo_url], check=True)
            print(f"Successfully cloned {repo_url}")
    except subprocess.CalledProcessError:
        print(f"Failed to clone {repo_url}")

for repo in repositories:
    clone_repo(repo)

print("All repositories cloned successfully")
