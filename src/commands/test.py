import discord
from discord.ext import commands
from src.__main__ import Bot
import requests
import json
import sqlite3
import datetime
WORDLE_DB = "db/wordle.db"
class Test(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.DB_PATH = WORDLE_DB
    @commands.command("test")
    async def cmd_tests(self, ctx: commands.Context):
        
        def fetch_word(word):
            con = sqlite3.connect(self.DB_PATH)
            cur = con.cursor()
            cur.execute("SELECT word FROM daily")
            data = cur.fetchall()
            
            con.commit()
            con.close()
            return data
        def fetch_date(date):
            con = sqlite3.connect(self.DB_PATH)
            cur = con.cursor()
            cur.execute("SELECT date FROM daily")
            data = cur.fetchall()
            con.commit()
            con.close()
            return data      
         
        def create_word(word, date):
            con = sqlite3.connect(self.DB_PATH)
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS daily (word TEXT, date TEXT)")

            word = fetch_word(word)
            data = fetch_date(datetime.date.fromisoformat)
            if not data:
                if not word:
                    cur.execute("INSERT INTO daily VALUES(?, ?)", (word, date))
            
            con.commit()
            con.close()
        create_word("teste", datetime.date.today().isoformat())
        await ctx.reply("Check Terminal")
def setup(bot: Bot):
    bot.add_cog(Test(bot))
