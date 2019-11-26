import os
import sys
import shutil
from send2trash import send2trash

folder = "~/Downloads"
path = os.path.expanduser(folder)


def remove_unnecessary_files(extension="dmg"):
    with os.scandir(path) as it:
        if len(os.listdir(path)) == 0:
            print("No files were found in " + folder)
            return

        new_folder_name = path + "/" + extension.capitalize() + "_folder"

        for entry in it:
            if entry.name.endswith(extension):
                # this will create a new folder with the following pattern:
                # <extension>_folder
                make_new_directory(new_folder_name)

                print(entry.path, entry.name)

                # move all the files with specified extension to the new directory
                shutil.move(entry.path, new_folder_name)

    total_size = calculate_folder_size(new_folder_name)
    # if the size exceeds 500MB, move the whole folder to trash bin
    if total_size >= 500000000:
        # remove all the files in directory
        # shutil.rmtree(new_folder_name, ignore_errors=True)
        send2trash(new_folder_name)


# this function counts the total size of all files contains in the given folder
def calculate_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


# if there is no directory with given name, create a new one
def make_new_directory(new_folder_name):
    if os.path.isdir(new_folder_name):
        return
    else:
        os.mkdir(new_folder_name)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ext = sys.argv[1]
        print(ext)
        remove_unnecessary_files(ext)
    else:
        remove_unnecessary_files() # dng by default
