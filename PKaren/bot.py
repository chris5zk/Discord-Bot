import discord
import config
import logging
import asyncio
import os

from discord.ext import commands

# Initialize bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.invites = True
bot = commands.Bot(intents=intents, command_prefix=';;')


@bot.event
async def on_ready():
    log_msg = f"{bot.user.name} has connected to Discord!"
    logging.getLogger('discord').info(log_msg)


async def init():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    asyncio.run(init())
    bot.run(config.DISCORD_API_SECRET, root_logger=True)
