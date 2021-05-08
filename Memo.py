import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix="!")

@client.command()
async def hello(ctx):
    command_list = "!\n!download\n!play\n!spotify\n!soundcloud\n!ytm\n!yt"
    await ctx.send(command_list)

@client.command()
async def hi(ctx):
    command_list = "!\n!download\n!play\n!spotify\n!soundcloud\n!ytm\n!yt"
    await ctx.send(command_list)

@client.command()
async def play(ctx, *, message):
    url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
    GET_content = requests.get(url)
    Play_Content = str(GET_content.text)
    await ctx.send(Play_Content)

@client.command()
async def yt(ctx, *, message):
    url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
    GET_content = requests.get(url)
    Play_Content = str(GET_content.text)
    await ctx.send(Play_Content)

@client.command()
async def download(ctx, *, message):
    url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
    GET_content = requests.get(url)
    dl = GET_content.text.replace("youtube", "youtubepp")
    await ctx.send(dl)

@client.command()
async def spotify(ctx, *, message):
    url = "https://open.spotify.com/search/" + message.replace(" ", "%20")
    await ctx.send(url)

@client.command()
async def soundcloud(ctx, *, message):
    url = "https://soundcloud.com/search/sounds?q=" + message.replace(" ", "%20")
    await ctx.send(url)


@client.command()
async def ytm(ctx, *, message):
    url = "https://music.youtube.com/search?q=" + message.replace(" ", "+")
    await ctx.send(url)

@client.command()
async def memo(ctx):
    command_list = "!hi\n!hello\n!dl\n!download\n!play"
    await ctx.send(command_list)

@client.command()
async def commands(ctx):
    command_list = "!\n!download\n!play\n!spotify\n!soundcloud\n!ytm\n!yt"
    await ctx.send(command_list)

client.run("Your_Token")
