import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix="!")

@client.command()
async def hello(ctx):
    command_list = "\n!ytdownload\n!spotify\n!soundcloud\n!ytmusic\n!yt\n!google\n!medium\n!github\n!weather\n!gmaps\n!maps\n!ddg\n!wiki"
    await ctx.send("Hello" + command_list)

@client.command()
async def hi(ctx):
    await ctx.send("Hi")

@client.command()
async def weather(ctx, *, message):
    url = "https://www.google.com/search?q=weather " + message
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str.split('\n')
    sky = data[1]
    result = "Temperature was currently " + temp.replace("C", "celcius")
    await ctx.send(result)

@client.command()
async def yt(ctx, *, message):
    url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
    GET_content = requests.get(url)
    Play_Content = str(GET_content.text)
    await ctx.send(Play_Content)

@client.command()
async def medium(ctx, *, message):
    url = "https://medium.com/search?q=" + message.replace(" ", "%20")
    await ctx.send(url)

@client.command()
async def google(ctx, *, message):
    url = "https://www.google.com/search?q=" + message.replace(" ", "+")
    await ctx.send(url)

@client.command()
async def wiki(ctx, *, message):
    url = "https://en.wikipedia.org/wiki/" + message.replace(" ", "_")
    await ctx.send(url)

@client.command()
async def ddg(ctx, *, message):
    url = "https://duckduckgo.com/?t=ffab&q=" + message.replace(" ", "+")
    await ctx.send(url)

@client.command()
async def about(ctx):
    about = "Hello, i'm Memo.\nI Live in Discord.\nI provide url for User Queries.\nFor more information \nvisit : https://github.com/sijey-praveen/Memo"
    await ctx.send(about)

@client.command()
async def github(ctx, *, message):
    if "trending" in message:
        trending = "https://github.com/trending"
        await ctx.send(trending)

@client.command()
async def ytdownload(ctx, *, message):
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
async def ytmusic(ctx, *, message):
    url = "https://music.youtube.com/search?q=" + message.replace(" ", "+")
    await ctx.send(url)

@client.command()
async def googlemaps(ctx, *, message):
    url = "https://www.google.com/maps/search/" + message.replace(" ", "+")
    await ctx.send(url)

@client.command()
async def maps(ctx, *, message):
    url = "https://duckduckgo.com/?t=ffab&q=" + message.replace(" ", "+") + "&atb=v271-2&ia=web&iaxm=maps"
    await ctx.send(url)

@client.command()
async def memo(ctx):
    command_list = "\n!ytdownload\n!spotify\n!soundcloud\n!ytmusic\n!yt\n!google\n!medium\n!github\n!weather\n!gmaps\n!maps\n!ddg\n!wiki"
    await ctx.send(command_list)

@client.command()
async def commands(ctx):
    command_list = "\n!ytdownload\n!spotify\n!soundcloud\n!ytmusic\n!yt\n!google\n!medium\n!github\n!weather\n!gmaps\n!maps\n!ddg\n!wiki"
    await ctx.send(command_list)
    
client.run("Your_Token")
