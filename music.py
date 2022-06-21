import discord
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix=";")

@client.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("There's already a song playing")
        return
    voiceChannel = discord.utils.get(ctx.guild.voice_channels,name ="General")
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key':'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file,"song.mp3")
    voice.play(discord.FFmpegAudio("song.mp3"))

@client.command()
async def leave(ctx):
    voice = discord.utils.fet(client.voice_clients,guild =ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("I am not connected to a channel :')")

@client.command()
async def pause(ctx):
    voice = discord.utils.fet(client.voice_clients,guild =ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("I am not playing rn")
    
@client.command()
async def resume(ctx):
    voice = discord.utils.fet(client.voice_clients,guild =ctx.guild)
    if voice.is_pause():
        voice.resume()
    else:
        await ctx.send("I am gonna keep playing")

@client.command()
async def stop(ctx):
    voice = discord.utils.fet(client.voice_clients,guild =ctx.guild)
    voice.stop()


client.run('ODU2ODc4MzA3MTMyMDQ3Mzkw.YNHcHA.taM2zH_R-DaRgp2Y7RHmBB-ALvE')