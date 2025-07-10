import asyncio
import logging
import threading

from livereload import Server

from config import Config
from client import DiscordClient
from app import FlaskServer
from utils import setup_logger

logging = setup_logger()


def run_discord_client(discord_client):
    """Запуск Discord клієнта в окремому потоці"""
    try:
        asyncio.run(discord_client.start())
    except Exception as e:
        logging.error(f'Критична помилка Discord клієнта: {e}')


def run_flask_server(flask_server):
    """Запуск Flask сервера"""
    if Config.FLASK_DEBUG:
        server = Server(flask_server.get_app().wsgi_app)
        server.watch(Config.TEMPLATE_DIR)
        server.watch(Config.STATIC_DIR)
        server.serve(port=Config.LIVERELOAD_PORT, host=Config.FLASK_HOST, debug=True)
    else:
        flask_server.run()


def main():
    try:
        # Створюємо екземпляри класів
        discord_client = DiscordClient()
        flask_server = FlaskServer(discord_client)

        # Запускаємо Discord бота в окремому потоці
        discord_thread = threading.Thread(
            target=run_discord_client,
            args=(discord_client,),
            daemon=True
        )
        discord_thread.start()

        # Запускаємо Flask сервер
        run_flask_server(flask_server)

    except KeyboardInterrupt:
        logging.info('Програма зупинена користувачем')
    except Exception as e:
        logging.error(f'Критична помилка: {e}')
    finally:
        logging.info('Програма завершена')


if __name__ == "__main__":
    main()
