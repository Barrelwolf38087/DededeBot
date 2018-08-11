import discord
import requests, asyncio, platform, os
from ctypes.util import find_library

discord.opus.load_opus(find_library("opus"))

# Make sure we're in the bot's root dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open("token.txt", "r") as token_file:
    # We have to grab the first line
    # because a newline in the string will
    # cause cryptic errors, and nobody
    # likes those
    lines = token_file.read().splitlines()
    global TOKEN    
    TOKEN = lines[0]

client = discord.Client()

commands = {}

@client.event
async def on_message(message):
    # No self-replying
    if message.author == client.user:
        return
    
    if message.content == "!dedede":
        with open("dedede.jpg", "rb") as dedede_jpg:
            await client.send_file(message.channel, dedede_jpg, filename="Dedede.jpg", content="All hail our lord and savior")
        return
    
    if message.content.startswith("!d"):
        args = message.content[3:].split(" ")

        if args[0] in commands.keys():
            commands[args[0]](args[1:])
    
@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    voice = await client.join_voice_channel(client.get_channel("477643870042325007"))
    player = voice.create_ffmpeg_player("hypno.flac", before_options="-fflags +genpts -stream_loop -1 ")
    player.start()

client.run(TOKEN)