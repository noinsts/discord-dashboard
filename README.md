[![wakatime](https://wakatime.com/badge/user/5f28d705-3bc8-4138-8151-e12e0f9e9a23/project/abc20e82-72d8-48bb-a970-098ffff1baec.svg)](https://wakatime.com/badge/user/5f28d705-3bc8-4138-8151-e12e0f9e9a23/project/abc20e82-72d8-48bb-a970-098ffff1baec)

Do you speak English? [English Version](./README.en.md)

# discord-dashboard

**Discord Dashboard** — це вебзастосунок для перегляду статистики Discord-сервера в реальному часі.  

## 🚀 Чому це круто?

- **Повний огляд**: Отримуйте всю необхідну статистику вашого Discord-сервера в одному зручному місці.

- **Просте налаштування**: Швидко підключіть ваш сервер і почніть моніторинг без зайвих зусиль.

- **Сучасний дизайн**: Насолоджуйтеся інтуїтивно зрозумілим та адаптивним інтерфейсом, що чудово виглядає на будь-якому пристрої.

- **Відкритий код**: Завдяки відкритості проєкту ви можете легко розширювати функціонал та додавати власні метрики.

## 📌 Важливо

Я новачок у веброзробці, тому код може бути неідеальним і містити деякі недоліки. Якщо знайдеш баги чи маєш ідеї — буду радий, якщо скажеш! Не судіть строго, а допомагайте розвиватися 🙌

## 🖼️ Прев'ю

### 💻 Десктоп

<img src="assets/previews/desktop.png" alt="Скріншот сайту на пк" width="500">

### 📱 Смартфон

<img src="assets/previews/phone.png" alt="Скріншот сайту з телефону" width="200">

## 🧱 Стек і технології

### Backend:
- 🐍 [Python 3.12](https://www.python.org/downloads/release/python-3124/)
- 🌐 [Flask](https://flask.palletsprojects.com/) — серверна частина
- 🤖 [discord.py](https://discordpy.readthedocs.io/en/stable/) — інтеграція з Discord API
- 📦 [Poetry](https://python-poetry.org/) — менеджер залежностей
- 🔐 [python-dotenv](https://pypi.org/project/python-dotenv/) — тримає всі твої секрети у секреті

### Frontend:
- 🧱 [HTML](https://en.wikipedia.org/wiki/HTML) — структура сторінки
- 🎨 [CSS](https://en.wikipedia.org/wiki/CSS) — стилі та дизайн
- ⚙️ [JavaScript](https://en.wikipedia.org/wiki/JavaScript) — логіка і динаміка інтерфейсу

## ⚙️ Встановлення

### 1. Скопіюйте проект та встановіть залежності

```bash
git clone https://github.com/noinsts/discord-dashboard.git
cd discord-dashboard
 ```

### 2. Встановіть залежності

```bash
poetry install
```

### 3. Налаштуйте секретики діскорду

1. Створіть файл .env
   ```bash
   touch .env
   ```
2. Вкажіть в .env токен та id серверу, зразок в [.env.example](./.env.example)

### 4. Налаштуйте конфіг Flask-серверу

1. Зайдіть в [config.py](./src/backend/config.py) та змініть там наступне:
    ```python
    # Flask налаштування
    FLASK_HOST = '0.0.0.0'
    FLASK_PORT = 8080
    FLASK_DEBUG = True

    # LiveReload налаштування
    LIVERELOAD_PORT = 9098
    ```
   
### 5. Запустіть вже нарешті проект

```bash
poetry run python src/backend/main.py
```

## 🛡 Ліцензія

Цей проєкт ліцензовано під [MIT License](./LICENSE).

## ✨ Автор

[**@noinsts**](https://github.com/noinsts) – автор і розробник цього проекту.
