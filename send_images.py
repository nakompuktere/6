import os
import telegram
import time
from dotenv import load_dotenv
from pathlib import Path
import random
from download_comic_images import get_comic_image


def send_files(chat_id, bot):
    first_comic_id = 1
    last_comic_id = 614
    random_number = random.randint(first_comic_id, last_comic_id)
    get_comic_image(random_number)
    with open("images/comic.png", 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)



def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    load_dotenv()
    bot = telegram.Bot(token=os.getenv("TELEGRAM_TOKEN"))
    default_chat_id = os.getenv("TG_CHAT_ID")
    try:
        send_files(default_chat_id, bot)
    finally:
        os.remove("images/comic.png")


if __name__ == "__main__":
    main()