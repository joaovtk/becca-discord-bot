import discord
import requests
from dotenv import dotenv_values
env = dotenv_values(".env")

class BanCommandAccept(discord.ui.View):

    @discord.ui.button(label="Punir Severamente", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction: discord.Interaction):      
        embed = discord.Embed(title="Usuário Punido :)", description="Ele teve a devida punição agora ele não vai mais se atrever a ignorar seus avisos...", color=0x00ff00)
        embed.set_author(name="goiabatk", url="https://github.com/joaovtk/beccca-discord-bot", icon_url=interaction.client.user.display_avatar.url)
        embed.set_footer(text=f"goiabatk/beccatk", icon_url="https://cdn.discordapp.com/avatars/608309054485430294/e6d35770ddabd3b2c64cf5eb72fd983b.png?size=1024")
        button.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)

    
    @discord.ui.button(label="Ser Piedoso", style=discord.ButtonStyle.red)
    async def button_cancel_callback(self, button: discord.Button, interaction: discord.Interaction):
        secret = env["SECRET"]
        url = env["APIURL"]
        embed = discord.Embed(title="Usuário Poupado :)", description="O usuário se safou da **dura punição**, tente na proxima vez concluir o castigo...\nEu gosto de ver caos... a é mesmo toma uma conquista ai medroso", color=0xff0000)
        embed.set_author(name="goiabatk", url="https://github.com/joaovtk/beccca-discord-bot", icon_url=interaction.client.user.display_avatar.url)
        embed.set_footer(text=f"goiabatk/beccatk", icon_url="https://cdn.discordapp.com/avatars/608309054485430294/e6d35770ddabd3b2c64cf5eb72fd983b.png?size=1024")
        button.disabled = True
        for item in self.children:
            if isinstance(item, discord.ui.Button):
                item.disabled = True
        await interaction.response.edit_message(embed=embed, view=self) 
        identifier = "bancmdbtncancel2"
        payloadAdd = {"identifier": identifier, "identifierCommand": "ban", "desc": "Tema: Poupar as vezes é bom: \nAperte o botão de cancelar pela primeira vez e seja humilhado pela becca\nComando/Categoria: ban/moderação", "secret": secret}
        payloadGain = {"userId": interaction.user.id, "identifier": identifier, "secret": secret, "cookies": 10, "rupes": 5000.0}
        responseAdd = requests.post(url + "/achievements/add", json=payloadAdd)
        responseGain = requests.post(url + "/achievements/gain", json=payloadGain)
        print(responseAdd.status_code, responseGain.status_code)
        print(responseAdd.text, responseGain.text)

        if responseGain.status_code == 200:
            with open("assets/sound.mp3", "rb") as f:
                file = discord.File(f)
                await interaction.channel.send(content=f"*PLIM* Conquista desbloqueada\n\n**{payloadAdd['desc']}**", file=file)
