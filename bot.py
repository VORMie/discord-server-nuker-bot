import discord
from discord.ext import commands
from discord.flags import Intents

bottk=""

intents=discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client=commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("You're ready to rumble!")

@client.command
async def ping(ctx):
    ctx.send(f'Pong! Latency is {client.latency*1000}ms')

@client.command
async def ban(ctx, member: discord.Member, Reason=None):
    await member.ban(reason=Reason)
    ctx.send(f"The user **{member}** has been banned!")

@client.command
async def kick(ctx, member: discord.Member, Reason=None):
    await member.kick(reason=Reason)
    ctx.send(f"The user **{member}** has been kicked!")

client.run(bottk)