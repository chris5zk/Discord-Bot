import discord
from discord import ui
from discord import app_commands
from tools.extension import CogExtension
from tools.log import log_message
from datetime import datetime


class Send(CogExtension):
    @app_commands.command(name="announce", description="select testing")
    async def announce(self, interaction: discord.Interaction):
        log_msg = f'{interaction.user} send an announcement.'
        await interaction.response.send_message(view=EmbedView(self.announce))
        await log_message(self.backend, log_msg, guild=interaction.guild, command=True)


class AnnounceModal(ui.Modal):
    def __init__(self, num, channel):
        super().__init__(title="Announcement")
        self.fields = []
        self.channel = channel
        self.init_input()
        self.add_field(num)
        self.add_to_item()

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Announcement", description=self.fields[0], timestamp=datetime.now())
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar.url)
        for i in range(1, len(self.fields), 2):
            embed.add_field(name=self.fields[i], value=self.fields[i+1], inline=False)
        embed.set_footer(text="Timestamp")
        await self.channel.send(embed=embed)
        await interaction.response.send_message("Announce sent!")

    def init_input(self):
        self.fields.append(ui.TextInput(label='Description', style=discord.TextStyle.paragraph))

    def add_field(self, num):
        for i in range(num):
            self.fields.append(ui.TextInput(label=f'Field {i+1}', style=discord.TextStyle.short))
            self.fields.append(ui.TextInput(label='content', style=discord.TextStyle.paragraph))

    def add_to_item(self):
        for field in self.fields:
            self.add_item(field)


class EmbedSelect(ui.Select):
    def __init__(self, channel):
        self.channel = channel
        options = [discord.SelectOption(label="Only description", emoji="0️⃣", value="0"),
                   discord.SelectOption(label="Add one field to embed", emoji="1️⃣", value="1"),
                   discord.SelectOption(label="Add two fields to embed", emoji="2️⃣", value="2")]
        super().__init__(placeholder="Choose the numbers of fields in embed message.", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(AnnounceModal(int(self.values[0]), self.channel))


class EmbedView(ui.View):
    def __init__(self, channel):
        super().__init__()
        self.add_item(EmbedSelect(channel))


async def setup(bot):
    await bot.add_cog(Send(bot))
