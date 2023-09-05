import discord
from discord.ext import commands

from settings import Config, logger, replier

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
            reply_embed = replier.error(value='此指令僅限擁有者使用')
            await ctx.send(embed=reply_embed)
        else:
            await self.bot.unload_extension(f'cogs.{extension}')
            logger.info(f'unloaded {extension} done')
            reply_embed = replier.success(value=f'已卸載 {extension}')
            await ctx.send(embed=reply_embed)

    @commands.command()
    async def re(self, ctx, extension):
        if ctx.author.id != CONFIG.OWNER_ID:
            reply_embed = replier.error(value='此指令僅限擁有者使用')
            await ctx.send(embed=reply_embed)
        else:
            await self.bot.reload_extension(f'cogs.{extension}')
            await self.bot.tree.sync(guild=discord.Object(id=CONFIG.GUILD_ID))
            logger.info(f'reloaded {extension} done')
            reply_embed = replier.success(value=f'已重新載入 {extension}')
            await ctx.send(embed=reply_embed)

    @commands.command()
    async def l(self, ctx, extension):
        if ctx.author.id != CONFIG.OWNER_ID:
            reply_embed = replier.error(value='此指令僅限擁有者使用')
            await ctx.send(embed=reply_embed)
        else:
            await self.bot.load_extension(f'cogs.{extension}')
            logger.info(f'loaded {extension} done')
            reply_embed = replier.success(value=f'已載入 {extension}')
            await ctx.send(embed=reply_embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExtControl(bot), guild=bot.get_guild(CONFIG.GUILD_ID))
