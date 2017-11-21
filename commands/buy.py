from messages import BUY
from telegram.ext import CommandHandler
import requests

API_URL = 'https://arqss4.ing.puc.cl/api'
QUEUE_URL = 'https://arqss5.ing.puc.cl'
AMOUNT = 1

def buy_handler(bot, update, args, user_data):
    if not('token' in user_data.keys()):
        bot.send_message(
            chat_id=update.message.chat_id,
            text='Debes realizar login mediante: /login')
        return 0
    elif not(args):
        bot.send_message(
            chat_id=update.message.chat_id,
            text= "Ingresa el nombre mediante: /buy \{producto\}")
        return 1
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text= "Buscando producto..")
        
    product_id = getID(" ".join(args))
    if product_id == -1:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Producto invalido.")
        return 2
    data = [{"product_id":product_id, "amount":AMOUNT}]
    
    ## Falta continuar
    print(data)
    postProduct(data, user_data)
    

def getID(product_name):
    ACTION_URL = '/products'
    answer = requests.get(QUEUE_URL + ACTION_URL)
    print(answer)
    for p in answer.json():
        if p['fields']['name'].upper() == product_name.upper():
            return p['pk']
    return -1

def postProduct(data, user_data):
    ACTION_URL = '/cart'
    answer = requests.post(API_URL + ACTION_URL, data, headers={'Authorization':user_data['token']} )
    print(answer)
    return answer

buy = CommandHandler("buy", buy_handler, pass_args=True, pass_user_data=True)
