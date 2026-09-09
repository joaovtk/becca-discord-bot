import discord

class WordleView(discord.ui.View):
    def __init__(self, DB_PATH, responseTermo):
        super().__init__(timeout=60)
        self.DB_PATH = DB_PATH
        self.responseTermo = responseTermo
    async def on_timeout(self):
        for item in self.children:
           item.disabled = True

        await self.message.edit(view=self)
    @discord.ui.button(label="Modo Difícil", style=discord.ButtonStyle.secondary, disabled=True, emoji="🇩")
    async def button_hard(self, button: discord.Button, interaction: discord.Interaction):
        pass
    @discord.ui.button(label="Modo Normal", style=discord.ButtonStyle.secondary, emoji="🇹")
    async def button_normal(self, button: discord.Button, interaction : discord.Interaction):
        from src.view.Wordle.WordleNormal import NormalView
        await interaction.edit(view=NormalView(self.DB_PATH, self.responseTermo))
    @discord.ui.button(label="Modo Extra", style=discord.ButtonStyle.secondary, emoji="🇪")
    async def button_extra(self, button: discord.Button, interaction : discord.Interaction):
        pass
