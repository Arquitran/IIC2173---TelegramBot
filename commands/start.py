from messages import START
from telegram.ext import CommandHandler


def start_handler(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=START
    )


start = CommandHandler("start", start_handler)
