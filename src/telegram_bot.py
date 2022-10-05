# importing libraries and modules
from dotenv import load_dotenv
import telebot
import os

load_dotenv()
TOKEN = os.getenv('API_KEY')

bot = telebot.TeleBot(TOKEN)
