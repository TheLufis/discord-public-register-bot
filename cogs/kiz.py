import discord
from discord.ext import commands
import json
import sqlite3

# Veritabanına bağlan
baglanti = sqlite3.connect("kayit.db")
imlec = baglanti.cursor()

class Kiz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Kullanıcıyı kız olarak kaydeder.")
    async def kiz(self, ctx, uye: discord.Member, isim, yas):
        global imlec, baglanti  # imlec ve baglanti değişkenlerini global olarak tanımla

        # Yetkili rolünü al
        with open("settings.json", "r") as ayarlar_dosyasi:
            ayarlar = json.load(ayarlar_dosyasi)

        yetkili_rol_id = int(ayarlar["yetkili_rol_id"])
        kiz_rol_id = int(ayarlar["kiz_rol_id"])
        kayitsiz_rol_id = int(ayarlar["kayitsiz_id"])

        # Komutu kullanan kişinin yetkili rolü olup olmadığını kontrol et
        if yetkili_rol_id not in [rol.id for rol in ctx.author.roles]:
            await ctx.respond("Bu komutu kullanmaya yetkiniz yok.")
            return

        # Yaş kısmına sayı girilip girilmediğini kontrol et
        if not yas.isdigit():
            # Yaş kısmına sayı girilmediyse hata mesajı gönder
            embed = discord.Embed(title=":x: KAYIT BAŞARISIZ", color=0xFF0000)
            embed.add_field(name="Hatalı Yaş Girişi",
                            value="Lütfen yaş kısmına bir sayı girin.",
                            inline=False)
            await ctx.respond(embed=embed)
            return

        # Veritabanında kullanıcıyı ara
        imlec.execute("SELECT * FROM users WHERE user_id=?", (uye.id,))
        sonuc = imlec.fetchone()

        if sonuc:
            # Kullanıcı zaten kayıtlı ise uyarı embedini gönder
            embed = discord.Embed(title=":warning: UYARI", color=0xFFFF00)
            embed.add_field(name="Bu Kullanıcı Zaten Veritabanında Kayıtlı",
                            value="Eğer bu uyarı mesajını görüyorsanız, kaydedilen kullanıcı daha önce bu sunucuda kayıt edilmiştir. Bu yüzden bu kayıdı manuel yapmak zorundasınız.",
                            inline=False)
            await ctx.respond(embed=embed)
            return

        # Kullanıcı zaten kayıtlı değilse, kayıt işlemini başlat
        kiz_rol = discord.utils.get(ctx.guild.roles, id=kiz_rol_id)
        kayitsiz_rol = discord.utils.get(ctx.guild.roles, id=kayitsiz_rol_id)
        await uye.add_roles(kiz_rol)
        await uye.edit(nick=f"{isim} {yas}")
        await uye.remove_roles(kayitsiz_rol)

        # Veritabanına kullanıcıyı kaydet
        imlec.execute("INSERT INTO users (user_id, name, age, gender) VALUES (?, ?, ?, ?)", (uye.id, isim, yas, "Kız"))
        baglanti.commit()

        # Kayıt başarılı olduğunda sonuç mesajını gönder
        embed = discord.Embed(title=":white_check_mark: KAYIT BAŞARILI", color=0x00FF00)
        embed.add_field(name="Kullanıcı", value=uye.mention, inline=False)
        embed.add_field(name="Rol Verildi", value=kiz_rol.mention, inline=False)
        embed.add_field(name="Kayıtsız Rol Alındı", value=kayitsiz_rol.mention, inline=False)
        embed.add_field(name="Yeni İsim", value=f"{isim} {yas}", inline=False)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Kiz(bot))
