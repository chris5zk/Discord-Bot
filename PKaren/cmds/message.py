import discord
import logging
from discord.ext import commands
from core.extension import CogExtension


class Message(CogExtension):
    @commands.command()
    async def hello(self, ctx):
        logging.getLogger('discord').info(f"{str(ctx.author)} said hello!")
        await ctx.send("Hello!")


async def setup(bot):
    await bot.add_cog(Message(bot))
