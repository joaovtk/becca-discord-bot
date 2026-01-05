import discord
from discord.ext import commands
import sqlite3
import asyncio

DB_PATH = "dbs/perm.db"

class Perm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ban_queue = asyncio.Queue()
        self.perm_users = set()

        # Inicializa DB e cache
        self.bot.loop.create_task(self.load_users())
        self.bot.loop.create_task(self.ban_worker())

    async def load_users(self):
        def load():
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS users (userid TEXT PRIMARY KEY)")
            cur.execute("SELECT userid FROM users")
            data = cur.fetchall()
            con.close()
            return {row[0] for row in data}

        self.perm_users = await asyncio.to_thread(load)

    async def add_user_db(self, user_id: str):
        def add():
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute("INSERT OR IGNORE INTO users VALUES (?)", (user_id,))
            con.commit()
            con.close()

        await asyncio.to_thread(add)
        
    async def remove_user_db(self, user_id: str):
            con = sqlite3.connect(DB_PATH)
            cur = con.cursor()
            cur.execute("DELETE FROM users WHERE userid = ?", (user_id,))
            con.commit()
            con.close()

    async def ban_worker(self):
        while True:
            member = await self.ban_queue.get()
            try:
                await member.ban(reason="Banimento Permanente (Sistema)")
                print(f"Banido automaticamente: {member.id}")
            except discord.Forbidden:
                print("Sem permissão para banir.")
            except discord.HTTPException:
                print("Rate limit / erro HTTP.")
            await asyncio.sleep(1.5)  # proteção contra rate limit
            self.ban_queue.task_done()

    # 🔹 Listener otimizado
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if str(member.id) in self.perm_users:
            await self.ban_queue.put(member)

    # 🔹 Comando com cooldown
    @commands.command(name="perm")
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def perm_ban(self, ctx: commands.Context, user: discord.User):

        if str(user.id) in self.perm_users:
            return await ctx.reply("⚠️ **Usuário já está na lista permanente.** ele não se atreverá a entrar aqui mais")

        msg = await ctx.reply(
            f"Deseja punir severamente o {user.mention}? se sim: \nReaja com 👀"
        )
        await msg.add_reaction("👀")

        def check(reaction, u):
            return (
                u == ctx.author
                and str(reaction.emoji) == "👀"
                and reaction.message.id == msg.id
            )

        try:
            await self.bot.wait_for("reaction_add", timeout=30, check=check)

            self.perm_users.add(str(user.id))
            await self.add_user_db(str(user.id))

            try:
                await ctx.guild.ban(user, reason="Banimento Permanente")
                await ctx.send(f"✅ {user.name} foi punido e não se atreverá a percorrer o mesmo caminho que {ctx.author}... ")
            except discord.NotFound:
                await ctx.send("Usuário não está no servidor, mas foi marcado **Gold Experience Requiem**...")

        except asyncio.TimeoutError:
            await msg.edit(content="⏱️ Pensou de mais cara apenas faça...")
        
    @commands.command(name="unperm", description="Unperm Command")
    @commands.has_permissions(ban_members=True)
    async def unperm_cmd(self, ctx: commands.Context, user: discord.User):
        if str(user.id) in self.perm_users:
            msg = await ctx.reply("Quer tirar o usuário do loop infinito de morte ? se sim: \n\nReaja com ☠️...")
            await msg.add_reaction("☠️")
            def check(reaction, u):
                return (
                    u == ctx.author
                    and str(reaction.emoji) == "☠️"
                    and reaction.message.id == msg.id
                )
            try:
                await self.bot.wait_for("reaction_add", timeout=30, check=check)
                self.perm_users.remove(str(user.id))
                await self.remove_user_db(user.id)
                await ctx.send(f"✅ {user.name} Foi perdoado e saiu do loop de ban graças a {ctx.author}... ")
                invite = await ctx.channel.create_invite(max_uses=1, unique=True)
                await user.send(f"Você foi perdoado aqui seu convite... {invite.url}")
                await ctx.guild.unban(user=user)
            except asyncio.TimeoutError:
                await msg.edit(content="⏱️ Pensou de mais cara o que essa pessoa fez ?...")
            except discord.Forbidden:
                print("Convite não foi enviado")
                
        else:
            await ctx.reply("Esse usuário não está na nossa lista de ban...")
        
        

def setup(bot):
    bot.add_cog(Perm(bot))
