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
bot = commands.Bot(intents=intents, command_prefix='>')


@bot.event
async def on_ready():
    logging.getLogger('discord').info(f"{bot.user.name.encode('unicode-escape', 'ignore').decode('unicode-escape')} has connected to Discord!")


@bot.command()
async def load(ctx, extension):
    logging.getLogger('discord').info(f"【{extension}】 is loaded by {ctx.author}")
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded 【{extension}】 done!')


@bot.command()
async def unload(ctx, extension):
    logging.getLogger('discord').info(f"【{extension}】 is unloaded by {ctx.author}")
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded 【{extension}】 done!')


@bot.command()
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
