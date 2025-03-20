import sqlite3  

baglanti = sqlite3.connect("kullanicilar.db")
imlec = baglanti.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS kullanicilar (id INTEGER PRIMARY KEY, kullanici_adi TEXT, sifre TEXT)")

def guvenli_giris_yap(kullanici_adi):
    sorgu = "SELECT * FROM kullanicilar WHERE kullanici_adi = ?"
    imlec.execute(sorgu, (kullanici_adi,))
    return imlec.fetchall()

kullanici_girdisi = input("Kullanıcı adını girin: ")
sonuc = guvenli_giris_yap(kullanici_girdisi)

if sonuc:
    print("Kullanıcı bulundu:", sonuc)
else:
    print("Kullanıcı bulunamadı!")

baglanti.close()
