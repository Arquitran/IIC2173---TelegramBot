import logging
from commands import HANDLERS
from telegram.ext import Updater
from os import environ


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == "__main__":
    updater = Updater(token=environ["TELEGRAM_TOKEN"])
    dispatcher = updater.dispatcher

    print("Agregando handlers...")
    for handler in HANDLERS:
        dispatcher.add_handler(handler)

    updater.start_polling()
    print("To stop bot press CTRL + C (maybe repeatedly)")
    updater.idle()
    print("Stopping bot...")
    updater.stop()
