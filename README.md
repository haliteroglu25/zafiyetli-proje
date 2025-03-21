# zafiyetli-proje
Bu repo, güvenlik açıklarını test etmek için oluşturulmuştur.
# Zafiyetli GitHub Projesi

Bu projede bir SQL Injection güvenlik açığı ve düzeltilmiş versiyonu bulunmaktadır.

##  Zafiyetli Kod (zafiyetli_kod.py)
- **Zafiyet:** SQL Injection (OWASP A03:2021 - Injection)  
- **Zafiyetin CVSS Skoru:** 9.8 (Kritik)
- **Vector String:** CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Exploit Vektörü:** Kullanıcı girişine zararlı SQL kodları eklenebilir.  

##  Güvenli Kod (guvenli_kod.py)
- **Çözüm:** Parametreli sorgular kullanılarak SQL Injection önlenmiştir.  

## Demo Videosu
Aşağıdaki videoda zafiyetin nasıl istismar edildiği ve güvenli versiyonun nasıl çalıştığı gösterilmektedir.
https://youtu.be/vgASZQ0mLuY
