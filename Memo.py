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
    wmcd = """Memo, A Discord Bot.
What Memo Can Do?
    - Provide Results From Wikipedia.
    - Helps You to navigate <Your_Location> to <Destination_Location> using Google Maps.
    - Provide the URL For Your Query from YouTube.
    - Provide the weather Forecast From your Country/State/City.
    """
    await ctx.send(wmcd)

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
