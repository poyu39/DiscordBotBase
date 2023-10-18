import discord
from discord.ext import commands

from settings import Config, logger, replier

CONFIG = Config()


class Demo(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info('>>已載入 Demo<<')

    @commands.command()
    async def ping(self, ctx):
        reply_embed = replier.info(
            'Pong!', f'延遲: {self.bot.latency * 1000:.2f} ms'
        )
        await ctx.send(embed=reply_embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Demo(bot), guild=bot.get_guild(CONFIG.GUILD_ID))
