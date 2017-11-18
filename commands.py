import messages


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=messages.START
    )


def buy(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=messages.BUY
    )
