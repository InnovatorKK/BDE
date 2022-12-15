import nextcord
from nextcord.ext import commands, tasks
import logging
import sqlite3

con = sqlite3.connect('db/data.db')
cur = con.cursor()
#cur.execute("CREATE TABLE Account(DiscordID text, Balance integer);")

guild_ids = [938687715673767937]
token = "MTA1MjgzNzYyMzgzMzU1OTExMA.GQ1OTX.QirONV9ZrY-xxGvoK2OnMCzMRBwxeimn9vIgKI"
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
    cur.execute("INSERT INTO Account Values(:DiscordID, :Balance);", {"DiscordID":user, "Balance":0})
    await ctx.send(f"succesfuly registered as {ctx.user.mention} {user}")
    
@bot.slash_command(guild_ids=guild_ids)
async def ping(ctx):
	await ctx.send("ping")
 
@bot.slash_command(guild_ids=guild_ids)
async def my(ctx):
    cur.execute('SELECT * FROM Account')
    for row in cur:
        await ctx.send(row)

bot.run(token)