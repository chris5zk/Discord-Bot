import discord
import logging
from discord.ext import commands
from core.extension import CogExtension


class Member(CogExtension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        logging.getLogger('discord').info(f"{member} join the server.")
        channel = self.bot.get_channel(1070258519351234610)
        await channel.send(f"{member} join!!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logging.getLogger('discord').info(f"{member} leave the server.")
        channel = self.bot.get_channel(1070258519351234610)
        await channel.send(f"{member} leave!!")


async def setup(bot):
    await bot.add_cog(Member(bot))
