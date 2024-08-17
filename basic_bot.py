import discord
import random
import requests
import os
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
    await ctx.send("$hello \n$heh N\n$flip_coin\n$gen_emoji\n$add N N\n$rest N N\n$multiply N N\n$divide N N\n$gen_pass\n$roll NdN\n$repeat N palabra\n$choose opcion1 opcion2 (...)\n$mem\n$random_mem\n$duck\n$huerto_urbano")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Que tal, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command() 
async def flip_coin(ctx):
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
async def rest(ctx, num1: int, num2: int):
    await ctx.send(int(num1-num2))

@bot.command() 
async def multiply(ctx, num1: int, num2: int):
    await ctx.send(int(num1*num2))

@bot.command() 
async def divide(ctx, num1: int, num2: int):
    await ctx.send(int(num1/num2))
    
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

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    with open('memes/meme1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def random_mem(ctx):
    imagenes = os.listdir('memes')
    with open(f'memes/{random.choice(imagenes)}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def huerto_urbano(ctx):
    await ctx.send(f"""Hola, soy un bot {bot.user}!""")
    await ctx.send('Te voy hablar un poco sobre el cultivo de plantas urbano')
    time.sleep(1)
    await ctx.send('El cultivo urbano de plantas es una forma innovadora de conectar con la naturaleza en medio de la ciudad.')
    time.sleep(2)
    await ctx.send('Aprovechando espacios pequeños, como balcones y azoteas, podemos crear jardines que no solo embellecen el entorno, sino que también contribuyen a mejorar la calidad del aire y a producir alimentos frescos.')
    time.sleep(2)
    await ctx.send("Es una práctica que promueve la autosuficiencia y el bienestar, transformando rincones urbanos en oasis verdes.")
    time.sleep(3)
    await ctx.send("Quieres saber las ventajas de tener cultivos urbanos?, Responde con 'sí' o 'no'.")
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("1. Mejora la calidad del aire.")
            await ctx.send("2. Proporciona alimentos frescos.")
            await ctx.send("3. Reduce el estrés y mejora el bienestar.")   
        else:
            await ctx.send("Está bien, si alguna vez te da curiosidad, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Quieres consejos sobre cómo cultivar?, responde si o no")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['sí', 'si']:
            await ctx.send("1. Aprovecha espacios verticales para maximizar el área disponible.")
            await ctx.send("2. Utiliza contenedores y macetas con buen drenaje.")
            await ctx.send("3. Selecciona plantas adaptadas a las condiciones urbanas, como lechugas, rábanos, chícharos, etc.")
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
        
bot.run("TOKEN")
