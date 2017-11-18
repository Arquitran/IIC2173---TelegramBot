from telegram.ext import CommandHandler


def about_handler(bot, update, user_data):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=str(user_data)
    )


about_me = CommandHandler("about_me", about_handler, pass_user_data=True)
