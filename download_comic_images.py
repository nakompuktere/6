import requests
from urllib.parse import urlparse
import os
import telegram
import time
import argparse
from dotenv import load_dotenv
import random


def get_comic_image(random_number):
    url = f'https://xkcd.com/{random_number}/info.0.json'
    response = requests.get(url)

    response.raise_for_status()

    file_path = "images/comic.png"
    comic_archive = response.json()
    image_url = comic_archive["img"]
    comment = comic_archive["alt"]
    download_image(file_path, image_url)
    

def download_image(file_path, image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    
    with open(file_path, 'wb') as file:
        file.write(response.content)