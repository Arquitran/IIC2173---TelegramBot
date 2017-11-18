import requests
import json
from os import environ
from messages import LOGIN
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters, RegexHandler


TYPING_EMAIL, TYPING_PASSWORD = range(2)


def init_handler(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Por favor, escribe tu correo registrado en nuestra web.")
    return TYPING_EMAIL

init = CommandHandler("login", init_handler)

def email_handler(bot, update, user_data):
    chat_id = update.message.chat_id
    email = update.message.text
    user_data["email"] = email
    bot.send_message(chat_id=chat_id, text="Por favor, ingresa tu contraseña. Por tu seguridad, borra el mensaje después.")
    return TYPING_PASSWORD

email = MessageHandler(Filters.text, email_handler, pass_user_data=True)

def password_handler(bot, update, user_data):
    password = update.message.text
    chat_id = update.message.chat_id
    email = user_data["email"]
    res = requests.post(environ["API_URL"] + "/api/signin",json.dumps({"email": email, "password": password}), headers={"Content-Type": "application/json"})
    print(res)
    token = res.json()["token"]
    user_data["token"] = token
    bot.send_message(chat_id=chat_id, text=token)
    return ConversationHandler.END

password = MessageHandler(Filters.text, password_handler, pass_user_data=True)

def cancel_handler(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Ok, cancelando.")
    return ConversationHandler.END

cancel = RegexHandler('^Cancelar$', cancel_handler, pass_user_data=True)

entry_points = [init]
states = {
    TYPING_EMAIL: [email],
    TYPING_PASSWORD: [password]
}
fallbacks = [cancel]

login = ConversationHandler(entry_points=entry_points, states=states, fallbacks=fallbacks, per_user=True)
