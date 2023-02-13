import discord
import logging
from discord.ext import commands
from tools.extension import CogExtension


class Backend(CogExtension):
    @commands.command()
    async def log(self, ctx, date):
        if ctx.message.author.guild_permissions.administrator:
            log_msg = f'【{ctx.guild}】{str(ctx.author)} is using commands【>log】'
            logging.getLogger('discord').info(log_msg)
            await ctx.send(f'Log file of {date}', file=discord.File(f'.\\logs\\{date}.log'))
        else:
            logging.getLogger('discord').info(f'【{ctx.guild}】{str(ctx.author)} has no permissions for using command【>log】')
            await ctx.send(f'{ctx.message.author.mention}, you have no permission for doing this.')

    # @commands.command()
    # async def audit(self, ctx):
    #     if ctx.message.author.guild_permissions.administrator:
    #         async for entry in ctx.guild.audit_logs(limit=1):
    #             await ctx.send(f'**{entry.user.name}#{entry.user.discriminator}** do【{str(entry.action).split("AuditLogAction.")[1]}】')


async def setup(bot):
    await bot.add_cog(Backend(bot))
