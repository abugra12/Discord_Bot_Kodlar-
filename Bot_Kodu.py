import discord
import os
import random
from discord.ext import commands
memler = os.listdir('Ders-4\Resimler')
animal_mems = os.listdir("Ders-4\Resimler\hayvan_mems")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

#------------------------------------------------------------------------------

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

#------------------------------------------------------------------------------

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

#------------------------------------------------------------------------------

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

#------------------------------------------------------------------------------

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

#------------------------------------------------------------------------------

@bot.command()

async def rastgele_mem(ctx):

    resim_adi = random.choice(memler)
    
    with open(f'Ders-4\Resimler\{resim_adi}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    
#------------------------------------------------------------------------------

@bot.command()

async def mem_1(ctx):
    with open('Ders-4\Resimler\mem1.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

#----------------------------------------------------------------------------------
    
@bot.command()

async def rastgele_hayvan_mem(ctx):

    resim_adi2 = random.choice(animal_mems)
    
    with open(f'Ders-4\Resimler\hayvan_mems\{resim_adi2}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
    


bot.run(" Token İs HERE ")
