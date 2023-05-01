import requests
import json
import telegram
from telegram import ParseMode, Update
# функция, которая будет вызываться при команде /info
def info_command(update: Update, context):
    # запоминаем команду, чтобы пользователь мог просто ввести никнейм без указания команды
    if not context.user_data.get('command'):
        context.user_data['command'] = '/info'
    
    # проверяем, что пользователь указал никнейм игрока
    if len(context.args) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Укажите никнейм игрока после команды /info')
        return
    
    # отправляем GET-запрос на указанный URL с указанием никнейма игрока
    url = f'https://wfbot.cf/api/player/{context.args[0]}'
    response = requests.get(url)

    # проверяем статус ответа и выводим ошибку, если игрок не найден
    result = response.json()
    if result.get('code') == 'player_not_found':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Игрок с таким никнеймом не найден.')
        return
    elif result.get('code') == 'inactive':
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'К сожалению, игрок "{context.args[0]}" ни разу не был сохранен в нашей базе данных, мы не сможем вывести его статистику =(')
        return
    if result.get('code') == 'hidden':
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Игрок "{context.args[0]}" скрыл свою статистику.\nИгрок ни разу не был сохранен в нашей базе данных, мы не сможем вывести его статистику =(')
        return
    if response.status_code == 200:
        # если все ок, выводим результат в чат-бота в виде текста
        nickname = result['player']['nickname']
        kills = result['player']['kills']
        death = result['player']['death']
        kdratio = result['player']['pvp']
        pve_kills = result['player']['pve_kills']
        pve_death = result['player']['pve_death']
        pve_kdratio = result['player']['pve']
        favorit_pvp = result['player']['favoritPVP']
        favorit_pve = result['player']['favoritPVE']
        playtime_h = result['player']['playtime_h']
        clan = result['player'].get('clan_name', 'Отсутствует')

        if favorit_pvp:
            if favorit_pvp == "Medic":
                favorit_pvp = "Медик"
            elif favorit_pvp == "Engineer":
                favorit_pvp = "Инженер"
            elif favorit_pvp == "Rifleman":
                favorit_pvp = "Штурмовик"
            elif favorit_pvp == "Sniper":
                favorit_pvp = "Снайпер"
        else:
            favorit_pvp = "Отсутствует"

        if favorit_pve:
            if favorit_pve == "Medic":
                favorit_pve = "Медик"
            elif favorit_pve == "Engineer":
                favorit_pve = "Инженер"
            elif favorit_pve == "Rifleman":
                favorit_pve = "Штурмовик"
            elif favorit_pve == "Sniper":
                favorit_pve = "Снайпер"
        else:
            favorit_pve = "Отсутствует"

        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Никнейм: {nickname}\nУбийства (PvP): {kills}\nСмерти (PvP): {death}\nK/D (PvP): {kdratio}\nУбийства (PvE): {pve_kills}\nСмерти (PvE): {pve_death}\nK/D (PvE): {pve_kdratio}\nЛюбимый класс в PvP: {favorit_pvp}\nЛюбимый класс в PvE: {favorit_pve}\nОбщее время игры: {playtime_h} часов\nКлан: {clan}')
    else:
        # если что-то пошло не так, выводим сообщение об ошибке
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Ошибка {response.status_code}: {response.text}')
if __name__ == '__main__': main()
