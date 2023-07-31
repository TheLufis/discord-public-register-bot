import discord
from discord.ext import commands
import json
import sqlite3

intents = discord.Intents().all()

with open("config.json", "r") as config_file:
    config = json.load(config_file)

# ---------------------------Database---------------------------------

conn = sqlite3.connect("kayit.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    gender TEXT
                )""")
conn.commit()

bot = commands.Bot(intents=intents)

# ---------------------------Otomatik Giriş---------------------------------

@bot.event
async def on_member_join(member: discord.Member):
    guild = member.guild
    
    channel_id = 1234 # Hoş geldin mesajının gönderileceği kanal id
    
    channel = bot.get_channel(channel_id)
    
    await channel.send(f"Hoş Geldin {member.mention} {guild.name}!")
    role = discord.utils.get(guild.roles, id=1234) #Otomatik verilecek rol kayıtsız id ile aynı şeyi yazabilirsiniz
    await member.add_roles(role)

# ---------------------------Status---------------------------------

@bot.event
async def on_ready():
    print(f"Giriş Yapıldı {bot.user}")
    await bot.change_presence (activity=discord.Game (name="Register Bot")) # Botun durumu

# ---------------------------Coglar---------------------------------

bot.load_extension("cogs.kiz")
bot.load_extension("cogs.erkek")
bot.load_extension("cogs.istatistik")
bot.load_extension("cogs.test")

bot.run(config["token"])

conn.close()
