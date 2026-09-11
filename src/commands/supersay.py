from discord.ext import commands
from src.__main__ import Bot
from discord import Webhook
import discord


class SuperSay(commands.Cog):
    def __init__(self, bot: Bot):
         self.bot = bot
    @commands.slash_command(name="supersay", description="Super Command Say")
    async def cmd_ssay(self, ctx: discord.ApplicationContext, msg: str, user: discord.User = None, custom_name: str = None, custom_avatar: str = None):
        superbot = {}
        if custom_name and custom_avatar:
            superbot = {"name": custom_name, "avatar": custom_avatar}
        elif user:
            superbot = {"name": user.name, "avatar": user.display_avatar.url}
        if not superbot:
             await ctx.respond("O arrombado precisa selecionar uma pessoa", ephemeral=True)
        else:
            webhook = await ctx.channel.create_webhook(name="Becca Web")
            await ctx.respond(ephemeral=True, content="Enviado")
            await webhook.send(content=f"{msg}", username=superbot["name"], avatar_url=superbot["avatar"], )

def setup(bot: Bot):
    bot.add_cog(SuperSay(bot))
