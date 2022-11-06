from aiohttp import client
import discord
from datetime import datetime
 
from discord.ext import commands
 
import urllib.request
import random
import time
 
bot = commands.Bot(command_prefix="$", case_insensitive = True)
 
word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()
 
word = ''
start = 0
@bot.command()
async def Hi(ctx):
    await ctx.send("Hi, welcome to our server")
 
@bot.command()
async def Ping(ctx):
    await ctx.send("Pong")
    await ctx.send('My ping is '+str(int(bot.latency*1000))+'ms')
 
@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
       detailMessage = 'We welcome {0.mention} to the {1.name}!'.format(member, guild)
       await guild.system_channel.send(detailMessage)
       return
 
@bot.event
async def on_message(message):
    if not message.author.bot and message.content==word:
        end = time.time()
        difference = str(round(end-start,3))
        await message.channel.send('It took you '+difference+' seconds to type the word '+word+"!")
    if not message.author.bot and ('copy' in message.content or 'copying' in message.content or 'copied' in message.content):
        await message.channel.send(''+message.content+' :P')
    await bot.process_commands(message)
 
@bot.command()
async def PingMe(ctx):
    #to get a member from a 'ctx' object is ctx.author
    #from there its .mention will mention (ping) the user
    #also there are others like .id
    await ctx.send(ctx.author.mention)
 
@bot.command()
async def MyName(ctx):
    await ctx.send('Your name is '+ctx.author.display_name)
 
@bot.command()
async def MyAge(ctx):
    creationDate = datetime.strptime(ctx.author.created_at.strftime('%m/%d/%Y'), '%m/%d/%Y')
    timeDelt = str(datetime.now()-creationDate)
    timeDelt = timeDelt.split(',')
    await ctx.send('Your account was created on '+creationDate.strftime('%m/%d/%Y')+', that was '+timeDelt[0]+' ago')
 
@bot.command()
async def ServerJoin(ctx):
    joinDate = datetime.strptime(ctx.author.joined_at.strftime('%m/%d/%Y'), '%m/%d/%Y')
    timeDelt = str(datetime.now()-joinDate)
    timeDelt = timeDelt.split(',')
    await ctx.send('Your joined the server on '+joinDate.strftime('%m/%d/%Y')+', that was '+timeDelt[0]+' ago')
 
@bot.command()
async def ServerAge(ctx):
    screationDate = datetime.strptime(ctx.author.guild.created_at.strftime('%m/%d/%Y'), '%m/%d/%Y')
    timeDelt = str(datetime.now()-screationDate)
    timeDelt = timeDelt.split(',')
    await ctx.send('This server was created on '+screationDate.strftime('%m/%d/%Y')+', that was '+timeDelt[0]+' ago')
 
@bot.command(aliases=['sg'])
async def SpellingGame(ctx):
    global word
    global start
    word = words[random.randint(0,len(words)-1)]
    await ctx.send('Spell: '+word)
    start = time.time()
 
Secret = open("secret.txt", 'r')
Secret = Secret.read()
 
bot.run(Secret)
 
 
 
 

