# importing libraries and modules
from dotenv import load_dotenv
import telebot
import os

# loading environment variables
load_dotenv()
TOKEN = os.getenv('API_KEY')

# creating bot object
class TelegramBot: # class to create a Telegram bot
    def __init__(self): # constructor
        self.bot = telebot.TeleBot(TOKEN) # creating a bot object
        self.bot.set_update_listener(self.listener) # setting listener
        self.bot.polling(none_stop=True) # starting bot

    def listener(self, messages): # listener
        for m in messages: # for each message
            if m.content_type == 'text': # if the message is text
                print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text) # print the message

    def run(self): # run method
        @self.bot.message_handler(commands=['start']) # decorator to handle the /start command
        def start(message): # function to handle the /start command
            self.bot.reply_to(message, 'Olá, eu sou o SmartCashBot, o seu assistente financeiro! Para começar, digite /help para ver as minhas funcionalidades.') # sending a message to the user

        @self.bot.message_handler(commands=['help']) # decorator to handle the /help command
        def help(message): # function to handle the /help command
            self.bot.reply_to(message, 'Para começar, digite /start para ver as minhas funcionalidades.') # sending a message to the user



