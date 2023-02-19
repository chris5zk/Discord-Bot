from discord.ext import commands
from tools.extension import CogExtension
from tools.log import log_message


class Loader(CogExtension):
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        log_msg = f"【{extension}】 is loaded by {ctx.author}"
        await self.bot.load_extension(f'cmds.{extension}')
        await log_message(self.backend, log_msg, guild=ctx.guild, channel=ctx.channel, command=True)
        await ctx.send(log_msg)

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        log_msg = f"【{extension}】 is unloaded by {ctx.author}"
        await self.bot.unload_extension(f'cmds.{extension}')
        await log_message(self.backend, log_msg, guild=ctx.guild, channel=ctx.channel, command=True)
        await ctx.send(log_msg)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        log_msg = f"【{extension}】 is reloaded by {ctx.author}"
        await self.bot.reload_extension(f'cmds.{extension}')
        await log_message(self.backend, log_msg, guild=ctx.guild, channel=ctx.channel, command=True)
        await ctx.send(log_msg)


async def setup(bot):
    await bot.add_cog(Loader(bot))
