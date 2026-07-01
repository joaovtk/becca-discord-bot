import os

import discord
from discord.ext import commands
from dotenv import dotenv_values

class Bot(commands.Bot):
    """ Main Class """
    def __init__(self):
        self.env = dotenv_values(".env")
        if self.env["STATUS"] == "D":
            prefix = "<>"
        else:
            prefix = ";"
        super().__init__(
            command_prefix=prefix,
            intents=discord.Intents.all(),
            guild_ids=[1019641971989549149],
        )

    async def on_connect(self):

        for file in os.listdir("src/commands/"):
            if file.endswith(".py"):
                self.load_extension(f"src.commands.{file.replace('.py', '')}")

        if self.env["STATUS"] == "D":
            msg = "Ouvindo a becca no teste"
        else:
            msg = f"Ouvindo atualmente {len(self.guilds)} fãs da becca"
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=msg,
                url="https://github.com/joaovtk/becca-discord-bot",
            )
        )