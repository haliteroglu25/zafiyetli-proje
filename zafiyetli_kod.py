import sqlite3  

baglanti = sqlite3.connect("kullanicilar.db")
imlec = baglanti.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS kullanicilar (id INTEGER PRIMARY KEY, kullanici_adi TEXT, sifre TEXT)")

def zafiyetli_giris_yap(kullanici_adi):
    sorgu = f"SELECT * FROM kullanicilar WHERE kullanici_adi = '{kullanici_adi}'"
    print("SQL Sorgusu:", sorgu)  # Hata ayıklama için sorguyu ekrana yazdır
    imlec.execute(sorgu)
    return imlec.fetchall()

kullanici_girdisi = input("Kullanıcı adını girin: ")
sonuc = zafiyetli_giris_yap(kullanici_girdisi)

if sonuc:
    print("Kullanıcı bulundu:", sonuc)
else:
    print("Kullanıcı bulunamadı!")

baglanti.close()
