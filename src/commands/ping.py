from datetime import datetime

import discord
from discord.ext import commands

from src.__main__ import Bot


class Ping(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name="ping", description="says pong")
    async def cmd_ping(self, ctx: commands.Context):
        ms = round(ctx.bot.latency * 1000)
        msg = await ctx.reply(f"Analisando...")
        await msg.edit(content=f"PONG...🏓 {ms}ms de api")

    @commands.slash_command(name="ping", description="Says Pong and meter api latency")
    async def sl_ping(self, ctx: discord.ApplicationContext):
        ms = round(ctx.bot.latency * 1000)
        await ctx.respond("Analisando...")

        await ctx.edit(content=f"PONG...🏓 {ms}ms de api")


def setup(bot: Bot):
    bot.add_cog(Ping(bot))
