import requests
import json
from os import environ
from messages import LOGIN
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters, RegexHandler


TYPING_EMAIL, TYPING_PASSWORD = range(2)


def init_handler(bot, update, user_data):
    if "token" in user_data:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Ya iniciaste sesión. Para cerrar la sesión usa /logout."
        )
        return ConversationHandler.END
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Por favor, escribe tu correo registrado en nuestra web. Para cancelar, usa /cancel."
    )
    return TYPING_EMAIL

init = CommandHandler("login", init_handler, pass_user_data=True)


def email_handler(bot, update, user_data):
    chat_id = update.message.chat_id
    email = update.message.text
    user_data["email"] = email
    bot.send_message(chat_id=chat_id, text="Por favor, ingresa tu contraseña. Por tu seguridad, borra el mensaje después. Para cancelar, usa /cancel.")
    return TYPING_PASSWORD

email = MessageHandler(Filters.text, email_handler, pass_user_data=True)


def password_handler(bot, update, user_data):
    password = update.message.text
    email = user_data["email"]
    chat_id = update.message.chat_id
    res = requests.post(
        environ["API_URL"] + "/api/signin",
        json.dumps({"email": email, "password": password}),
        headers={"Content-Type": "application/json"}
    )
    if res.status_code == 200:
        token = res.json()["token"]
        user_data["token"] = token
        bot.send_message(
            chat_id=chat_id,
            text="Has iniciado sesión correctamente como {}.".format(email)
        )
        del user_data["email"]
        return ConversationHandler.END
    bot.send_message(
        chat_id=chat_id,
        text="Correo o contraseña inválidos. Por favor, vuelve a ingresar tu correo. Para cancelar, usa /cancel."
    )
    return TYPING_EMAIL

password = MessageHandler(Filters.text, password_handler, pass_user_data=True)


def cancel_handler(bot, update, user_data):
    if "email" in user_data:
        del user_data["email"]
    bot.send_message(chat_id=update.message.chat_id, text="Ok, cancelado.")
    return ConversationHandler.END

cancel = CommandHandler("cancel", cancel_handler, pass_user_data=True)


entry_points = [init]
states = {
    TYPING_EMAIL: [email],
    TYPING_PASSWORD: [password]
}
fallbacks = [cancel]

login = ConversationHandler(entry_points, states, fallbacks, per_user=True)
