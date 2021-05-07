import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix="!")

@client.command()
async def hello(ctx):
    await ctx.send("Hello")

@client.command()
async def hi(ctx):
    await ctx.send("Hi")

@client.command()
async def play(ctx, *, message):
    url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
    GET_content = requests.get(url)
    Play_Content = str(GET_content.text)
    await ctx.send(Play_Content)

@client.command()
async def yt(ctx, *, message):
    url = "https://www.youtube.com/results?search_query=" + message
    await ctx.send(url)

@client.command()
async def download(ctx, *, message):
    url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
    GET_content = requests.get(url)
    dl = GET_content.text.replace("youtube", "youtubepp")
    await ctx.send(dl)

@client.command()
async def dl(ctx, *, message):
    url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
    GET_content = requests.get(url)
    dl = GET_content.text.replace("youtube", "youtubepp")
    await ctx.send(dl)

@client.command()
async def memo(ctx):
    command_list = "!hi\n!hello\n!dl\n!download\n!play"
    await ctx.send(command_list)

@client.command()
async def commands(ctx):
    command_list = "!hi\n!hello\n!dl\n!download\n!play"
    await ctx.send(command_list)

client.run("ODQwMjI3NDk4NjAzMzE1MjYw.YJVI1g.Yd8BBCSQ8SnSoxacb7I9jjrVMSE")
