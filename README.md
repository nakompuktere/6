# Публикация комиксов
данная программа скачивает комикс один раз в день и отправляет их ботом в телеграмм.

### Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Переменная окружения «TG_CHAT_ID» хранит id чата Telegram канала, на который бот будет отправлять комиксы.
Переменная окружения «TELEGRAM_TOKEN» хранит токен бота, который позволяет управлять им.

### Как запустить
для запуска бота следует ввести в терминал:
```
python python_telegram_bot.py
```
указать ключ "delay" - задержка между отправкой всех фото и ключ "chat_id" - ваш чат id.
```
python python_telegram_bot.py --delay время в секундах --chat_id "ваш чат id"
```

### Цели проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).