from src.__main__ import Bot
from discord.ext import commands
import sqlite3
import datetime
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
        response = cur.fetchone()
        await ctx.reply(content="test", view=WordleView(WORDLE_DB, response[0]))

def setup(bot: Bot):
    bot.add_cog(Games(bot))
