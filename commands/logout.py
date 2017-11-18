from telegram.ext import CommandHandler


def logout_handler(bot, update, user_data):
    if "token" in user_data:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Tienes que iniciar sesión primero"
        )
    del user_data["token"]
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Has cerrado sesión correctamente."
    )

logout = CommandHandler("logout", logout_handler, pass_user_data=True)
