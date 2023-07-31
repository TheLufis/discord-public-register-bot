import discord
from discord.ext import commands
import platform
import psutil
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

class Istatistik(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[int(config["guild_id"])], description="Botun istatistiklerini gösterir.")
    async def istatistik(self, ctx):
        system_info = f"**İşletim Sistemi:** {platform.system()} {platform.release()}"
        python_info = f"**Python Sürümü:** {platform.python_version()}"
        discord_info = f"**PyCord Sürümü:** {discord.__version__}"
        ping_info = f"**Bot Ping:** {round(self.bot.latency * 1000)} ms"  # ms cinsinden ping değeri
        memory_info = f"**Bellek Kullanımı:** {psutil.virtual_memory().percent} %"
        ram_info = f"**RAM Kullanımı:** {psutil.virtual_memory().used / 2**30:.2f} GB / {psutil.virtual_memory().total / 2**30:.2f} GB"

        embed = discord.Embed(title="Bot İstatistikleri", color=0x00FF00)
        embed.add_field(name="Sistem Bilgileri", value=system_info, inline=False)
        embed.add_field(name="Python Bilgileri", value=python_info, inline=False)
        embed.add_field(name="Discord Bilgileri", value=discord_info, inline=False)
        embed.add_field(name="Bot Ping", value=ping_info, inline=False)
        embed.add_field(name="Bellek Kullanımı", value=memory_info, inline=False)
        embed.add_field(name="RAM Kullanımı", value=ram_info, inline=False)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Istatistik(bot))
