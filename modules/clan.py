import requests
import json
import telegram
from telegram import ParseMode, Update
def clan_command(update: Update, context):
    # проверяем, что пользователь указал название клана
    if len(context.args) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Укажите название клана после команды /clan')
        return
    
    # отправляем GET-запрос на указанный URL с указанием названия клана
    url = f'https://wfs.globalart.dev/api/clan/{context.args[0]}'
    response = requests.get(url)

    # проверяем статус ответа
    if response.status_code == 200:
        # если все ок, выводим результат в чат-бота
        result = response.json()[0]['data']
        clan_name = result['name']
        members = result['members']
        members_list = '\n'.join([f"{member['nickname']} - {translate_role(member['clan_role'])}" for member in members])
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Клан: {clan_name}\nУчастники:\n{members_list}')
    elif response.status_code == 404:
        # если клан не существует, выводим соответствующее сообщение
        clan_name = context.args[0]
        error_message = f'Клан "{clan_name}" не найден.'
        context.bot.send_message(chat_id=update.effective_chat.id, text=error_message)
    else:
        # если что-то пошло не так, выводим сообщение об ошибке
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Ошибка {response.status_code}: {response.text}')

def translate_role(role):
    translations = {'MASTER': 'Глава', 'OFFICER': 'Офицер', 'REGULAR': 'Рядовой'}
    return translations.get(role, role)

if __name__ == '__main__': main()
