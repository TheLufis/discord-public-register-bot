# Discord Public Sunucuları İçin Tasarlanmış Kullanımı Kolay Ve Anlaşılır Slash Komutları Destekli Kayıt Botu

**Özellikler**
- İstatistik
- Erkek Kayıt
- Kız Kayıt
- Otomatik Rol
- Hoş Geldin Mesajı
- Slash Komutlarını Destekler

## Uyarılar
- Bu bot SQLite Veritabanı Üzerinden Çalışır Botu Çalıştırdığınız Zaman Otomatik kayit.db adı altında bir dosya oluşur bu dosyayı silmeniz veritabanına kayıtlı kişileri silmeniz anlamına gelir

## Kurulum (Visual Studio Code gibi bir yerde çalıştırmanız önerilir)

    - Projeyi Yükleyin Veya Klonlayın
    - klasörün Bulunduğu Yola: ```python pip install -r requirements.txt``` Yazın

    ### Doldurulması Gereken Dosyalar
          **config.json**
            ```{
                 "token": "",
                 "guild_id": "",
                 "sahip_id": ""
               }``` 
              - guild_id kısmına Sunucu İdsi Gelecek
              - sahip_id kısmına Botun Sahibinin İdsi Gelecek
              - Token kısmına botun tokeni gelecek

           **settings.json**

    - main.py dosyasını çalıştırın (eğer modül hatası alıoyrsanız ```pythonpip install [hatası alınan modülün adı]``` yazarak bu sorunu giderebilirsiniz)
