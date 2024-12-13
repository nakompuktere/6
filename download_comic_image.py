import requests
from urllib.parse import urlparse
import os
import telegram
import time
import argparse
from dotenv import load_dotenv
import random


def download_comic_image(random_number):
    url = f'https://xkcd.com/{random_number}/info.0.json'
    response = requests.get(url)

    response.raise_for_status()

    file_path = os.path.join("images", "comic.png")
    comic_archive = response.json()
    image_url = comic_archive["img"]
    download_image(file_path, image_url)
    

def download_image(file_path, image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    
    with open(file_path, 'wb') as file:
        file.write(response.content)