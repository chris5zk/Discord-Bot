import discord
import config
import logging
import asyncio
import os

from tools.message import emoji
from discord.ext import commands

# Initialize bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
bot = commands.Bot(intents=intents, command_prefix='>')


@bot.event
async def on_ready():
    log_msg = f"{emoji(bot.user.name)} has connected to Discord!"
    logging.getLogger('discord').info(log_msg)


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    logging.getLogger('discord').info(f"【{extension}】 is loaded by {ctx.author}")
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded 【{extension}】 done!')


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    logging.getLogger('discord').info(f"【{extension}】 is unloaded by {ctx.author}")
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded 【{extension}】 done!')


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    logging.getLogger('discord').info(f"【{extension}】 is reload by {ctx.author}")
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded 【{extension}】 done!')


async def init():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    asyncio.run(init())
    bot.run(config.DISCORD_API_SECRET, root_logger=True)
