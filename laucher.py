from dotenv import dotenv_values
from src.main import Bot

env = dotenv_values(".env")

bot = Bot(env["TOKEN"], env["PREFIX"])

if __name__ == "__main__":
    bot.login()