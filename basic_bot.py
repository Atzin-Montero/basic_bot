import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def help_me(ctx):
    await ctx.send("Aquí tienes una lista de comandos (N significa un número): ")
    await ctx.send("$hello")
    await ctx.send("$heh N")
    await ctx.send("$flip_coin")
    await ctx.send("$gen_emoji")
    await ctx.send("$add N N")
    await ctx.send("$gen_pass")
    await ctx.send("$roll NdN")
    await ctx.send("$repeat N palabra")
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Que tal, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command() 
async def flip(ctx):
    flip = random.randint(0, 2)
    if flip == 0:
        await ctx.send("CRUZ")
    else:
        await ctx.send("CARA")

@bot.command() 
async def gen_emoji(ctx):
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    await ctx.send(random.choice(emoji))

@bot.command() 
async def add(ctx, num1: int, num2: int):
    await ctx.send(int(num1+num2))
    
@bot.command() 
async def gen_pass(ctx, pass_length = 8):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    
    await ctx.send(password)

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

bot.run("TOKEN")
