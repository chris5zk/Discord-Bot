import discord
from discord.ext import commands
from tools.extension import CogExtension
from tools.log import log_message
from tools.data import get_json

data = get_json()


class Response(CogExtension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
        if msg.content in data['key_word_1']:
            await msg.channel.send(file=discord.File(data['pic_1']))

    @commands.command()
    async def hello(self, ctx):
        log_msg = f'{ctx.author} is using commands【>hello】'
        await log_message(self.backend, log_msg, guild=ctx.guild, channel=ctx.channel, command=True)
        await ctx.send("Hello!")


async def setup(bot):
    await bot.add_cog(Response(bot))
