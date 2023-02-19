import discord
from discord.ext import commands
from tools.extension import CogExtension
from tools.log import log_message


class Backend(CogExtension):
    @commands.command()
    async def log(self, ctx, date):
        if ctx.message.author.guild_permissions.administrator:
            log_msg = f'{ctx.author} is using commands【>log】'
            await log_message(self.backend, log_msg, guild=ctx.guild, channel=ctx.channel, command=True)
            try:
                await ctx.send(f'Log file of {date}', file=discord.File(f'.\\logs\\logfile_{date}.log'))
            except FileNotFoundError:
                await ctx.send(f'Log file not found!!!')
        else:
            log_msg = f'{ctx.author} has no permissions for using command【>log】'
            await log_message(self.backend, log_msg, guild=ctx.guild, channel=ctx.channel, command=0)
            await ctx.send(f'{ctx.author.mention}, You have no permission!!!')

    # @commands.command()
    # async def audit(self, ctx):
    #     if ctx.message.author.guild_permissions.administrator:
    #         async for entry in ctx.guild.audit_logs(limit=1):
    #             await ctx.send(f'**{entry.user.name}#{entry.user.discriminator}** do【{str(entry.action).split("AuditLogAction.")[1]}】')


async def setup(bot):
    await bot.add_cog(Backend(bot))
