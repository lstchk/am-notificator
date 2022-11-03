import telebot
from telebot import types
from utils.config_reader import config


bot = telebot.TeleBot(config["telegram_token"])
