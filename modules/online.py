import requests
import json
import telegram
from telegram import ParseMode, Update
def online_command(update: Update, context):
    # отправляем GET-запрос на указанный URL
    url = 'https://wfbot.cf/api/online'
    response = requests.get(url)

    # проверяем статус ответа
    if response.status_code == 200:
        # если все ок, выводим результат в чат-бота в виде текста
        result = response.json()
        ru_players = result['ru']['all']
        int_players = result['int']['all']
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'На сервере RU сейчас онлайн {ru_players} игроков, а на сервере INT - {int_players} игроков.')
    else:
        # если что-то пошло не так, выводим сообщение об ошибке
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Ошибка {response.status_code}: {response.text}')
        
    if __name__ == '__main__': main()