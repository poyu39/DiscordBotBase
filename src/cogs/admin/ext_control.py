import discord
from discord.ext import commands

from settings import Config, logger

CONFIG = Config()


class ExtControl(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info('>>ExtControl is loaded<<')

    @commands.command()
    async def un(self, ctx, extension):
        if ctx.author.id != CONFIG.OWNER_ID:
            await ctx.send('此指令僅限擁有者使用')
            return
        await self.bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'unloaded {extension} done')

    @commands.command()
    async def re(self, ctx, extension):
        await self.bot.reload_extension(f'cogs.{extension}')
        await self.bot.tree.sync(guild=discord.Object(id=CONFIG.GUILD_ID))
        logger.info(f'reloaded {extension} done')
        await ctx.send(f'reloaded {extension} done')

    @commands.command()
    async def l(self, ctx, extension):
        await self.bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'loaded {extension} done')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExtControl(bot), guild=bot.get_guild(CONFIG.GUILD_ID))
