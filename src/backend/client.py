import discord
from discord.ext import commands

from config import Config


class DiscordClient:
    def __init__(self):
        self.token = Config.DISCORD_TOKEN
        self.server_id = Config.DISCORD_SERVER_ID
        self.log = Config.logger
        self.server = None
        self._ready = False

        # підключення інтентів
        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True

        self.client = commands.Bot(
            command_prefix='.',
            intents=intents
        )

        self.stats = {
            "online": 0,
            "allmembers": 0,
            "invoice": 0
        }

        self._setup_events()

    def _setup_events(self):
        @self.client.event
        async def on_ready():
            """Метод, що спрацьовує після запуску бота автоматично"""
            self._ready = True
            self.server = self.client.get_guild(self.server_id)

            if self.server:
                self.log.info(f"Бот підключено як {self.client.user}")
                self.log.info(f"Сервер {self.server.name} знайдено")

                try:
                    await self.server.chunk()
                    self.log.info(f"Завантажено {len(self.server.members)} учасників.")
                except Exception as e:
                    self.log.error(f"Помилка завантаження учасників: {e}")
            else:
                self.log.error(f"Не вдалося встановити підключення з сервером {self.server_id}")
                self._ready = False

    async def start(self):
        """Метод, що запускає Discord клієнт"""
        self.log.info("Запуск Discord клієнта")
        await self.client.start(self.token)

    def is_ready(self):
        """Getter статусу бота"""
        return self._ready

    async def update_data(self):
        """Метод, що оновлює дані self.stats"""
        if not self.server:
            return

        try:
            self.stats["online"] = await self.get_online_member_count()
            self.stats["allmembers"] = await self.get_member_count()
            self.stats["invoice"] = await self.get_invoice_member_count()
        except Exception as e:
            self.log.error(f"Помилка оновлення статистики: {e}")

    async def get_member_count(self):
        """Повертає кількість учасників серверу"""
        if self.server:
            return self.server.member_count
        return 'Невідомий сервер'

    async def get_online_member_count(self):
        """Повертає кількість учасників серверу, які в мережі"""
        online_members = 0

        if self.server:
            for member in self.server.members:
                if member.status != discord.Status.offline:
                    online_members += 1

        return online_members

    async def get_invoice_member_count(self):
        """Повертає кількість учасників серверу, що знаходяться у войсі"""
        voice_member = 0

        if self.server:
            for voice_channel in self.server.voice_channels:
                voice_member += len(voice_channel.members)

        return voice_member
