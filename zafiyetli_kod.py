import sqlite3

conn = sqlite3.connect('kullanici_veritabani.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS kullanicilar (
    id INTEGER PRIMARY KEY,
    kullanici_adi TEXT,
    sifre TEXT
)
''')

cursor.execute("INSERT INTO kullanicilar (kullanici_adi, sifre) VALUES ('admin', 'admin123')")
conn.commit()

def kullanici_giris():
    kullanici_adi = input("Kullanıcı adını girin: ")
    sifre = input("Şifreyi girin: ")

    query = f"SELECT * FROM kullanicilar WHERE kullanici_adi = '{kullanici_adi}' AND sifre = '{sifre}'"
    cursor.execute(query)

    if cursor.fetchone():
        print("Giriş başarılı!")
    else:
        print("Kullanıcı bulunamadı!")

kullanici_giris()

conn.close()
