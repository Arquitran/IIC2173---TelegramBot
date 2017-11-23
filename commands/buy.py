from messages import BUY
from telegram.ext import CommandHandler
from os import environ
import requests
import json

QUEUE_URL = 'https://arqss5.ing.puc.cl'
AMOUNT = 1

def buy_handler(bot, update, args, user_data):
    if not('token' in user_data.keys()):
        bot.send_message(
            chat_id=update.message.chat_id,
            text='Debes realizar login mediante: /login')
        return 1
    elif not(args):
        bot.send_message(
            chat_id=update.message.chat_id,
            text= "Ingresa el nombre mediante: /buy {producto}")
        return 2
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text= "Buscando producto..")
        
    product_id = getID(" ".join(args))
    if product_id == -1:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Producto invalido.")
        return 3
    data = [{"product_id":str(product_id), "amount":str(AMOUNT)}]
    print(data)
    response = postProduct(data, user_data)    
    if response.status_code == 200:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Producto procesado correctamente.")
        return 0
    elif response.status_code == 401:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Ha ocurrido un error con las credenciales.")
        return 4
    else:
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Ha ocurrido un error inesperado.")
        return 6



def getID(product_name):
    ACTION_URL = '/products'
    answer = requests.get(QUEUE_URL + ACTION_URL)
    print(answer)
    for p in answer.json():
        if p['fields']['name'].upper() == product_name.upper():
            return p['pk']
    return -1

def postProduct(data, user_data):
    ACTION_URL = '/api/cart'
    header = {'Authorization':user_data['token']}
    print(data)
    answer = requests.post(environ["API_URL"] + ACTION_URL, json.dumps(data), headers = header )
    print(answer)
    print(answer.text)
    return answer

buy = CommandHandler("buy", buy_handler, pass_args=True, pass_user_data=True)
