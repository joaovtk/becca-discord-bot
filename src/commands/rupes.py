""" Base pycord module to create cogs """
from discord.ext import commands
from dotenv import dotenv_values
from src.__main__ import Bot

env = dotenv_values(".env")


class Rupes(commands.Cog):
    """ Rupes Cogs class """
    def __init__(self, bot: Bot):
        self.bot = bot
        self.url = env["APIURL"]
        self.secret = env["SECRET"]


    @commands.command(name="daily")
    async def add_post(self, ctx: commands.Context):     
        """ Listen post command """
        
        


def setup(bot: Bot):
    """ Needed Setup cogs """
    bot.add_cog(Rupes(bot))
