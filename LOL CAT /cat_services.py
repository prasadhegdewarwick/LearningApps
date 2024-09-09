import os.path
import shutil
import subprocess
import platform

from PIL import Image

import requests


def get_cat(full_path):
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"

    print("Downloading Cat Images............")
    for idx in range(1, 9):
        data = download_cat(url)

        print()
        print()
        print("Saving Images........")
        save_images(full_path, data, idx)

    print(f"Downloaded Cat Images are Save in {full_path} this Directories")


def download_cat(url):
    response = requests.get(url, stream=True)

    return response.raw


def save_images(full_path, data, idx):
    file_name = f"lolcat_{idx}"
    file_path = os.path.join(full_path, file_name + '.jpg')

    with open(file_path, 'wb') as fout:
        shutil.copyfileobj(data, fout)


def open_images(full_path):

    if platform.system() == "Darwin":
        subprocess.call(['open', full_path])
    else:

        subprocess.call(['explorer', full_path])

