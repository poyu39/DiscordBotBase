import discord
from discord.ext import commands

from settings import Config, logger, replier

CONFIG = Config()


class ExtControl(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info('>>已載入 ExtControl<<')

    @commands.command()
    async def un(self, ctx, extension):
        if ctx.author.id != CONFIG.OWNER_ID:
            reply_embed = replier.error(value='此指令僅限擁有者使用')
            await ctx.send(embed=reply_embed)
        else:
            try:
                await self.bot.unload_extension(f'cogs.{extension}')
                logger.info(f'已卸載 {extension}')
                reply_embed = replier.success(value=f'已卸載 {extension}')
            except Exception as e:
                logger.error(f'{extension} 未載入', exc_info=e)
                reply_embed = replier.error(value=f'{extension} 未載入\n{e}')
            await ctx.send(embed=reply_embed)

    @commands.command()
    async def re(self, ctx, extension):
        if ctx.author.id != CONFIG.OWNER_ID:
            reply_embed = replier.error(value='此指令僅限擁有者使用')
            await ctx.send(embed=reply_embed)
        else:
            try:
                await self.bot.reload_extension(f'cogs.{extension}')
                await self.bot.tree.sync(
                    guild=discord.Object(id=CONFIG.GUILD_ID)
                )
                logger.info(f'已重新載入 {extension}')
                reply_embed = replier.success(value=f'已重新載入 {extension}')
            except Exception as e:
                logger.error(f'{extension} 未載入', exc_info=e)
                reply_embed = replier.error(value=f'{extension} 未載入\n{e}')
            await ctx.send(embed=reply_embed)

    @commands.command()
    async def l(self, ctx, extension):
        if ctx.author.id != CONFIG.OWNER_ID:
            reply_embed = replier.error(value='此指令僅限擁有者使用')
            await ctx.send(embed=reply_embed)
        else:
            try:
                await self.bot.load_extension(f'cogs.{extension}')
                logger.info(f'已載入 {extension}')
                reply_embed = replier.success(value=f'已載入 {extension}')
            except Exception as e:
                logger.error(f'{extension} 未載入', exc_info=e)
                reply_embed = replier.error(value=f'{extension} 未載入\n{e}')
            await ctx.send(embed=reply_embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ExtControl(bot), guild=bot.get_guild(CONFIG.GUILD_ID))
