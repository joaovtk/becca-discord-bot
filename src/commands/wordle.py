from src.__main__ import Bot
from discord.ext import commands
class Wordle(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

def setup(bot: Bot):
    bot.add_cog(Wordle(bot))

