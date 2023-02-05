import json
import discord
import logging
from func import emoji
from discord.ext import commands
from core.extension import CogExtension

with open('data.json', 'r', encoding='utf8') as file:
    data = json.load(file)


class Message(CogExtension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        urls = [x.url for x in msg.attachments]
        author = emoji(str(msg.author))
        content = emoji(str(msg.content))
        channel = emoji(str(msg.channel))
        logging.getLogger('discord').info(f"{author}: {content} {urls if urls else ''} ({channel})")
        if msg.author == self.bot.user:
            return
        if msg.content in data['key_word_1']:
            await msg.channel.send(file=discord.File(data['pic_1']))

    @commands.command()
    async def hello(self, ctx):
        logging.getLogger('discord').info(f"{str(ctx.author)} is using commands【>hello】")   # Y or N
        await ctx.send("Hello!")


async def setup(bot):
    await bot.add_cog(Message(bot))
