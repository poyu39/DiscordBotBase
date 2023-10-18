import logging
import os
from datetime import datetime
from logging import handlers

import discord
import pytz
import yaml

WORKDIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    def __init__(self):
        with open(
            WORKDIR + '/storage/config.yml', 'r', encoding='utf-8'
        ) as stream:
            self.config = yaml.load(stream, Loader=yaml.FullLoader)

        # bot timezone
        self.timezone_TW = pytz.timezone('ROC')

        # bot settings
        self.COMMDAND_PREFIX = self.config['command_prefix']
        self.TOKEN = self.config['token']
        self.GUILD_ID = self.config['guild_id']
        self.APPLICATION_ID = self.config['application_id']
        self.ACTIVITY = self.config['activity']
        self.OWNER_ID = self.config['owner_id']

        # reply embed
        self.REPLIER = self.config['replier']


class BotLogger:
    def __init__(self):
        log_dir = f'{WORKDIR}/storage/logs/'
        log_name = datetime.now().strftime('%d_%m_%Y.log')
        self.logger = logging.getLogger('discord')
        self.logger.setLevel(logging.INFO)
        logging.getLogger('discord.http').setLevel(logging.INFO)

        handler = handlers.RotatingFileHandler(
            filename=f'{log_dir}/{log_name}',
            encoding='utf-8',
            maxBytes=32 * 1024 * 1024,  # 32 MiB
            backupCount=5,  # Rotate through 5 files
        )
        dt_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter(
            '[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger


class Replier:
    def info(self, name='', value='', inline=False):
        info_embed = discord.Embed(color=CONFIG.REPLIER['info']['color'])
        info_embed.add_field(name=name, value=value, inline=inline)
        return info_embed

    def debug(self, name='', value='', inline=False):
        debug_embed = discord.Embed(color=CONFIG.REPLIER['debug']['color'])
        debug_embed.add_field(name=name, value=value, inline=inline)
        return debug_embed

    def success(self, name='', value='', inline=False):
        sucess_embed = discord.Embed(color=CONFIG.REPLIER['success']['color'])
        sucess_embed.add_field(name=name, value=value, inline=inline)
        return sucess_embed

    def error(self, name='', value='', inline=False):
        error_embed = discord.Embed(color=CONFIG.REPLIER['error']['color'])
        error_embed.add_field(name=name, value=value, inline=inline)
        return error_embed

    def warning(self, name='', value='', inline=False):
        warning_embed = discord.Embed(color=CONFIG.REPLIER['warning']['color'])
        warning_embed.add_field(name=name, value=value, inline=inline)
        return warning_embed


CONFIG = Config()
logger = BotLogger().get_logger()
replier = Replier()
