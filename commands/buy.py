from messages import BUY
from telegram.ext import CommandHandler
import requests

API_URL = 'https://arqss4.ing.puc.cl/api'
QUEUE_URL = 'https://arqss5.ing.puc.cl/mail'

def buy_handler(bot, update, args, user_data):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=BUY
    )
    if not('token' in user_data.keys()):
        print('Falta hacer login')
        return 0

    #args[0] = product  args[1] = amount
   
    product_id = getID(args[0])
    if product_id == -1:
        print('Producto invalido')
        return 1

    amount = args[1]    
    data = [{"product_id":product_id, "amount":amount}]
    
    ## Falta continuar
    answer = postProduct(data, user_data)
    print(answer)

def getID(product_name):
    ACTION_URL = '/products'
    answer = requests.get(QUEUE_URL + ACTION_URL)
    for p in answer.json():
        if p['fields']['name'].upper() == product_name.upper():
            return p['pk']
    return -1

def postProduct(data, user_data):
    ACTION_URL = '/cart'
    a = requests.post(API_URL + ACTION_URL, data, headers={'Authorization':user_data['token']} )
    return a

buy = CommandHandler("buy", buy_handler, pass_args=True, pass_user_data=True)
