import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

import json
from random import randint
from gtts import gTTS
#bruh
TOKEN = "NDQ4MTIzMDQ1MDY0ODY3ODYw.DeRiqg.bz8KKLXq9o0FzQI48cB9eJRgyF0"
bot = commands.Bot(command_prefix="!")

def getpastas():
    with open("copypastas.json","r") as obj:
        global copypastas
        copypastas = json.load(obj)
        obj.close()

def addpasta(name,txt):
    copypastas[name] = txt
    with open("copypastas.json","w") as obj:
        json.dump(copypastas,obj, indent=4)
        obj.close()
    getpastas()

def delpasta(name):
    del copypastas[name]
    with open("copypastas.json","w") as obj:
        json.dump(copypastas,obj, indent=4)
        obj.close()
    getpastas()

copypastas = {}


@bot.event
async def on_ready():
    print("bot loaded")

async def connectvoice(server):
    global voice
    voice = await bot.join_voice_channel(server)

@bot.command(pass_context=True)
async def whoareyou(ctx):
    """Basic bot info"""
    await bot.say("I am Cory-chan.")

@bot.command(pass_context=True)
async def whoami(ctx):
    """Basic sender info"""
    await bot.say(f"You are {str(ctx.message.author)}")

@bot.command(pass_context=True)
async def copypasta(ctx):
    """Send dank copypasta"""
    try:
        name = ctx.message.content.split(" ")[1]
        await bot.say(copypastas[name])
    except:
        await bot.say(f"Copypasta with name {name} not found!")

@bot.command(pass_context=True)
async def howthicc(ctx):
    """Thicc or not thicc?"""
    if ctx.message.mentions:
        if randint(1,2) == 1:
            await bot.say(f"{ctx.message.mentions[0].display_name} is dummy thicc")
        else:
            await bot.say(f"{ctx.message.mentions[0].display_name} is hecking flat")
    else:
        await bot.say("Command usage: '!howthicc @userhere'")

@bot.command(pass_context=True)
async def greene(ctx):
    """Chub n' tuck god"""
    await bot.send_file(ctx.message.channel,"greene.jpg")
    await bot.say(":heart_eyes::heart_eyes::heart_eyes::heart_eyes::heart_eyes:")

@bot.command(pass_context=True)
async def addcopypasta(ctx):
    """Add custom copypasta"""
    content = ctx.message.content.split(" ")
    name = content[1]
    txt = " ".join(content[2::])
    addpasta(name,txt)
    await bot.say(f"{name} added!")

@bot.command(pass_context=True)
async def delcopypasta(ctx):
    """Delete copypasta -- Benevolent Dictator role required"""
    try:
        if ctx.message.author.roles[1].name == "Benevolent Dictator":
            content = ctx.message.content.split(" ")
            name = content[1]
            delpasta(name)
            await bot.say(f"{name} deleted!")
        else:
            await bot.say("Sorry, you have to be a Benevolent Dictator to do this.")
    except:
        await bot.say("Something went wrong executing this command.")

@bot.command(pass_context=True)
async def listcopypastas(ctx):
    """List available copypastas"""
    await bot.say(", ".join(copypastas.keys()))

@bot.command(pass_context = True)
async def clear(ctx, number):
    """Clear all messages -- Benevolent Dictator role required"""
    try:
        if ctx.message.author.roles[1].name == "Benevolent Dictator":
            mgs = []
            number = int(number)
            async for x in bot.logs_from(ctx.message.channel, limit = number):
                mgs.append(x)
            await bot.delete_messages(mgs)
        else:
            await bot.say("Sorry, you have to be a Benevolent Dictator to do this.")
    except:
        await bot.say("Something went wrong executing this command.")

@bot.command(pass_context=True)
async def say(ctx):
    """Text to speech"""
    if not bot.is_voice_connected(ctx.message.author.server):
        await connectvoice(ctx.message.author.voice.voice_channel)
    content = " ".join(ctx.message.content.split(" ")[1::])
    tts = gTTS(text=content, lang="en")
    tts.save("speech.mp3")
    player = voice.create_ffmpeg_player("speech.mp3")
    player.start()

@bot.command(pass_context=True)
async def yt(ctx, url):
    """Play YouTube video"""
    if not bot.is_voice_connected(ctx.message.author.server):
        await connectvoice(ctx.message.author.voice.voice_channel)
    player = await voice.create_ytdl_player(url)
    player.start()

@bot.command(pass_context=True)
async def stop(ctx):
    """Disconnect from voice channel"""
    for client in bot.voice_clients:
        if client.server == ctx.message.server:
            await client.disconnect()

bot.run(TOKEN)


#Sandbox Text: 447888085695463425
#Sandbox Voice: 447888085695463427
#Sandbox Server: 447888084999340045
#Entente Text: 271052999361560579
#Entente Voice: 271052999885979648
#Entente Server: 271052999361560579
