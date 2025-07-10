import os
from dotenv import load_dotenv

from utils import setup_logger

load_dotenv()


class Config:
    # Discord налаштування
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    DISCORD_SERVER_ID = int(os.getenv("DISCORD_SERVER_ID"))

    # Flask налаштування
    FLASK_HOST = '0.0.0.0'
    FLASK_PORT = 8080
    FLASK_DEBUG = True

    # LiveReload налаштування
    LIVERELOAD_PORT = 9098

    # Шляхи
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_DIR = os.path.join(BASE_DIR, '../frontend/templates')
    STATIC_DIR = os.path.join(BASE_DIR, '../frontend/static')

    # Логування
    logger = setup_logger()
