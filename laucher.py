import os
import asyncio
from dotenv import load_dotenv
from src.__main__ import Bot

load_dotenv()
token = os.getenv("TOKEN")

async def main():
    if not token or len(token.strip()) < 10:
        raise ValueError("ERRO FATAL: Token inválido.")

    print(f"Token detectado. Iniciando o Pycord...")
    
    # Agora o loop já existe na thread porque estamos dentro de um 'async def' rodado pelo asyncio.run()
    bot = Bot()
    
    # Iniciamos o bot passando o token. 
    # Como já estamos em um ambiente assíncrono, usamos o start() para não colidir loops.
    await bot.start(token.strip())

if __name__ == "__main__":
    try:
        # asyncio.run cria o event loop automaticamente de forma moderna e segura
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot desligado com sucesso.")