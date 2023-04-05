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
        ru_pvp_players = result['ru']['pvp']
        ru_pve_players = result['ru']['pve']
        ru_all_players = result['ru']['all']
        int_pvp_players = result['int']['pvp']
        int_pve_players = result['int']['pve']
        int_all_players = result['int']['all']
        
        message = f'На сервере RU сейчас онлайн:\n\n- PvP: {ru_pvp_players} \n- PvE: {ru_pve_players} \n- Всего: {ru_all_players} \n\nНа сервере EU сейчас онлайн:\n\n- PvP: {int_pvp_players} \n- PvE: {int_pve_players} \n- Всего: {int_all_players} '
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        # если что-то пошло не так, выводим сообщение об ошибке
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Ошибка {response.status_code}: {response.text}')
        
    if __name__ == '__main__': main()
