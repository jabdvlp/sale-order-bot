from datetime import datetime
import telebot
from telebot import types
from config.db import conn
from config.order import orders
from config.schemas import Order
import pandas as pd
import os
from dotenv import load_dotenv

# TOKEN = "5046627714:AAEhMoR-l8xyalkky-S1eS60GCwWCzb7rO0"
load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

value = "Bienvenido al Bot de Ordenes de Compra \n Welcome to the Sale Order Bot \n \n Use el comando /help para mostrar la lista de comandos"
msj = "Envie su pedido con el siguiente formato \n \n CodigoCliente,CodigoProducto,Cantidad,Unidad "
msj_help = "Lista de comandos disponibles: \n /start \n /order \n /help"

@bot.chat_join_request_handler()

@bot.message_handler(commands=['start'])
def sendWelcome(message):
    bot.reply_to(message, value)
   # bot.reply_to(message, "This is a message handler")

@bot.message_handler(commands=['help'])
def sendWelcome(message):
    bot.reply_to(message, msj_help)
    bot.set_update_listener(listener)

@bot.message_handler(commands=['order'])
def sendWelcome(message):
    bot.reply_to(message, msj)
    bot.set_update_listener(listener)

def listener(mensajes):
    for msj in mensajes:
        chat_id = msj.chat.id
        texto = msj.text
        data_list = texto.split(',')
        new_order = {"client":data_list[0], "sku":data_list[1], "quantity":data_list[2], "unit":data_list[3], "time":datetime.now()}
        result = conn.execute(orders.insert().values(new_order))

        print('ID: ' + str(chat_id) + ' - MENSAJE: ' + texto + str(new_order)) 
        # list = pd.DataFrame(data_list, columns= "Cliente","Código","Cantidad","Unidad")
 


bot.infinity_polling()





""" 
@bot.message_handler(func=lambda message: True)
def echoAll(message):
    bot.reply_to(message, message.text)
 """