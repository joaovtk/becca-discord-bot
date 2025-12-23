from dotenv import dotenv_values

from src.__main__ import Bot

env = dotenv_values(".env")
bot = Bot()

if __name__ == "__main__":
    bot.run(env["TOKEN"])
