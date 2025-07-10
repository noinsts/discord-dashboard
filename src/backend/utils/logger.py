import logging
import os


def setup_logger():
    logger = logging.getLogger("discord_bot")
    logger.setLevel(logging.INFO)

    # Формат логів
    log_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    # Створюємо директорію, якщо її ще нема
    log_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "log", "debug")
    os.makedirs(log_dir, exist_ok=True)

    log_file_path = os.path.join(log_dir, "app.log")

    # 📂 Запис у файл `log/debug/bot.log`
    file_handler = logging.FileHandler(log_file_path, mode="a")
    file_handler.setFormatter(log_format)

    # 🖥️ Вивід у консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    # Додаємо хендлери (попередньо очищаємо старі)
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
