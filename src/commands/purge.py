from datetime import datetime

import discord
from discord.ext import commands

from src.__main__ import Bot
import asyncio

class Purge(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    def check_user(ctx):
        return ctx.author.id in [768614963002474506, 608309054485430294]

    @commands.command(name="punban")
    @commands.check(check_user)
    async def cmd_purge_unban(self, ctx: commands.Context, user: discord.User):
        banlist = ctx.guild.bans()
        async for ban in banlist:
            if ban.user.id == user.id:
                await ctx.guild.unban(user)
                msg = await ctx.reply("o usuário foi desbanido por forças divinas")
                invite = await ctx.channel.create_invite(max_age=3600, max_uses=1, unique=True, reason="Desbanimento")
                await user.send(invite.url)
                return

        await ctx.reply("O Usuário já está desbanido, eu sei que algumas pessoas merecem perdão mais por favor usa o comando **;pban** denovo, **to esperando...**")
    @commands.command(name="pban")
    @commands.check(check_user)
    async def cmd_purge_ban(self,ctx: commands.Context, user: discord.Member):
        banlist = ctx.guild.bans()
        have = False
        print(user)
        print(have, banlist)
        async for ban in banlist:
            
            print(ban.user.name, user.id)
            if ban.user.id == user.id:
                have = True
                break
        if not have:
            embed = discord.Embed(title="Com esse tesouro, eu invoco o General Divino Mahoraga...", description="Quer refazer a luta de ||Megumi vs Haruta ?||", color=0x0000ff)
            embed.set_image(url="https://i.makeagif.com/media/3-30-2024/r8FCo1.gif")
            msg = await ctx.reply(embed=embed)

            await msg.add_reaction("🤭")
            try:
                def check(reaction, target):
                    return target == ctx.author and str(reaction.emoji) == "🤭" and reaction.message.id == msg.id
                
                reaction, target = await self.bot.wait_for("reaction_add", timeout=30.00, check=check)
            except asyncio.TimeoutError:
                await ctx.send("Tempo esgotado")
    
            else:
                await ctx.guild.ban(user)
                embed.description = "**USUÁRIO BANIDO**\n\nAproveite seu mundo perfeito..."
                await ctx.send("Brutal", embed=embed)
        else:
            embed = discord.Embed(title="E falhou... to cansada foi mal\n", description="E também tem a possibilidade da pessoa já tá banido e infelizmente ainda não elimino pessoas da existencia... :)", color=0xff0000)
            embed.set_image(url="https://i.pinimg.com/1200x/9f/d5/df/9fd5df9724156c37cab3423e32b3d830.jpg")
            await ctx.reply(embed=embed)
    @commands.command(name="pkmove")
    async def cmd_kick_call(self, ctx: commands.Context, member: discord.Member, voice: discord.VoiceChannel = None):
        if member.voice:
            if voice:
                await member.move_to(voice)
                await ctx.reply(f"Movido e eu não sei porque...")
            else:
                await member.move_to(voice)
                await ctx.reply(f"Tomou de morador rsrs...")
        else:
            await ctx.reply("Ei ele nem tá em call cara... Não dá para tirar ele de uma coisa que ele não tá :(")
    @commands.command(name="pkmute")
    async def cmd_mute(self, ctx: commands.Context, member: discord.Member):
        if member.voice:
            if not member.voice.mute:
                await member.edit(mute=True)
                await ctx.reply("O usuário parou de falar...")
            else:
                await member.edit(mute=False)
                await ctx.reply("O usuário abriu a boca...")
        else:
            await ctx.reply("Eu sei que muitas pessoas merecem ficar calada mas eu acho que ele não tá falando...")

    @cmd_purge_ban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Digite o usuário por favor.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.reply("Eu não to vendo ninguem amigo por favor tente banir uma pessoa que existe... e tome seu remedio para **esquizofrenia** eu nem existo...")
    @cmd_purge_unban.error
    async def ban_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Digite o usuário por favor.")

        elif isinstance(error, discord.Forbidden):
            await ctx.send("O usuário se recusou a voltar...")
        
        elif isinstance(error, discord.HTTPException):
            await ctx.send("Mensagem interceptada...")

    @cmd_kick_call.error
    @cmd_mute.error
    @cmd_kick_call.error
    async def kick_call_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("Essa pessoa realmente existe cara...")

def setup(bot):
    bot.add_cog(Purge(bot))
