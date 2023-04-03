import requests
import json
import telegram
from telegram import ParseMode, Update

def help_command(update: Update, context):
    # выводим подсказку по использованию бота
    context.bot.send_message(chat_id=update.effective_chat.id, text="Этот бот предназначен для получения информации о Warface. Доступны следующие команды:\n/online - получить информацию о количестве игроков онлайн на RU и INT серверах\n/info [никнейм игрока] - получить информацию об онлайне и статусе указанного игрока\n/help - получить справку по использованию бота")
    
if __name__ == '__main__': main()
