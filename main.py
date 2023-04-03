import requests
import json
import telegram
from telegram import ParseMode, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from modules.info import info_command
from modules.online import online_command
from modules.clan import clan_command
from modules.help import help_command

# чтение токена из файла
with open('config.json') as f:
    config = json.load(f)
    TOKEN = config['token']

# функция, которая будет вызываться при команде /start
def start_command(update, context):
    # создаем меню команд
    keyboard = [
        [telegram.KeyboardButton('/online')],
        [telegram.KeyboardButton('/info')],
        [telegram.KeyboardButton('/clan')],
    ]
    # создаем объект ReplyKeyboardMarkup и добавляем к нему меню
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard)
    # приветствуем пользователя и описываем доступные команды
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для получения информации о Warface. Вот мои доступные команды:", reply_markup=reply_markup)
    # сохраняем команду, на которую пользователь нажмет в меню, в контексте
    context.user_data['command'] = ''
    
def message_handler(update, context):
    # проверяем, что пользователь ввел никнейм при вызове команды /info
    if context.user_data.get('command') == '/info':
        context.args = [update.message.text]
        info_command(update, context)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Используйте команды для работы с ботом.')

# создаем экземпляр бота и добавляем обработчики команд
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('online', online_command))
updater.dispatcher.add_handler(CommandHandler('info', info_command))
updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('clan', clan_command))

updater.start_polling()
updater.idle()

if __name__ == '__main__': main()
