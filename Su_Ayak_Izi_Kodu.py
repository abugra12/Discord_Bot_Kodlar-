import discord
import time
import os
import random
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

#------------------------------------------------------------------------------

@bot.command()
async def su_ayak_izi(ctx):
    await ctx.send(f'Merhaba! Ben su ayak izi botuyum , eğer su ayak izini azaltmak istiyorsan chata %tavsiyeler yaz eğer bilgi almak 
istiyorsan chata %bilgi1 , %bilgi2 veya %bilgi3 yazabilirsin. Kolay gelsin.')

#-------------------------------------------------------------------------------

@bot.command()
async def bilgi1(ctx):
    with open('Ders-4\Resimler\Su_Ayak_Izi_fotolar\Bilgi1.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

@bot.command()
async def bilgi2(ctx):
    with open('Ders-4\Resimler\Su_Ayak_Izi_fotolar\Bilgi2.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

@bot.command()
async def bilgi3(ctx):
    with open('Ders-4\Resimler\Su_Ayak_Izi_fotolar\Bilgi3.jpeg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)



#------------------------------------------------------------------------------

@bot.command()
async def tavsiyeler(ctx):
    await ctx.send(f'Diş fırçalarken ve tıraş olurken musluğu kapatın.')
    time.sleep(1)
    await ctx.send(f'Meyve ve sebzeleri yıkarken suyu açık bırakmayın.')
    time.sleep(1)
    await ctx.send(f'Duş sürenizi kısaltın.')
    time.sleep(1)
    await ctx.send(f'Kıyafetlerinizi makinede yıkayın.')
    time.sleep(1)
    await ctx.send(f'Su sızıntılarına dikkat edin.')
    time.sleep(1)
    await ctx.send(f'Temizlik için kullandığınız suya dikkat edin.')
    time.sleep(1)
    await ctx.send(f'Arabanızı yıkarken hortum değil kova kullanın.')
    time.sleep(1)
    await ctx.send(f'Kahve yerine çayı tercih edin.')
    
#------------------------------------------------------------------------------



#----------------------------------------------------------------------------------
    

    


bot.run(" Token Is Here ")
