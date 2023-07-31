from discord.ext import commands
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    
class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[int(config["guild_id"])], description="Botun Aktifliğini Test Etme Komutu")
    async def test(self, ctx):
        await ctx.respond("Bot Aktif Durumda")

def setup(bot):
    bot.add_cog(Test(bot))
