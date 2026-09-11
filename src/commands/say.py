from discord.ext import commands
from discord.commands import SlashCommandGroup
from src.__main__ import Bot
from gtts import gTTS
import os

import discord
class Say(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
    utilsGroup = SlashCommandGroup("utils", "Utils Command")
    
    @utilsGroup.command(name="audio",description="Make The Audio with your message")
    async def sl_say_audio(self, ctx: discord.ApplicationContext, * ,message: str, quiet: bool):
        await ctx.respond(ephemeral=True, content="👑 Sua Mensagem foi entregue faz bom uso de vossa consequencia...👑")
        gtts = gTTS(text=message, lang="pt")
        gtts.save("message.mp3") 
        file = discord.File("message.mp3")
        try:
            if quiet:
                await ctx.channel.send(file=file) 
            else:
                
                await ctx.channel.send(content="💬 Alguem das profudezas disse...💬", file=file) 
                
                os.remove("message.mp3") 
        except Exception as err:
            if not quiet:
                await ctx.channel.send("💀 Alguem das profudezas tentou se comunicar com você... e não teve exito. A mensagem é perdida para sempre... 💀")
                print(err)
            
    @utilsGroup.command(name="say", description="Say Anything In the chat")
    async def sl_base_say(self, ctx: discord.ApplicationContext, * , message: str, quiet: bool):
        try:
            await ctx.respond(ephemeral=True, content=f"📧 Sua Carta foi entregue, tome cuidado a contactar seres desse mundo vulgo membros do {ctx.guild.name} 📧")
            if quiet:
                await ctx.channel.send(content=f"{message}") 
            else:
                
                await ctx.channel.send(content=f"💬 Alguem das profudezas disse...💬\n\n **{message}**") 
        except Exception as err:
            if not quiet:
                await ctx.channel.send("☠️...A tentativa de comunicação falhou...☠️")
                print(err)
            

    @utilsGroup.command(name="echo", description="Echo Command")
    async def cmd_ssay(self, ctx: discord.ApplicationContext, msg: str, user: discord.User = None, name: str = None, avatar: discord.Attachment = None):
        print(avatar.filename)
        if avatar and not avatar.filename.endswith((".png", "jpeg", "gif", "jpg")):
            await ctx.respond("O arquivo deve terminar com .png, .gif, .jpeg, .jpg, .webp")
        else:  
            superbot = {}
            if name and avatar:
                superbot = {"name": name, "avatar": avatar.url}
            elif user:
                superbot = {"name": user.name, "avatar": user.display_avatar.url}
            else:
                superbot = {"name": ctx.author.name, "avatar": ctx.author.display_avatar}
        
            webhook = await ctx.channel.create_webhook(name="Becca Web")
            await ctx.respond(ephemeral=True, content="Enviado")
            await webhook.send(content=f"{msg}", username=superbot["name"], avatar_url=superbot["avatar"], )

            
    @commands.command(name="audio",description="audio")
    async def cmd_say_audio(self, ctx: commands.Context, * ,message: str):
        try:
            gtts = gTTS(text=message, lang="pt")
            gtts.save("message.mp3") 
            file = discord.File("message.mp3")
            await ctx.channel.send(content="💬 Alguem das profudezas disse...💬\n\nDica de Entidade caso você precise não anunciar que foi enviado a mensagem utilize slash commands ou comandos de /, eles vão tá nomeado como /utils audio você precisa fornecer se quer ser silencioso ou quer abrir a portas para as pesssoas que recebeu a mensagem, isso se deve a limitaçoes do discord e por pura preguiça de quem escreveu essa linha", file=file) 
            
            await ctx.message.delete()
            
            os.remove("message.mp3") 
        except Exception as err:
            print(err)
            await ctx.channel.send("💀 Alguem das profudezas tentou se comunicar com você... e não teve exito. A mensagem é perdida para sempre... 💀")
    
    @commands.command(name="say", description="say command")
    async def cmd_base_say(self, ctx: commands.Context, *, message: str):
        try:
            await ctx.message.delete()
            await ctx.channel.send(content=f"{message}") 
        except Exception as err:
            print(err)
            await ctx.channel.send("☠️...A tentativa de comunicação falhou...☠️")

    # make this after
    #@commands.command(name="avatar", description="avatar command")
    #async def cmd_avatar(self, ctx: commands.Context, *, user: discord.User = None):
        #if user:
        #    target = user
        #else: 
        #    target = ctx.author
            
        #embed = discord.Embed(title="Esse é seu receptaculo...", description="Irei Julga")
        
             
def setup(bot: Bot):
    bot.add_cog(Say(bot))
