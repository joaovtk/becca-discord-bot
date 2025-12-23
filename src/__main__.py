import os

import discord
from discord.ext import commands

from src.logging import logger


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=";",
            intents=discord.Intents.all(),
            guild_ids=[1019641971989549149],
        )

    async def on_ready(self):
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
        await self.sync_commands()

    def run(self, token):
        super().run(token=token)
