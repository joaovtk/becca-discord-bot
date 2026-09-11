from src.__main__ import Bot
from discord.ext import commands
import discord
import datetime
from dotenv import dotenv_values
import requests
from json import dumps
from src.view.BanCommandAccept import BanCommandAccept
from src.view.UnbanCommandAccept import UnbanCommandAccept

env = dotenv_values(".env")

class Mod(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.url = env["APIURL"] 
        self.secret = env["SECRET"]

    @commands.command("ban")
    @commands.has_permissions(ban_members=True, administrator=True)
    async def cmd_ban(self, ctx: commands.Context, member: discord.User):
        identifier = "bancmd1"

        if member.id == ctx.author.id and ctx.guild.owner_id == ctx.author.id:
            payloadAdd = {"identifier": identifier, "identifierCommand": "ban", "desc": "Tema: A traição veio por você mesmo: \nAção: Use o comando ban contra a si mesmo\nComando/Categoria: ban/moderação", "secret": self.secret}
            payloadGain = {"userId": ctx.author.id, "identifier": identifier, "secret": self.secret, "cookies": 10, "rupes": 10000.0}
            responseAdd = requests.post(self.url + "/achievements/add", json=payloadAdd)
            responseGain = requests.post(self.url + "/achievements/gain", json=payloadGain)
            print(responseAdd.status_code, responseGain.status_code)
            print(responseAdd.text, responseGain.text)
        
            await ctx.reply("*Fez isso pela conquista né ?* Toma mais 10k de rupes de bonificação... **caso você não tenha** Pobre.")
            if responseGain.status_code == 200:
                with open("assets/sound.mp3", "rb") as f:
                    file = discord.File(f)
                    await ctx.send(content=f"*PLIM* Conquista desbloqueada\n\n**{payloadAdd['desc']}**", file=file)
        elif member.id == ctx.author.id:
            payloadAdd = {"identifier": identifier, "identifierCommand": "ban", "desc": "Tema: A traição veio por você mesmo: \nAção: Use o comando ban contra a si mesmo\nComando/Categoria: ban/moderação", "secret": self.secret}
            payloadGain = {"userId": ctx.author.id, "identifier": identifier, "secret": self.secret, "cookies": 10, "rupes": 5000.0}
            responseAdd = requests.post(self.url + "/achievements/add", json=payloadAdd)
            responseGain = requests.post(self.url + "/achievements/gain", json=payloadGain)
            print(responseAdd.status_code, responseGain.status_code)
            print(responseAdd.text, responseGain.text)
            await ctx.reply("*Hora da punição hihi*, brincadeira não da pra se banir só fiz isso uma vez e são **memórias  de guerra**...")
            if responseGain.status_code == 200:
                with open("assets/sound.mp3", "rb") as f:
                    file = discord.File(f)
                    await ctx.send(content=f"*PLIM* Conquista desbloqueada\n\n**{payloadAdd['desc']}**", file=file)
        elif member.id == ctx.guild.owner_id :  
            await ctx.reply(f"*Cara tá tá pedindo para ser banido no servidor né*, Vamos fazer um cenário hipotético o que aconteceria se você banisse a pessoa que mantem a ancora entre você e o servidor... **Acho que talvez o servidor não existiria né**\nEntão {member.mention} bane ele, só tem desculpa caso for pela conquista e alias ||**Plim! onomatopeia de conquista de jogos**||")
        else:
            embed = discord.Embed(title="Esperando você decidir...", description="Clique no botão __***punir severamente***__ para concluir a punição", color=0xFF8DA1)
            embed.set_author(name="goiabatk", url="https://github.com/joaovtk/beccca-discord-bot", icon_url=self.bot.user.display_avatar.url)
            embed.set_footer(text=f"goiabatk/beccatk", icon_url="https://cdn.discordapp.com/avatars/608309054485430294/e6d35770ddabd3b2c64cf5eb72fd983b.png?size=1024")
            await ctx.reply(embed=embed, view=BanCommandAccept(member))
    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True, administrator=True)
    async def cmd_unban(self, ctx: commands.Context, member: discord.User):

        if member.id == ctx.author.id and ctx.guild.owner_id == ctx.author.id:
            await ctx.reply("__**Hora de poupar**__ alguém, porém não posso, pois essa pessoa, além de ser você, é também o dono do grupo, né? Você não tem conquista dessa vez... e nem rupes a mais, seu burro...")
        elif member.id == ctx.author.id:
            await ctx.reply("__**Hora de olhar para si mesmo e ver se você merece perdão... **__ Na verdade, você só está me dando mais trabalho, porque tenho que validar isso tudo. Obrigado aos usuários, vocês são perfeitos... e também não têm conquista. Desde já, obrigado.")
            identifier = "unbbancmdbtnself2"
            payloadAdd = {"identifier": identifier, "identifierCommand": "unban", "desc": "Tema: Você tá me dando trabalho 1: \nTente se desbanir e gere mais trabalho para programador da becca\nComando/Categoria: unban/moderação", "secret": self.secret}
            payloadGain = {"userId": ctx.author.id, "identifier": identifier, "secret": self.secret, "cookies": 10, "rupes": 10000.0}
            requests.post(self.url + "/achievements/add", json=payloadAdd)
            responseGain = requests.post(self.url + "/achievements/gain", json=payloadGain)
            if responseGain.status_code == 200:
                with open("assets/sound.mp3", "rb") as f:
                    file = discord.File(f)
                    await ctx.channel.send(content=f"*PLIM* Conquista desbloqueada\n\nVocê finalmente achou a conquista parabéns\n\n{payloadAdd['desc']}", file=file)
        elif member.id == ctx.guild.owner_id :  
            await ctx.reply(f"__**O {member.mention} fez algo imperdoavel assim para você?**__ Porque eu acho que isso, eu sei que as pessoas não podem guardar rancor, só que, porém, não compensa me dar mais trabalho. Obrigado... Ah, e não tem conquista de novo, tô falando isso porque a conquista tá muito escondida.")

        else:
            banlist = ctx.guild.bans()
            have = False
            async for ban in banlist:
                print(ban.user.name, member.id)
                if ban.user.id == member.id:
                    have = True
                    break
            print(have) 
            if have:
                embed = discord.Embed(title="Hora da Piedade", description="Tente ser piedoso contra uma pesso que já fez muito mal, as vezes poupar é bom *exceto em jogo de tiro*", colour=0x0000f)
                embed.set_author(name="goiabatk", url="https://github.com/joaovtk/beccca-discord-bot", icon_url=member.display_avatar.url)
                embed.set_footer(text=f"goiabatk/beccatk\nA Becca não gosta dessa ideia.", icon_url="https://cdn.discordapp.com/avatars/608309054485430294/e6d35770ddabd3b2c64cf5eb72fd983b.png?size=1024")
                await ctx.reply(embed=embed, view=UnbanCommandAccept(member))
            
            else:
                await ctx.reply("__**Oxi, essa pessoa nem tá banida**__. Tente banir alguém, só que não use esse comando, por favor. Mas tem que ter motivo, né? Se não, vira ditadura.")                
    @cmd_ban.error
    @cmd_unban.error
    async def main_errors(self, ctx, error):
        print(error)
        if isinstance(error, commands.UserNotFound) or isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(title="Nossa deu um erro bizarro...", description="Parece que você não forneceu um __**usuário valido**__, da proxima vez você seu *bizarro* analise o comando", color=0xff0000)
            embed.set_author(name="goiabatk", url="https://github.com/joaovtk/beccca-discord-bot", icon_url=self.bot.user.display_avatar.url)
            embed.set_footer(text=f"goiabatk/beccatk", icon_url="https://cdn.discordapp.com/avatars/608309054485430294/e6d35770ddabd3b2c64cf5eb72fd983b.png?size=1024")
            await ctx.reply(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Nossa deu um erro bizarro...", description="Parece que você não tem permissoes o suficiente para isso tente contactar forças superiores para te ajudar", color=0xff0000)
            embed.set_author(name="goiabatk", url="https://github.com/joaovtk/beccca-discord-bot", icon_url=self.bot.user.display_avatar.url)
            embed.set_footer(text=f"goiabatk/beccatk", icon_url="https://cdn.discordapp.com/avatars/608309054485430294/e6d35770ddabd3b2c64cf5eb72fd983b.png?size=1024")
            await ctx.reply(embed=embed)

def setup(bot: Bot):
    bot.add_cog(Mod(bot))