import sqlite3
import datetime
from src.__main__ import Bot

from discord.ext import tasks, commands
import requests
import json
DB_PATH = "db/wordle.db"
class WordleUpdate(commands.Cog):
   def __init__(self, bot):
        self.bot = bot
        self.wordle_daily_update.start()
   @tasks.loop(hours=2)
   async def wordle_daily_update(self):
        contentTermo = requests.get("https://random-word-api.herokuapp.com/word?lang=pt-br&length=5")
        responseTermo = responseTermo = json.dumps(contentTermo.json())
        responseTermo = responseTermo.replace("[", "")
        responseTermo = responseTermo.replace("]", "")
        responseTermo = responseTermo.replace('"', "")

        def fetch_word(word):
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute("SELECT word FROM daily WHERE word = ?", (word,))
            data = cur.fetchall()

            con.commit()
            con.close()
            return data
        def fetch_date(date):
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute("SELECT date FROM daily WHERE date = ?", (date,))
            data = cur.fetchall()
            con.commit()
            con.close()
            return data

        def create_word(word, date):
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS daily (word TEXT, date TEXT)")

            word_data = fetch_word(word)
            data = fetch_date(datetime.date.today().isoformat())
            print(data)
            print(word_data)
            if not data:
                if not word_data:
                    cur.execute("INSERT INTO daily VALUES(?, ?)", (word, date))
                    print("Palavra Criada")
            else:
                print("Palavra já criada")
            con.commit()
            con.close()

        create_word(responseTermo, datetime.date.today().isoformat())

def setup(bot: Bot):
    bot.add_cog(WordleUpdate(bot))
