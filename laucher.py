import os
from dotenv import load_dotenv
from src.__main__ import Bot
from app import keep_alive

# 1. Tenta carregar o .env (útil para desenvolvimento local)
load_dotenv()

# 2. Prioriza o Token do sistema (Render Environment) 
# ou do .env carregado pelo load_dotenv
token = os.getenv("TOKEN")

def start_bot():
    # VALIDAÇÃO CRÍTICA: Se o token for inválido, o código para aqui.
    if not token or len(token.strip()) < 10:
        raise ValueError(
            "ERRO FATAL: O Token não foi encontrado ou é inválido! "
            "Verifique a aba 'Environment' no painel do Render."
        )

    print(f"Token detectado (tamanho: {len(token)}). Iniciando...")
    #keep_alive()
    
    # Inicia o bot de fato
    bot = Bot()
    bot.run(token.strip())

if __name__ == "__main__":
    start_bot()