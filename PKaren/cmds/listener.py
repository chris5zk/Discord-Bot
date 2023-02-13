import discord
import logging
import config
from tools.message import msg_process
from discord.ext import commands
from tools.extension import CogExtension
from tools.log import log_message


class Listener(CogExtension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel != self.backend and msg.channel != self.welcome:
            urls, author, content, channel, guild = msg_process(msg)
            logging.getLogger('discord').info(f"【{guild}】{author}: {content} {urls if urls else ''} ({channel})")
            await self.backend.send(await log_message(f"[{channel}] {author}: {content} {urls if urls else ''}"))

    @commands.Cog.listener()
    async def on_message_edit(self, msg_bf, msg_af):
        logging.getLogger('discord').info(f'【{msg_bf.guild}】{msg_bf.author} edit content: {msg_bf.content} -> {msg_af.content}')
        await self.backend.send(await log_message(f"[{msg_bf.channel}] {msg_bf.author} edit content: {msg_bf.content} -> {msg_af.content}"))

    # @commands.Cog.listener()
    # async def on_message_delete(self,):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        logging.getLogger('discord').info(f"【{member.guild.name}】{member} join the server.")
        await self.welcome.send(f"{member} join!!")
        await self.backend.send(await log_message(f"{member} join the server."))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logging.getLogger('discord').info(f"【{member.guild.name}】{member} leave the server.")
        await self.welcome.send(f"{member} leave!!")
        await self.backend.send(await log_message(f"{member} leave the server."))

    @commands.Cog.listener()
    async def on_guild_update(self, guild_old, guild_new):
        logging.getLogger('discord').info(f"【{guild_old}】guild name change to 【{guild_new}】")
        await self.backend.send(await log_message(f"【{guild_old}】guild name change to 【{guild_new}】"))


async def setup(bot):
    await bot.add_cog(Listener(bot))
