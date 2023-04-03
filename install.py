import subprocess
import sys
import json
# установка необходимых библиотек
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot==13.7"])

# получение токена
token = input("Введите токен вашего бота: ")

# запись токена в файл
with open('config.json', 'w') as f:
    json.dump({'token': token}, f)

print("Установка завершена.")