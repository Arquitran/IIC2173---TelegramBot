import logging
from commands import start, buy
from telegram.ext import Updater, CommandHandler
from os import environ


def add_handlers(dispatcher, handlers):
    for handler in handlers:
        dispatcher.add_handler(CommandHandler(handler.__name__, handler))


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == "__main__":
    updater = Updater(token=environ["TELEGRAM_TOKEN"])
    dispatcher = updater.dispatcher
    add_handlers(dispatcher, [start, buy])
    updater.start_polling()
    input("Press any key to stop bot")
    updater.stop()
