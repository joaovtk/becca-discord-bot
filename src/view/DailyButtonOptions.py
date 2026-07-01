import discord
import requests
from dotenv import dotenv_values
env = dotenv_values(".env")

class BanCommandAccept(discord.ui.View):
    @discord.ui.button(label="=Daily em dobro TOP.gg", style=discord.ButtonStyle.secondary, disabled=True)
    async def button_callback(self, button, interaction: discord.Interaction):
        """Decorator to create button"""    
        pass
    
    @discord.ui.button(label="Daily Normal", style=discord.ButtonStyle.secondary, disabled=False)
    async def button_callback(self, button, interaction: discord.Interaction):
        secret = env["SECRET"]