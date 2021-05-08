import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import wikipedia


client = commands.Bot(command_prefix="!")

# General Commands
@client.command()
async def hello(ctx):
    await ctx.send("Hello")

@client.command()
async def hi(ctx):
    await ctx.send("Hi")

@client.command()
async def memo(ctx):
    command_list = "\n!yt\n!weather\n!maps\n!wiki"
    await ctx.send(command_list)

@client.command()
async def about(ctx):
    about = "Hello, i'm Memo.\nI Live in Discord.\nI provide url for User Queries.\nFor more information \nvisit : https://github.com/sijey-praveen/Memo"
    await ctx.send(about)

# Main Commands
@client.command()
async def weather(ctx, *, message):
    url = "https://www.google.com/search?q=weather " + message
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str.split('\n')
    sky = data[1]
    result = "In " + message + " the Temperature was currently " + temp.replace("C", "celcius")
    await ctx.send(result)

@client.command()
async def yt(ctx, *, message):
    url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
    GET_content = requests.get(url)
    Play_Content = str(GET_content.text)
    await ctx.send(Play_Content)

@client.command()
async def wiki(ctx, *, message):
    try:
        result_from_wiki = wikipedia.summary(str(message), sentences=5)
        await ctx.send(result_from_wiki)
    except Exception:
        url = "https://en.wikipedia.org/wiki/" + message.replace(" ", "_")
        await ctx.send(url)

@client.command()
async def maps(ctx, *, message):
    url = "https://www.google.com/maps/dir/" + message.replace(">", "/")
    await ctx.send(url)
    
client.run("Your_Token")
