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
            payloadAdd = {"identifier": identifier, "identifierCommand": "ping", "desc": "Try use ping for first time"}
            payloadGain = {"userId": ctx.author.id, "identifier": identifier}
    
            

            requests.get(self.url+ f"/achievements/add", json=payloadAdd)
            responseOne =  requests.get(f"{self.url}/achievements/gain", json=payloadGain)
            z = 1
            print(responseOne.status_code)
            if responseOne.status_code == 200:
                await msg.channel.send(f"O {ctx.author} consegui uma conquista do comando **ping**: \n ||{desc}||")
            print(responseOne.status_code, responseOne.json())
            for i in range(10):
                if self.count.getCount("ping", ctx.author.id) > i * 25:
                    identifier = f"1{i + 1}20262503"
                    payloadAdd["identifier"] = identifier
                    desc = f"Using command ping for {(i + 1) * 25}"
                    payloadAdd["desc"] = desc
                    session = requests.Session()

                    responseTwo =  requests.get(f"{self.url}/achievements/gain", json=payloadGain)
                    session.get(self.url+ f"/achievements/add", json=payloadAdd)
                    print(responseTwo.status_code, responseTwo.json())
                    if responseTwo.status_code == 200:
                        await msg.channel.send(f"O {ctx.author} consegui uma conquista do comando **ping**: \n ||{desc}||")
                        break
                if responseTwo.status_code == 200:
                    await msg.channel.send(f"O {ctx.author} consegui uma conquista do comando **ping**: \n ||{desc}||")
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
