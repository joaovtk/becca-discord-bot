import asyncio
from code import interact
from socket import timeout
from sqlite3.dbapi2 import Time

import discord
from src.__main__ import Bot
import requests
import json
import sqlite3
from discord.ext import commands
import time
import random

class NormalView(discord.ui.View):
    def __init__(self, DB_PATH, responseTermo):
        super().__init__()
        self.DB_PATH = DB_PATH
        self.responseTermo = responseTermo
    async def on_timeout(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)
    @discord.ui.button(label="Diário", style=discord.ButtonStyle.primary)
    async def btn_daily(self, button: discord.Button, interaction: discord.Interaction):

        id = random.randint(0, 1000)
        msg = await interaction.channel.send(f"{interaction.user}\n\n Começando Partida de Diário\n\nEi psiu ficou sem a caixa de dialogo ? clica no emoji que ele volta")
        channel = interaction.channel # define this!
        def msg_check(message):
            return message.channel == channel.id and message.content.lower() == str(id)

        thead = await channel.create_thread(name=f"wordle {interaction.user.name}", type=discord.ChannelType.private_thread)
        await thead.add_user(interaction.user)
        await thead.send(f"Partida Diario começando em 15 segundos\nCaso Queira adicionar pessoas, elas devem digitar esse codigo {id}")

        try :
            message = await interaction.client.wait_for("message", check=msg_check, timeout=15)
            if message.content.lower() == str(id):
                await thead.add_user(message.author)
        except Exception as err:
            if isinstance(err, asyncio.TimeoutError):
                await interaction.reply("Partida Começando")
        #    message = await interaction.client.wait_for(event="message", check=check)
        #if message.content == self.responseTermo:
        #    await interaction.message.channel.send(f"Parabéns {interaction.user} acertou a palavra era **{self.responseTermo}**,", view=self)
            #else:
            #await interaction.message.channel.send(f"", view=self)
    @discord.ui.button(label="Dueto", style=discord.ButtonStyle.primary, disabled=True)
    async def btn_duet(self, button: discord.Button, interaction: discord.Interaction):
        pass
    @discord.ui.button(label="Quarteto", style=discord.ButtonStyle.primary, disabled=True)
    async def btn_quartet(self, button: discord.Button, interaction: discord.Interaction):
        pass
    @discord.ui.button(label="Octeto", style=discord.ButtonStyle.primary, disabled=True)
    async def btn_octet(self, button: discord.Button, interaction: discord.Interaction):
            pass
    @discord.ui.button(label="Voltar", style=discord.ButtonStyle.secondary)
    async def btn_back(self, button: discord.Button, interaction: discord.Interaction):
        from src.view.Wordle.WorldeView import WordleView
        await interaction.edit(view=WordleView())
async def attempt(word, interaction, responseTermo) -> int:
    await interaction.response.defer()
    #def
    #requests.get("https://api.dicionario-aberto.net/word")
    content = requests.get(f"https://api.dicionario-aberto.net/word/{word}")
    response = json.dumps(content.json())
    if word in ["becca por favor para", "para agora becca", "para becca não quero jogar mais", "eu já cansei"]   :
        return 0
    elif len(word) != 5 or response == "[]":
        return 1
    else:
        green = []
        vermelho = []
        amarelo = []
        i = 0
        print(responseTermo)
        for x in word.lower():
            print(x)
            if responseTermo[i] == x:
                green.append({"pos": i})
                print("verde")
            elif responseTermo[i].find(x):
                amarelo.append({"pos": i})
                print("amarelo")
            else:
                vermelho.append({"pos": i})
                print("vermelho")
            i+=1
        text = []
        for t in range(5):
            text.append("")
        for g in green:
            print(g)
            text[g["pos"]] = "🟩"

        for r in vermelho:
            print(r)
            text[r["pos"]] = "🟥"

        for a in amarelo:
            print(a)
            text[a["pos"]] = "🟨"

        text = str(text).replace("'", "")
        text = str(text).replace(",", "")
        text = str(text).replace("[", "")
        text = str(text).replace("]", "")
        msg = await interaction.channel.send(content=f"{interaction.user}\n\n||{text}||")
        await msg.add_reaction("😇")
        def check(reaction, user):
            return str(reaction.emoji) == "😇" and user == interaction.user and reaction.message.id == msg.id
        print(check)
        try:
            reaction, user = await interaction.client.wait_for(event="reaction_add", check=check, timeout=10.0)
            if reaction:
                await msg.edit("Round i + 1\n**Em 5 segundos**")
                return 3
            if word.lower() == responseTermo:
                return 2
        except asyncio.TimeoutError:
            print('Acabou')
