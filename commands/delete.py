from telegram.ext import CommandHandler


def delete_handler(bot, update, args, user_data):
    key = args[0]
    if key in user_data:
        del user_data[key]
    bot.send_message(
        chat_id=update.message.chat_id,
        text=str(user_data)
    )


delete = CommandHandler("delete", delete_handler, pass_args=True, pass_user_data=True)
