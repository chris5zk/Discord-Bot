import json
import discord
import logging
from discord.ext import commands
from tools.extension import CogExtension

with open('data.json', 'r', encoding='utf8') as file:
    data = json.load(file)


class Response(CogExtension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
        if msg.content in data['key_word_1']:
            await msg.channel.send(file=discord.File(data['pic_1']))

    @commands.command()
    async def hello(self, ctx):
        logging.getLogger('discord').info(f"【{ctx.guild}】{str(ctx.author)} is using commands【>hello】")
        await ctx.send("Hello!")


async def setup(bot):
    await bot.add_cog(Response(bot))
