import os
import shutil


def get_file_path():
    base_folder = os.path.dirname(__file__)
    folder = "cat_pictures"
    full_path = os.path.join(base_folder, folder)
    print(full_path)

    if os.path.exists(full_path) or os.path.isdir(full_path):
        print(f" Deleting Old Directory from {full_path}")
        # os.rmdir(full_path)
        shutil.rmtree(full_path)
    # if not os.path.exists(full_path) or not os.path.isdir(full_path):
    print(f"Creating new Directory at {full_path}")
    os.mkdir(full_path)
    return full_path
