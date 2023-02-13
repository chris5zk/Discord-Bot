import discord
import config
from discord.ext import commands


class CogExtension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.backend = None
        self.welcome = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.backend = self.bot.get_channel(int(config.BACKEND_CHANNEL))
        self.welcome = self.bot.get_channel(int(config.WELCOME_CHANNEL))