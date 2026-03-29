import os

import discord
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=";",
            intents=discord.Intents.all(),
            guild_ids=[1019641971989549149],
        )

    async def on_connect(self):
        for file in os.listdir("src/commands/"):
            if file.endswith(".py"):
                self.load_extension(f"src.commands.{file.replace('.py', '')}")

        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=f"Ouvindo atualmente {len(self.guilds)} fãs da becca",
                url="https://github.com/joaovtk/becca-discord-bot",
            )
        )
    #async def on_member_ban(self, user):
    #    if user.id in ["768614963002474506", "608309054485430294"]:
    #        await user.guild.unban(user)
    #        try:
    #            await user.guild.fetch_channels().send("But it refused")
    #        except Exception as err:
    #            print(err)


    def run(self, token):
        super().run(token=token)
