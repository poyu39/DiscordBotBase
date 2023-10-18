import asyncio
import os

import discord
from discord.ext import commands

from settings import Config, logger

CONFIG = Config()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=CONFIG.COMMDAND_PREFIX,
            intents=discord.Intents.all(),
            application_id=CONFIG.APPLICATION_ID,
        )

        self.initial_extensions = [
            'cogs.admin.ext_control',
            'cogs.admin.demo',
        ]

        self.workspace = os.getcwd()
        self.bot_dir = os.path.dirname(os.path.abspath(__file__))

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)
        await self.tree.sync(guild=discord.Object(id=CONFIG.GUILD_ID))

    async def on_ready(self):
        logger.info(">>Bot is online<<")
        activity = discord.Game(CONFIG.ACTIVITY)
        await self.change_presence(activity=activity)

    async def close(self):
        await super().close()


bot = Bot()
bot.run(token=CONFIG.TOKEN, log_handler=None)
