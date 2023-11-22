#!/usr/bin/env python3
import os
from sys import platform
from pathlib import Path
import shutil

def install(profile_dir):
    # Setup target paths
    user_js_target_path = f"{profile_dir}/user.js"
    user_chrome_target_path = f"{profile_dir}/chrome/userChrome.css"

    # Copy files into profile directory
    shutil.copyfile("./user.js", user_js_target_path)
    shutil.copyfile("./userChrome.css", user_chrome_target_path)


def main():
    # What OS are we in right now?
    if platform == "linux" or platform == "linux2":
        raise Exception("Not implemented yet!")
    elif platform == "darwin":
        home_dir = str(Path.home())
        base_install_path = f"{home_dir}/Library/Application Support/Firefox/Profiles"
    elif platform == "win32":
        raise Exception("Not implemented yet!")

    # Check for profiles
    profile_dirs = [ f.path for f in os.scandir(base_install_path) if f.is_dir() ]
    if len(profile_dirs) > 1:
        print("Multiple profiles found. Please choose the target profile.")
        for index, profile_dir in enumerate(profile_dirs):
            print(f"{index + 1}. {profile_dir}")
        print(f"{len(profile_dirs) + 1}. Copy to all profile directories")
        choice = int(input("Your selection: ")) - 1
    else:
        choice = 0

    if choice == len(profile_dirs):
        for profile_dir in profile_dirs:
            install(profile_dir)
    else:
        install(profile_dirs[0])

if __name__=="__main__":
    main()