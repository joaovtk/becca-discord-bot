from datetime import datetime

import discord
from discord.ext import commands
from db import AchievementsCount

from src.__main__ import Bot
import requests
from dotenv import dotenv_values
import json

env = dotenv_values(".env")


class Ping(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.count = AchievementsCount()
        self.url = env["APIURL"]
        self.secret = env["SECRET"]

    @commands.command(name="ping", description="says pong")
    async def cmd_ping(self, ctx: commands.Context):
        self.count = AchievementsCount()
        try:
            self.count.incCount("ping", ctx.author.id)
            
            ms = round(ctx.bot.latency * 1000)
            msg = await ctx.reply(f"Analisando...")
            await msg.edit(content=f"PONG...🏓 {ms}ms de api")
            session = requests.Session()
            identifier = f"1120262503"
            desc = "Using ping command for first time"
            payloadAdd = {"identifier": identifier, "identifierCommand": "ping", "desc": "Try use ping for first time", "secret": self.secret}
            payloadGain = {"userId": ctx.author.id, "identifier": identifier, "secret": self.secret, "cookies": 1   , "rupes": 200.0}
    
            

            requests.post(self.url+ f"/achievements/add", json=payloadAdd)
            responseOne =  requests.post(f"{self.url}/achievements/gain", json=payloadGain)
            z = 1
            print(responseOne.status_code)
            if responseOne.status_code == 200:
                await msg.channel.send(f"O {ctx.author} consegui uma conquista do comando **ping**: \n ||{desc}||")
            print(responseOne.status_code, responseOne.json())
        except Exception as err:
            print(err)
            await ctx.reply("Houve um erro na execução")
        finally:
            self.count.cur.close()
    @commands.slash_command(name="ping", description="Says Pong and meter api latency")
    async def sl_ping(self, ctx: discord.ApplicationContext):
        ms = round(ctx.bot.latency * 1000)
        await ctx.respond("Analisando...")

        await ctx.edit(content=f"PONG...🏓 {ms}ms de api")


def setup(bot: Bot):
    bot.add_cog(Ping(bot))
