from telegram.ext import CommandHandler


def save_handler(bot, update, args, user_data):
    user_data[args[0]] = args[1]
    bot.send_message(
        chat_id=update.message.chat_id,
        text=str(user_data)
    )


save = CommandHandler("save", save_handler, pass_args=True, pass_user_data=True)
