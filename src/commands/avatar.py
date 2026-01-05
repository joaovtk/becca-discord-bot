from datetime import datetime

import discord
from discord.ext import commands

from src.__main__ import Bot

class Avatar(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        
    @commands.command(name="avatar", description="Avatar command")
    async def cmd_avatar(self, ctx: commands.Context, user: discord.User = None):
        if user:
            target = user
            
        else:
            target = ctx.author
            
        
        embed = discord.Embed(title="Seu receptáculo", description="Esse será seu receptáculo...", color=0x00ff00)
        
        embed.set_image(url=target.display_avatar.url)
        await ctx.reply(embed=embed)
def setup(bot: Bot):
    bot.add_cog(Avatar(bot))