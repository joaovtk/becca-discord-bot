import os
import asyncio
from dotenv import load_dotenv
from src.__main__ import Bot
import sqlite3
import datetime

from discord.ext import tasks
import requests
import json

load_dotenv()
token = os.getenv("TOKEN")
DB_PATH = "/db/wordle.db"

async def main():
    


    if not token or len(token.strip()) < 10:
        raise ValueError("ERRO FATAL: Token inválido.")

    print(f"Token detectado. Iniciando o Pycord...")
    
    # Agora o loop já existe na thread porque estamos dentro de um 'async def' rodado pelo asyncio.run()
    bot = Bot()
    
    # Iniciamos o bot passando o token. 
    # Como já estamos em um ambiente assíncrono, usamos o start() para não colidir loops.
    @tasks.loop(seconds=10)
    async def wordle_daily_update():
    
        contentTermo = requests.get("https://random-word-api.herokuapp.com/word?lang=pt-br&length=5")
        responseTermo = responseTermo = json.dumps(contentTermo.json())
        responseTermo = responseTermo.replace("[", "")
        responseTermo = responseTermo.replace("]", "")
        responseTermo = responseTermo.replace('"', "")
    
        def fetch_word(word):
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute("SELECT word FROM daily")
            data = cur.fetchall()
            
            con.commit()
            con.close()
            return data
        def fetch_date(date):
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute("SELECT date FROM daily")
            data = cur.fetchall()
            con.commit()
            con.close()
            return data      
            
        def create_word(word, date):
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS daily (word TEXT, date TEXT)")
    
            word = fetch_word(word)
            data = fetch_date(datetime.date.fromisoformat)
            if not data:
                if not word:
                    cur.execute("INSERT INTO daily VALUES(?, ?)", (word, date))
            con.commit()
            con.close()
            print("Palavra Criada")
        create_word(responseTermo, datetime.date.today().isoformat())
    await bot.start(token.strip())
   
        

if __name__ == "__main__":
    try:
        # asyncio.run cria o event loop automaticamente de forma moderna e segura
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot desligado com sucesso.")