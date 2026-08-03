import discord
from src.__main__ import Bot
import requests
import json
import sqlite3
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
         #def
        #requests.get("https://api.dicionario-aberto.net/word")
        await interaction.response.send_message("Começando Partida de Diário")
        def check(message: discord.Message):
            return message.author.id == interaction.user.id and not message.author.bot
        message = await interaction.client.wait_for(event="message", check=check)
        i = 0
        while i < 5:
            content = requests.get(f"https://api.dicionario-aberto.net/word/{message.content}")
            response = json.dumps(content.json())
            if message.content.lower() in ["becca por favor para", "para agora becca", "para becca não quero jogar mais", "eu já cansei"]   :
                await message.reply("Jogo Cancelado")
                for item in self.children:
                    item.disabled = True
                await self.message.edit(view=self)
            elif len(message.content) != 5 or response == "[]":
                await message.reply("Palavra invalida, caso deseje cancelar digite **```Becca Por Favor Para```**\n\**Digite uma palavra valida uma que existe no vocabulario de preferencia né**")
            else:
                #await message.reply(message.content)
                # Yellow
                    green = []
                    vermelho = []
                    amarelo = []
                    i = 0
                    print(self.responseTermo)
                    for x in message.content.lower():
                        print(x)
                        if self.responseTermo[i] == x:
                            green.append({"pos": i})
                            print("verde")
                        elif self.responseTermo[i].find(x):
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
                    await message.reply(content=f"{message.content}\n\n||{text}||")
                    if message.content == self.responseTermo:
                        break

            message = await interaction.client.wait_for(event="message", check=check)
        if message.content == self.responseTermo:
            await interaction.message.channel.send(f"Parabéns {interaction.user} acertou a palavra era **{self.responseTermo}**,", view=self)
        else:
            await interaction.message.channel.send(f"", view=self)
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
