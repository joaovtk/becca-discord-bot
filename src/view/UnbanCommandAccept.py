import discord
import requests

from dotenv import dotenv_values

env = dotenv_values(".env")
class UnbanCommandAccept(discord.ui.View):
    def __init__(self, user: discord.User):
        super().__init__(timeout=45)
        self.user = user
        self.unbanned = False
        self.cancel = False
    async def on_timeout(self):
        if not self.unbanned and not self.cancel:
            embed = discord.Embed(title="Comando cancelado por tempo :<", description="Não consegui decidir. Eu poderia decidir por você, porém ainda sou uma chatbot, então, __***por favor, faça, apenas faça***__. E, para você, não tem conquista, nem rupes a mais, apenas dor e sofrimento. :) ", color=0x0000ff)
            embed.set_author(name="goiabatk", url="https://github.com/joaovtk/beccca-discord-bot", icon_url=self.user.display_avatar.url)
            embed.set_footer(text=f"goiabatk/beccatk\nA Becca gostou das suas escolhas de vida", icon_url="https://cdn.discordapp.com/avatars/608309054485430294/e6d35770ddabd3b2c64cf5eb72fd983b.png?size=1024")
            for item in self.children:
                print(item)
                item.disabled = True
                await self.message.edit(view=self, embed=embed)

    @discord.ui.button(style=discord.ButtonStyle.primary, label="Ser Extremamente Burro", emoji="<:becca_is_cursed:1488223094014218361>")
    async def unban_cmd_accept(self, button, interaction: discord.Interaction):
        embed = discord.Embed(title="Affs, o usuário voltou pra cá", description="Ele teve seu perdão, agora arque com suas consequências... E, aliás, não é esse que tem conquista, procura aí.", color=0x00ff00)
        embed.set_author(name="goiabatk", url="https://github.com/joaovtk/beccca-discord-bot", icon_url=interaction.client.user.display_avatar.url)
        embed.set_footer(text=f"goiabatk/beccatk\n A Becca está depressiva.", icon_url="https://cdn.discordapp.com/avatars/608309054485430294/e6d35770ddabd3b2c64cf5eb72fd983b.png?size=1024")
        await interaction.guild.unban(self.user)
        for item in self.children:
            if isinstance(item, discord.ui.Button):
                item.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)
        self.unbanned = True
        try:
            invite = await interaction.channel.create_invite(max_age=300000, max_uses=1, unique=True)
            await self.user.send(invite.url)
        except Exception as err:
            print(err)
        
    @discord.ui.button(label="Ser Sábio", style=discord.ButtonStyle.grey, emoji="<:becca_is_death_funny:1481782802113499397>")
    async def unban_cmd_cancel(self, button, interaction: discord.Interaction):
        embed = discord.Embed(title="EBA, digo você não quer realmente perdoar ele né", description=f"***Fica aí banido por mais tempo,*** {self.user.global_name}; você não merece estar aqui. Se puder usar esse comandinho secreto chamado perm ban, por favor.", color=0x00ff00)
        embed.set_author(name="goiabatk", url="https://github.com/joaovtk/beccca-discord-bot", icon_url=interaction.client.user.display_avatar.url)
        embed.set_footer(text=f"goiabatk/beccatk\n A Becca está orgulhosa de você.", icon_url="https://cdn.discordapp.com/avatars/608309054485430294/e6d35770ddabd3b2c64cf5eb72fd983b.png?size=1024")
        
        for item in self.children:
            if isinstance(item, discord.ui.Button):
                item.disabled = True
        self.cancel = True
        await interaction.response.edit_message(embed=embed, view=self)
        secret = env["SECRET"]
        url = env["APIURL"]
        identifier = "unbbancmdbtncancel2"
        payloadAdd = {"identifier": identifier, "identifierCommand": "unban", "desc": "Tema: Seguir o conselho da becca e não desbanir alguem: \nAperte o botão de cancelar pela primeira vez e seja parabenizado pela becca\nComando/Categoria: unban/moderação", "secret": secret}
        payloadGain = {"userId": interaction.user.id, "identifier": identifier, "secret": secret, "cookies": 10, "rupes": 10000.0}
        requests.post(url + "/achievements/add", json=payloadAdd)
        responseGain = requests.post(url + "/achievements/gain", json=payloadGain)
        if responseGain.status_code == 200:
            with open("assets/sound.mp3", "rb") as f:
                file = discord.File(f)
                await interaction.channel.send(content=f"*PLIM* Conquista desbloqueada\n\n**\n\nVocê finalmente achou a conquista parabéns{payloadAdd['desc']}**", file=file)