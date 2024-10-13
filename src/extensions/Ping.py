import lightbulb
from laucher import bot

plugin = lightbulb.Plugin(__name__)

@plugin.command
@lightbulb.command(name="ping", description="Comando Basico de Todo Bot")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def cmdPing(ctx: lightbulb.Context):
    await ctx.respond("PONG!!!!!")

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)