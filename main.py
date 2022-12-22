import nextcord
from nextcord.ext import commands, tasks
import logging
import sqlite3
from db.db import AccountDB

Account = AccountDB()
guild_ids = [938687715673767937, 906706894482206760]
token = "${{secrets.TOKEN}}"
intents = nextcord.Intents.default()
help_command = commands.DefaultHelpCommand(no_category='Commands')
bot = commands.Bot(command_prefix=">", intents=intents, help_command=help_command)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.online, activity=nextcord.Game('BDE'))
    print(f'logged in as {bot.user}')

@bot.slash_command(description="registeration", guild_ids=guild_ids)
async def registerate(ctx):
    user = ctx.user.id        
    Account.register(user, 100)
    await ctx.send(f"did succesfuly registered as {ctx.user.mention} {user}")
   
@bot.slash_command(guild_ids=guild_ids)
async def deposit(ctx, amount: int):
    Account.deposit(ctx, amount)
    await ctx.send(":thumbsup:")


@bot.slash_command(guild_ids=guild_ids)
async def ping(ctx):
	await ctx.send("ping")

 
@bot.slash_command(guild_ids=guild_ids)
async def checkme(ctx):
    await ctx.send(Account.check(ctx.user.id)[str(ctx.user.id)])

@bot.slash_command(guild_ids=guild_ids)
async def checkall(ctx):
    await ctx.send(Account.check(ctx.user.id))


bot.run(token)