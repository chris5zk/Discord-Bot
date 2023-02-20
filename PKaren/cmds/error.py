from discord.ext import commands
from tools.extension import CogExtension
from cmds.backend import Backend
from cmds.loader import Loader


class Error(CogExtension):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error_command = f"{ctx.command}_error"
        if hasattr(ErrorHandler, error_command):
            exception = getattr(ErrorHandler, error_command)
            await exception(self, ctx, error)
            return
        else:
            await ErrorHandler.default_error(self, ctx, error)


async def setup(bot):
    await bot.add_cog(Error(bot))


class ErrorHandler:
    async def default_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command Not Found...")

    @Backend.log.error
    async def log_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing the argument <date>\n> format: YYYY-MM-DD\n> example. ;;log 2023-02-13")

    @Loader.load.error
    async def load_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send(f"{ctx.author.mention}, you don't have permission for using 【{ctx.command}】")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"【{ctx.command}】 is invoked! Please check the parameters again!")

    @Loader.reload.error
    async def reload_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send(f"{ctx.author.mention}, you don't have permission for using 【{ctx.command}】")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"【{ctx.command}】 is invoked! Please check the parameters again!")

    @Loader.unload.error
    async def unload_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send(f"{ctx.author.mention}, you don't have permission for using 【{ctx.command}】")
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"【{ctx.command}】 is invoked! Please check the parameters again!")
