from dotenv import dotenv_values
import os
from src.__main__ import Bot
from app import keep_alive

bot = Bot()
env = dotenv_values(".env")
print(len(env)) 
if len(env) > 0:
    keep_alive()
    if __name__ == "__main__":
        bot.run(env["TOKEN"])
else:   
    keep_alive()
    if __name__ == "__main__":
        bot.run(os.getenv("TOKEN"))