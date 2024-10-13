import hikari
import lightbulb

class Bot(lightbulb.BotApp):
    def __init__(self, token: str, prefix: str):
        super().__init__(token=token, prefix=prefix, intents=hikari.Intents.ALL)

    async def onReady(self, event: hikari.StartedEvent):
        print(f"Started {self.get_me().username} bot")
        self.load_extensions_from("src/extensions/")

    def login(self):
        self.event_manager.subscribe(hikari.StartedEvent, self.onReady)
        super().run(activity=hikari.Activity(name="Trabalhando em comandos de musica...", type=hikari.ActivityType.PLAYING))