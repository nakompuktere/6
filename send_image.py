import os
import telegram
import time
from dotenv import load_dotenv
from pathlib import Path
import random
from download_comic_images import get_comic_image


def send_files(chat_id, bot, image_path):
    with open(image_path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)



def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    load_dotenv()
    image_path = os.path.join("images", "comic.png")
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    default_chat_id = os.environ["TG_CHAT_ID"]

    first_comic_id = 1
    last_comic_id = 614
    random_number = random.randint(first_comic_id, last_comic_id)
    get_comic_image(random_number)


    try:
        send_files(default_chat_id, bot, image_path)
    finally:
        os.remove(image_path)


if __name__ == "__main__":
    main()