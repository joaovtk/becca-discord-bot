from src.__main__ import Bot
from discord.ext import commands
import sqlite3
import datetime
import discord
WORDLE_DB = "db/wordle.db"
class Games(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command("wordle")

    async def cmd_wordle(self, ctx: commands.Context):
        from src.view.Wordle.WorldeView import WordleView
        con = sqlite3.Connection(WORDLE_DB)
        cur = con.cursor()
        data = datetime.date.today().isoformat()
        cur.execute("CREATE TABLE IF NOT EXISTS daily (word TEXT, date TEXT)")
        cur.execute("SELECT word FROM daily WHERE date = ?", (data,))
        daily = cur.fetchone()

        embed = discord.Embed(title="Termo", description="Termo é um popular jogo de adivinhação de palavras em português, inspirado no sucesso global Wordle, no qual o jogador tem seis tentativas para descobrir uma palavra secreta diária. *Tive uma pequena ajuda do meu amigo google*, aqui você terá todo o termo em um só comando com extras por enquanto apenas selecione as categorias de modos\n__Alias temos os seguintes modos__\n**Normal**\n**Dificil**\n**Extra**", colour=0xFFFF00)
        embed.set_image(url="https://i.imgur.com/Q6lhgWL.gif")
        if not daily[0]:
            await ctx.reply("Ainda estou pensando em uma palavra que vai fazer você perder volte daqui duas horas... Por favor")
        else:
            await ctx.reply(embed=embed, view=WordleView(WORDLE_DB, daily[0]))

def setup(bot: Bot):
    bot.add_cog(Games(bot))
