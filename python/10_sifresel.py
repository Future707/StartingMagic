"""
    Script: 10_sifresel.py
    Açıklama: Parola üretimi, güvenlik testi ve şifreleme araçları uygulaması.
    Yazar: [Future Developer]
    Tarih: [19.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import random
import string
import hashlib
import base64
import math

print("OTOMATIK PAROLA VE GUVENLIK ARACLARI")
print("=" * 42)

# PAROLA URETICI
def parola_uretici():
    print("\nPAROLA URETICI")
    print("-" * 16)
    
    try:
        uzunluk = int(input("Parola uzunluğu (6-50): "))
        if uzunluk < 6 or uzunluk > 50:
            uzunluk = 12
            print("Geçersiz uzunluk, 12 karaktere ayarlandı.")
        
        print("\nKarakter türleri:")
        print("1. Sadece harfler")
        print("2. Harfler + rakamlar")
        print("3. Harfler + rakamlar + semboller")
        print("4. Özel güvenli parola")
        
        secim = int(input("Seçiminiz (1-4): "))
        
        if secim == 1:
            karakterler = string.ascii_letters
        elif secim == 2:
            karakterler = string.ascii_letters + string.digits
        elif secim == 3:
            karakterler = string.ascii_letters + string.digits + "!@#$%^&*"
        elif secim == 4:
            # Güvenli parola: her türden en az 1 karakter
            parola = []
            parola.append(random.choice(string.ascii_lowercase))
            parola.append(random.choice(string.ascii_uppercase))
            parola.append(random.choice(string.digits))
            parola.append(random.choice("!@#$%^&*"))
            
            # Kalan karakterler
            tum_karakterler = string.ascii_letters + string.digits + "!@#$%^&*"
            for _ in range(uzunluk - 4):
                parola.append(random.choice(tum_karakterler))
            
            random.shuffle(parola)
            uretilen_parola = ''.join(parola)
            
            print(f"\nÜretilen güvenli parola: {uretilen_parola}")
            guvenlik_puani = parola_guvenlik_testi(uretilen_parola)
            print(f"Güvenlik puanı: {guvenlik_puani}/100")
            return
        else:
            karakterler = string.ascii_letters + string.digits
        
        uretilen_parola = ''.join(random.choice(karakterler) for _ in range(uzunluk))
        
        print(f"\nÜretilen parola: {uretilen_parola}")
        
        # Güvenlik değerlendirmesi
        guvenlik_puani = parola_guvenlik_testi(uretilen_parola)
        print(f"Güvenlik puanı: {guvenlik_puani}/100")
        
    except ValueError:
        print("Geçerli bir sayı girin!")

# PAROLA GUVENLIK TESTI
def parola_guvenlik_testi(parola=None):
    print("\nPAROLA GUVENLIK TESTI")
    print("-" * 22)
    
    if parola is None:
        parola = input("Test edilecek parolayı girin: ")
    
    puan = 0
    oneriler = []
    
    # Uzunluk kontrolü
    uzunluk = len(parola)
    if uzunluk >= 12:
        puan += 25
    elif uzunluk >= 8:
        puan += 15
        oneriler.append("Parolayı 12+ karakter yapın")
    else:
        puan += 5
        oneriler.append("Parola çok kısa! En az 8 karakter olmalı")
    
    # Karakter çeşitliliği
    has_lower = any(c.islower() for c in parola)
    has_upper = any(c.isupper() for c in parola)
    has_digit = any(c.isdigit() for c in parola)
    has_symbol = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in parola)
    
    cesitlilik_puani = sum([has_lower, has_upper, has_digit, has_symbol]) * 15
    puan += cesitlilik_puani
    
    if not has_lower:
        oneriler.append("Küçük harf ekleyin")
    if not has_upper:
        oneriler.append("Büyük harf ekleyin")
    if not has_digit:
        oneriler.append("Rakam ekleyin")
    if not has_symbol:
        oneriler.append("Özel karakter ekleyin (!@#$%^&*)")
    
    # Yaygın parolalar kontrolü
    yaygın_parolalar = ["123456", "password", "123456789", "12345678", "12345", 
                       "qwerty", "abc123", "password123", "admin", "letmein"]
    
    if parola.lower() in yaygın_parolalar:
        puan -= 30
        oneriler.append("Bu parola çok yaygın! Farklı bir parola seçin")
    
    # Tekrar eden karakterler
    for i in range(len(parola) - 2):
        if parola[i] == parola[i+1] == parola[i+2]:
            puan -= 10
            oneriler.append("Üst üste aynı karakter kullanmayın")
            break
    
    # Ardışık karakterler
    for i in range(len(parola) - 2):
        if ord(parola[i+1]) == ord(parola[i]) + 1 == ord(parola[i+2]) - 1:
            puan -= 5
            oneriler.append("Ardışık karakterlerden kaçının (abc, 123)")
            break
    
    puan = max(0, min(100, puan))
    
    print(f"PAROLA: {parola}")
    print(f"UZUNLUK: {uzunluk} karakter")
    print(f"GUVENLIK PUANI: {puan}/100")
    
    if puan >= 80:
        seviye = "ÇOK GÜÇLÜ"
        renk = "🟢"
    elif puan >= 60:
        seviye = "GÜÇLÜ"
        renk = "🟡"
    elif puan >= 40:
        seviye = "ORTA"
        renk = "🟠"
    else:
        seviye = "ZAYIF"
        renk = "🔴"
    
    print(f"SEVİYE: {renk} {seviye}")
    
    if oneriler:
        print(f"\nÖNERİLER:")
        for oneri in oneriler[:3]:  # En fazla 3 öneri göster
            print(f"- {oneri}")
    
    # Kırılma süresi tahmini
    karakter_havuzu = 0
    if has_lower:
        karakter_havuzu += 26
    if has_upper:
        karakter_havuzu += 26
    if has_digit:
        karakter_havuzu += 10
    if has_symbol:
        karakter_havuzu += 20
    
    if karakter_havuzu > 0:
        kombinasyon = karakter_havuzu ** uzunluk
        saniye_tahmini = kombinasyon / (1000000000)  # 1 milyar deneme/saniye
        
        if saniye_tahmini < 60:
            sure_str = f"{saniye_tahmini:.1f} saniye"
        elif saniye_tahmini < 3600:
            sure_str = f"{saniye_tahmini/60:.1f} dakika"
        elif saniye_tahmini < 86400:
            sure_str = f"{saniye_tahmini/3600:.1f} saat"
        elif saniye_tahmini < 31536000:
            sure_str = f"{saniye_tahmini/86400:.1f} gün"
        else:
            sure_str = f"{saniye_tahmini/31536000:.1f} yıl"
        
        print(f"KIRMA SÜRESİ TAHMİNİ: {sure_str}")
    
    return puan

# METIN SIFRELEME
def metin_sifreleme():
    print("\nMETİN ŞİFRELEME")
    print("-" * 17)
    
    print("1. Caesar Şifresi (Basit)")
    print("2. Base64 Kodlama")
    print("3. ROT13 Şifresi")
    print("4. Ters Çevirme")
    
    try:
        secim = int(input("Şifreleme türü (1-4): "))
        metin = input("Şifrelenecek metin: ")
        
        if secim == 1:  # Caesar
            kaydirma = int(input("Kaydırma miktarı (1-25): "))
            sifrelenmis = ""
            
            for char in metin:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    shifted = (ord(char) - base + kaydirma) % 26
                    sifrelenmis += chr(base + shifted)
                else:
                    sifrelenmis += char
            
            print(f"Şifrelenmiş: {sifrelenmis}")
            
        elif secim == 2:  # Base64
            metin_bytes = metin.encode('utf-8')
            sifrelenmis = base64.b64encode(metin_bytes).decode('utf-8')
            print(f"Base64: {sifrelenmis}")
            
        elif secim == 3:  # ROT13
            sifrelenmis = ""
            for char in metin:
                if char.isalpha():
                    base = ord('A') if char.isupper() else ord('a')
                    shifted = (ord(char) - base + 13) % 26
                    sifrelenmis += chr(base + shifted)
                else:
                    sifrelenmis += char
            
            print(f"ROT13: {sifrelenmis}")
            
        elif secim == 4:  # Ters çevirme
            sifrelenmis = metin[::-1]
            print(f"Ters: {sifrelenmis}")
            
    except ValueError:
        print("Geçerli değerler girin!")

# HASH HESAPLAMA
def hash_hesaplama():
    print("\nHASH HESAPLAMA")
    print("-" * 16)
    
    metin = input("Hash hesaplanacak metin: ")
    
    # Farklı hash algoritmalarını hesapla
    md5_hash = hashlib.md5(metin.encode()).hexdigest()
    sha1_hash = hashlib.sha1(metin.encode()).hexdigest()
    sha256_hash = hashlib.sha256(metin.encode()).hexdigest()
    
    print(f"\nHASH SONUÇLARI:")
    print(f"Orijinal: {metin}")
    print(f"MD5:      {md5_hash}")
    print(f"SHA1:     {sha1_hash}")
    print(f"SHA256:   {sha256_hash}")
    
    print(f"\nHASH BİLGİLERİ:")
    print(f"MD5 uzunluğu: {len(md5_hash)} karakter")
    print(f"SHA1 uzunluğu: {len(sha1_hash)} karakter")
    print(f"SHA256 uzunluğu: {len(sha256_hash)} karakter")

# GUVENLIK IPUCLARI
def guvenlik_ipuclari():
    print("\nDİJİTAL GÜVENLİK İPUÇLARI")
    print("-" * 28)
    
    ipuclari = [
        "Her hesap için farklı parola kullanın",
        "2FA (iki faktörlü kimlik doğrulama) aktifleştirin",
        "Parolalarınızı düzenli olarak değiştirin",
        "Parola yöneticisi kullanın",
        "Şüpheli e-postaları açmayın",
        "Güvenlik güncellemelerini ihmal etmeyin",
        "Halka açık WiFi'de hassas işlemler yapmayın",
        "Sosyal medya paylaşımlarınıza dikkat edin",
        "Yedekleme alın ve güvenli saklayın",
        "Antivirüs programı kullanın"
    ]
    
    kategoriler = {
        "Parola Güvenliği": ipuclari[:4],
        "Genel Güvenlik": ipuclari[4:7],
        "Veri Güvenliği": ipuclari[7:]
    }
    
    for kategori, ipuc_listesi in kategoriler.items():
        print(f"\n{kategori.upper()}:")
        for i, ipuc in enumerate(ipuc_listesi, 1):
            print(f"  {i}. {ipuc}")

# PAROLA YONETIMI
def parola_yonetimi():
    print("\nPAROLA YÖNETİMİ REHBERİ")
    print("-" * 26)
    
    print("PAROLA OLUŞTURMA KURALLARI:")
    kurallar = [
        "En az 12 karakter uzunluğunda olsun",
        "Büyük-küçük harf, rakam ve sembol içersin",
        "Yaygın kelimeler kullanmayın",
        "Kişisel bilgiler (doğum tarihi, isim) eklemeyin",
        "Farklı hesaplar için farklı parolalar kullanın"
    ]
    
    for i, kural in enumerate(kurallar, 1):
        print(f"  {i}. {kural}")
    
    print(f"\nPAROLA SAKLAMA YÖNTEMLERİ:")
    yontemler = [
        ("Parola Yöneticisi", "En güvenli yöntem, otomatik üretim ve saklama"),
        ("Fiziksel Not", "Güvenli bir yerde saklanan yazılı notlar"),
        ("Mnemonik Teknik", "Unutamayacağınız cümlelerden parola türetme"),
        ("Kalıp Yöntemi", "Her site için temel kalıbı değiştirme")
    ]
    
    for yontem, aciklama in yontemler:
        print(f"• {yontem}: {aciklama}")
    
    print(f"\nPAROLA TEST ÖRNEKLERİ:")
    ornekler = [
        ("zayıf", "123456"),
        ("orta", "Parola123"),
        ("güçlü", "M3n!mG4v3nl!P@r0l@m")
    ]
    
    for seviye, ornek in ornekler:
        puan = parola_guvenlik_testi(ornek)
        print(f"• {seviye.capitalize()}: '{ornek}' - {puan}/100 puan")

# GUVENLIK QUIZ
def guvenlik_quiz():
    print("\nDİJİTAL GÜVENLİK QUIZ")
    print("-" * 23)
    
    sorular = [
        ("Güvenli parola uzunluğu minimum kaç karakter olmalı?", ["6", "8", "12", "16"], 2),
        ("2FA ne anlama gelir?", ["Two Factor Authentication", "Two File Access", "Total File Authority", "Time Factor Auth"], 0),
        ("Hangi hash algoritması daha güvenlidir?", ["MD5", "SHA1", "SHA256", "CRC32"], 2),
        ("Phishing saldırısı nedir?", ["Virüs", "Sahte e-posta", "Şifre kırma", "Sistem hack"], 1),
        ("En güvenli parola saklama yöntemi?", ["Tarayıcı", "Metin dosyası", "Parola yöneticisi", "Kağıda yazma"], 2)
    ]
    
    dogru_cevap = 0
    
    for i, (soru, secenekler, dogru_idx) in enumerate(sorular, 1):
        print(f"\nSoru {i}: {soru}")
        for j, secenek in enumerate(secenekler):
            print(f"   {j+1}. {secenek}")
        
        try:
            cevap = int(input("Cevabınız (1-4): ")) - 1
            if cevap == dogru_idx:
                print("✓ Doğru!")
                dogru_cevap += 1
            else:
                print(f"✗ Yanlış! Doğru cevap: {secenekler[dogru_idx]}")
        except ValueError:
            print(f"✗ Geçersiz seçim! Doğru cevap: {secenekler[dogru_idx]}")
    
    yuzde = (dogru_cevap / len(sorular)) * 100
    print(f"\nQUIZ SONUCU: {dogru_cevap}/{len(sorular)} ({yuzde:.0f}%)")
    
    if yuzde >= 80:
        print("🟢 Mükemmel! Güvenlik bilginiz çok iyi.")
    elif yuzde >= 60:
        print("🟡 İyi! Güvenlik konularını takip ediyorsunuz.")
    else:
        print("🔴 Dikkat! Güvenlik bilginizi geliştirmelisiniz.")

# ANA PROGRAM
def main():
    while True:
        print("\n" + "="*42)
        print("OTOMATIK PAROLA VE GUVENLIK ARACLARI")
        print("="*42)
        print("1. Parola Üretici")
        print("2. Parola Güvenlik Testi")
        print("3. Metin Şifreleme")
        print("4. Hash Hesaplama")
        print("5. Güvenlik İpuçları")
        print("6. Parola Yönetimi Rehberi")
        print("7. Güvenlik Quiz")
        print("8. Çıkış")
        
        try:
            secim = int(input("\nSeçiminiz (1-8): "))
            
            if secim == 1:
                parola_uretici()
            elif secim == 2:
                parola_guvenlik_testi()
            elif secim == 3:
                metin_sifreleme()
            elif secim == 4:
                hash_hesaplama()
            elif secim == 5:
                guvenlik_ipuclari()
            elif secim == 6:
                parola_yonetimi()
            elif secim == 7:
                guvenlik_quiz()
            elif secim == 8:
                print("Güvenlik araçlarından çıkılıyor!")
                break
            else:
                print("Geçersiz seçim!")
                
            input("\nDevam için Enter'a basın...")
            
        except ValueError:
            print("Lütfen 1-8 arası sayı girin!")
        except KeyboardInterrupt:
            print("\nProgram sonlandırılıyor...")
            break

if __name__ == "__main__":
    main()