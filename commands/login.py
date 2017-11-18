from messages import LOGIN
from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters

users = dict()

def init_handler(bot, update):
    print(update.message)
    bot.send_message(chat_id=update.message.chat_id, text="test")

init = CommandHandler("login", init_handler)

# def email_handler(bot, update):
#     chat_id = update.message.chat_id
#     email = update.message.text
#     bot.send_message(chat_id=chat_id, text=email)
#
# email = MessageHandler(Filters.text, email_handler, pass_user_data=True)
#
# def password_handler(bot, message):
#     password = update.message.text
#     chat_id = update.message.chat_id
#     bot.send_message(chat_id=chat_id, text=password)
#
# password = MessageHandler(Filters.text, password_handler, pass_user_data=True)
#
#
# entry_points = [init]
# states = {
#     "WAITING_EMAIL": email,
#     "WAITING_PASSWORD": password
# }
# fallbacks = []
#
# login = ConversationHandler(entry_points, states, fallbacks, per_user=True)

login = init
