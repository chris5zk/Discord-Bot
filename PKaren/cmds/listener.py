from discord.ext import commands
from tools.extension import CogExtension
from tools.log import log_message


class Listener(CogExtension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel != self.backend and msg.channel != self.welcome:
            if not msg.content.startswith(self.bot.command_prefix):
                urls = [x.url for x in msg.attachments]
                log_msg = f"{msg.author}: {msg.content} {urls if urls else ''}"
                await log_message(self.backend, log_msg, guild=msg.guild, channel=msg.channel)

    @commands.Cog.listener()
    async def on_message_edit(self, msg_bf, msg_af):
        if msg_bf.channel != self.backend:
            log_msg = f"{msg_bf.author} edit content: {msg_bf.content} -> {msg_af.content}"
            await log_message(self.backend, log_msg, guild=msg_bf.guild, channel=msg_bf.channel)

    # @commands.Cog.listener()
    # async def on_message_delete(self,):

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_msg = f"{member} join the server."
        await self.welcome.send(f"Welcome {member.mention}!!")
        await log_message(self.backend, log_msg, guild=member.guild)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_msg = f"{member} leave the server."
        await self.welcome.send(f"{member} leave!!")
        await log_message(self.backend, log_msg, guild=member.guild)

    @commands.Cog.listener()
    async def on_guild_update(self, guild_old, guild_new):
        log_msg = f"【{guild_old}】guild name change to 【{guild_new}】"
        await log_message(self.backend, log_msg, guild=guild_old)


async def setup(bot):
    await bot.add_cog(Listener(bot))
