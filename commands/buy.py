from messages import BUY
from telegram.ext import CommandHandler


def buy_handler(bot, update, args):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=BUY
    )
    print(args)


buy = CommandHandler("buy", buy_handler, pass_args=True)
