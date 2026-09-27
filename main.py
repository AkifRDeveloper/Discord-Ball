import discord
from discord.ext import commands
from model import get_class_name  # Model dosyasını içe aktarıyoruz

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_path = f"./{attachment.filename}"
            await attachment.save(file_path)
            await ctx.send(f"Resmi bu yola kaydettim {file_path}")
            
            try:
                # Modeli çalıştırıp sonuçları alıyoruz
                class_name, confidence_score = get_class_name("keras_model.h5", "labels.txt", file_path)
                
                # Sonucu Discord'a gönderiyoruz
                await ctx.send(f"Tahmin: {class_name}\nDoğruluk oranı: {confidence_score:.2f}")
            except Exception as e:
                await ctx.send(f"Model çalıştırılırken bir hata oluştu: {e}")
    else:
        await ctx.send("Bir dosya yuklemeyi unuttun.")

bot.run("")