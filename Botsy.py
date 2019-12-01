import os
import discord 
import random
from discord.ext import commands
from google_images_download import google_images_download
from bs4 import BeautifulSoup
import requests
import html as HTML
    
token = "NjQ3OTg4MjI3MjI3MjU0ODA3.XdoE-g.Fd6KH7TDwSPQ6aF-4P_BoFM5zLA"
GUILD = "Planet Hanyu"
client = discord.Client()
#user Ids
turtle='chaudhary#4703'
purple= 'PurpleFriend#4413'
lemino = 'LemiNo#0864'
bunny = 'Talk5678#0088'
skynet = 'Skynet#2313'
# smaller codes
bunny_food = '*serves carrot :carrot: *'
cow_food = '*gives grass to :cow:*'


 

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
       # await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException



bot = commands.Bot(command_prefix='>')
@bot.command(name='speak')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll', help='Simulates rolling dice.')
async def roll(ctx, number_of_sides: int):
    pick =str(random.choice(range(1,  number_of_sides + 1)))      
    await ctx.send(pick)

@bot.command(name='food', help='This gives you food')
async def get_food(ctx):
    print(ctx.author)
    author = str(ctx.author)
    
    if(turtle == author or purple == author):
        await ctx.send(cow_food)
    elif(bunny == author):
        await ctx.send(bunny_food)
    elif(lemino == author):
        await ctx.send('*throws some garlic* Catch!')
    elif( skynet == author):
        await ctx.send("You get no food! Only cucumba :cucumber: for you")
    else:
        await ctx.send('*showers with food of all kinds* Hope you got room!')

@bot.command(name='yuzu', help='It will give you a random Yuzu pic')
async def get_yuzu(ctx):
    keyword = "yuzu figure skater"
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": keyword,"limit":20, "print_urls": False, "no_download": True} 
    paths = response.download(arguments)   #passing the arguments to the function
    pic_dict , _ = paths
    imageUrls = pic_dict.get(keyword)   
    pick =random.choice(range(1,  len(imageUrls)))
    imageUrl= imageUrls[pick]
    await ctx.send(imageUrl)

@bot.command(name='hug')
async def get_hugged(ctx):
    keyword = "hug chibi gif"
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": keyword,"limit":20, "print_urls": False, "no_download": True} 
    paths = response.download(arguments)   #passing the arguments to the function
    pic_dict , _ = paths
    imageUrls = pic_dict.get(keyword)   
    pick =random.choice(range(1,  len(imageUrls)))
    imageUrl= imageUrls[pick]
    
    mention = ctx.message.mentions[0]
    print(mention.mention) 
    await ctx.send( ctx.author.mention + " hugs "  + mention.mention)
    await ctx.send(imageUrl)
    
@bot.command(name='dadjoke')
async def get_dadjoke(ctx):
    url = "https://icanhazdadjoke.com/" 
    response = requests.get(url, headers = {"Accept": "text/plain"})
    await ctx.send(response.content)
    
bot.run(token)
