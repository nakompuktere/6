import os
import telegram
import time
import argparse
from dotenv import load_dotenv
import random
from download_comic_images import get_comic_image


def send_files(delay, chat_id, bot):
    while True:
        random_number = random.randint(1, 614)
        get_comic_image(random_number)

        with open("images/comic.png", 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
        time.sleep(delay)

def main():
    load_dotenv()
    bot = telegram.Bot(token=os.getenv("TELEGRAM_TOKEN"))
    default_chat_id = os.getenv("TG_CHAT_ID")
    parser = argparse.ArgumentParser(description='бот присылает комикс один раз в день')
    parser.add_argument('--chat_id', help='ваш chat id', default=default_chat_id)
    parser.add_argument('--delay', help='выберете задержку', default=86400, type=int)
    args = parser.parse_args()
    try:
        send_files(args.delay, args.chat_id, bot)
    finally:
        os.remove("images/comic.png")

if __name__ == "__main__":
    main()