import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import wikipedia
from covid_india import states
import pyjokes

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
    embed = discord.Embed(title='Memo, a Discord Bot',
                      url='https://github.com/sijey-praveen/Memo/issues', color=000000)

    embed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fherobot.app%2Fwp-content%2Fuploads%2F2020%2F10%2FAI-bot-1.jpg&f=1&nofb=1')

    embed.set_author(name="Memo Bot", url="https://github.com/sijey-praveen/Memo/", icon_url="https://cdn.discordapp.com/attachments/840203029793996811/840868393396600842/VisualElements_512.png")

    embed.add_field(name="What Memo can do?", value="> Provide Results From Wikipedia.\n> Helps You to navigate <Your_Location> to <Destination_Location> using Google Maps.\n> Provide the URL For Your Query from YouTube.\n> Provide the weather Forecast From your Country/State/City.\n> Tell jokes When You're Bored.", inline=False)

    embed.add_field(name="Commands", value="> `!maps <your_location> > <destination_location>`\n> `!memo` This Refers To About Memo.\n> `!wiki <what_to_search>`\n> `!yt play <what_to_play>`\n> `!weather <your_location>`\n> `!hi` refers General (Don't be spam).\n> `!hello` refers General (Don't be spam).\n> `!joke` refers Jokes.", inline=False)

    embed.add_field(name='For more commands ideas', value='> Create a issue and mention there\n> Visit the [GitHub page](https://github.com/sijey-praveen/Memo/issues)', inline=False)

    embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))

    await ctx.channel.send(embed=embed)

# Main Commands
@client.command()
async def weather(ctx, *, message):
    url = "https://www.google.com/search?q=weather " + message
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    pos = strd.find('Wind')
    other_data = strd[pos:]
    result = "In " + message + " the Temperature was currently " + temp.replace("C", "celcius") + ", The Sky was now " + sky + " " + other_data
    em=discord.Embed(title=result,color=discord.Color.red())
    await ctx.send(embed=em)

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
        em=discord.Embed(title=message,color=discord.Color.red(), description=result_from_wiki)
        await ctx.send(embed=em)
    except Exception:
        url = "https://en.wikipedia.org/wiki/" + message.replace(" ", "_")
        await ctx.send(url)

@client.command()
async def maps(ctx, *, message):
    url = "https://www.google.com/maps/dir/" + message.replace(">", "/").replace(" ", "")
    await ctx.send(url)


@client.command()
async def joke(ctx):
    random_joke = pyjokes.get_joke()
    em=discord.Embed(title=random_joke,color=discord.Color.red())
    await ctx.send(embed=em)

@client.command()
async def covid(ctx, *, message):
    if "india" in message.lower():
        result = states.getdata()
        await ctx.send(result)
    else:
        result = states.getdata(message)
        await ctx.send(result)

@client.command()
async def coding(ctx, *, message):
    url = "https://stackoverflow.com/search?q=" + message.replace(" ", "+")
    await ctx.send(url)
    
client.run("Your_Token")
