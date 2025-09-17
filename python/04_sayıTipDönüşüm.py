"""
    Script: 04_sayıTipDönüşüm.py
    Açıklama: Sayı tipleri, taban dönüşümleri ve matematiksel işlemler eğitimi.
    Yazar: [Future Developer]
    Tarih: [07.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import math
import random

print("SAYI TIPLERI VE DONUSUMLER")
print("=" * 35)

# SAYI TIPI ANALIZI
def sayi_tipi_analizi():
    print("\nSAYI TIPI ANALIZI")
    print("-" * 20)
    
    try:
        sayi = input("Bir sayı girin: ").strip()
        
        # Tip kontrolü
        if '.' in sayi:
            float_sayi = float(sayi)
            print(f"Girilen: {sayi}")
            print(f"Tip: Float (Ondalık Sayı)")
            print(f"Float değer: {float_sayi}")
            print(f"Tam kısmı: {int(float_sayi)}")
            print(f"Ondalık kısmı: {float_sayi - int(float_sayi):.6f}")
            
            # Kontrollar
            if float_sayi.is_integer():
                print("Bu sayı aslında tam sayıdır!")
            
        else:
            int_sayi = int(sayi)
            print(f"Girilen: {sayi}")
            print(f"Tip: Integer (Tam Sayı)")
            print(f"Değer: {int_sayi}")
            
            # Sayı özellikleri
            print(f"Pozitif mi: {'Evet' if int_sayi > 0 else 'Hayır'}")
            print(f"Negatif mi: {'Evet' if int_sayi < 0 else 'Hayır'}")
            print(f"Sıfır mı: {'Evet' if int_sayi == 0 else 'Hayır'}")
            print(f"Çift mi: {'Evet' if int_sayi % 2 == 0 else 'Hayır'}")
            print(f"Tek mi: {'Evet' if int_sayi % 2 == 1 else 'Hayır'}")
            
            # Matematiksel işlemler
            print(f"Mutlak değer: {abs(int_sayi)}")
            print(f"Karesi: {int_sayi ** 2}")
            if int_sayi >= 0:
                print(f"Karekökü: {math.sqrt(int_sayi):.4f}")
            
    except ValueError:
        print("Geçersiz sayı formatı!")

# TABAN DONUSUM SISTEMI
def taban_donusumu():
    print("\nTABAN DONUSUM SISTEMI")
    print("-" * 25)
    
    try:
        print("Hangi tabanda sayı giriyorsunuz?")
        print("1. Onluk (Decimal - 10)")
        print("2. İkilik (Binary - 2)")
        print("3. Sekizlik (Octal - 8)")
        print("4. Onaltılık (Hex - 16)")
        
        kaynak_taban = int(input("Kaynak taban (1-4): "))
        sayi_str = input("Sayıyı girin: ").strip().upper()
        
        # Kaynak tabandan onluk sisteme çevir
        if kaynak_taban == 1:  # Decimal
            decimal_sayi = int(sayi_str)
        elif kaynak_taban == 2:  # Binary
            decimal_sayi = int(sayi_str, 2)
        elif kaynak_taban == 3:  # Octal
            decimal_sayi = int(sayi_str, 8)
        elif kaynak_taban == 4:  # Hex
            decimal_sayi = int(sayi_str, 16)
        else:
            print("Geçersiz taban!")
            return
        
        print(f"\nDONUSUM SONUCLARI:")
        print("-" * 20)
        print(f"Onluk (Decimal): {decimal_sayi}")
        print(f"İkilik (Binary): {bin(decimal_sayi)}")
        print(f"Sekizlik (Octal): {oct(decimal_sayi)}")
        print(f"Onaltılık (Hex): {hex(decimal_sayi)}")
        
        # Ek bilgiler
        print(f"\nEK BILGILER:")
        print(f"Bit sayısı: {decimal_sayi.bit_length()}")
        print(f"Basamak sayısı: {len(str(decimal_sayi))}")
        
    except ValueError:
        print("Geçersiz sayı veya format!")

# ASCII KARAKTER DONUSUMLERI
def ascii_donusumleri():
    print("\nASCII KARAKTER DONUSUMLERI")
    print("-" * 30)
    
    print("1. Karakter -> ASCII Kodu")
    print("2. ASCII Kodu -> Karakter")
    print("3. Metin -> ASCII Kodları")
    
    try:
        secim = int(input("Seçiminiz (1-3): "))
        
        if secim == 1:
            karakter = input("Bir karakter girin: ")
            if len(karakter) == 1:
                ascii_kod = ord(karakter)
                print(f"'{karakter}' karakterinin ASCII kodu: {ascii_kod}")
                print(f"Binary: {bin(ascii_kod)}")
                print(f"Hex: {hex(ascii_kod)}")
            else:
                print("Lütfen tek karakter girin!")
                
        elif secim == 2:
            kod = int(input("ASCII kodu girin (0-127): "))
            if 0 <= kod <= 127:
                karakter = chr(kod)
                print(f"ASCII kod {kod} -> '{karakter}'")
            else:
                print("ASCII kodu 0-127 arasında olmalı!")
                
        elif secim == 3:
            metin = input("Metin girin: ")
            print("ASCII kodları:")
            for i, char in enumerate(metin):
                print(f"{char} -> {ord(char)}", end="  ")
                if (i + 1) % 5 == 0:  # Her 5 karakterde yeni satır
                    print()
            print()
            
    except ValueError:
        print("Geçerli bir seçim yapın!")

# RASTGELE SAYI URETICI
def rastgele_sayi_uretici():
    print("\nRASTGELE SAYI URETICI")
    print("-" * 25)
    
    print("1. Tek sayı üret")
    print("2. Sayı listesi üret")
    print("3. Float sayı üret")
    print("4. Normal dağılım")
    
    try:
        secim = int(input("Seçiminiz (1-4): "))
        
        if secim == 1:
            min_val = int(input("Minimum değer: "))
            max_val = int(input("Maksimum değer: "))
            sayi = random.randint(min_val, max_val)
            print(f"Rastgele sayı: {sayi}")
            
        elif secim == 2:
            adet = int(input("Kaç adet: "))
            min_val = int(input("Minimum değer: "))
            max_val = int(input("Maksimum değer: "))
            
            sayilar = [random.randint(min_val, max_val) for _ in range(adet)]
            print(f"Rastgele sayılar: {sayilar}")
            
            # İstatistikler
            print(f"Ortalama: {sum(sayilar) / len(sayilar):.2f}")
            print(f"En küçük: {min(sayilar)}")
            print(f"En büyük: {max(sayilar)}")
            
        elif secim == 3:
            min_val = float(input("Minimum değer: "))
            max_val = float(input("Maksimum değer: "))
            sayi = random.uniform(min_val, max_val)
            print(f"Rastgele float: {sayi:.6f}")
            
        elif secim == 4:
            ortalama = float(input("Ortalama: "))
            std_sapma = float(input("Standart sapma: "))
            adet = int(input("Kaç adet: "))
            
            sayilar = [random.gauss(ortalama, std_sapma) for _ in range(adet)]
            print(f"Normal dağılım sayıları: {[round(x, 2) for x in sayilar]}")
            
    except ValueError:
        print("Geçerli değerler girin!")

# MATEMATIKSEL SABITLER
def matematiksel_sabitler():
    print("\nMATEMATIKSEL SABITLER")
    print("-" * 25)
    
    sabitler = {
        "Pi (π)": math.pi,
        "Euler sayısı (e)": math.e,
        "Altın oran (φ)": (1 + math.sqrt(5)) / 2,
        "Karekök(2)": math.sqrt(2),
        "Log(2)": math.log(2),
        "Log(10)": math.log(10)
    }
    
    for isim, deger in sabitler.items():
        print(f"{isim}: {deger:.10f}")
    
    print(f"\nDAHA FAZLA BILGI:")
    print(f"Pi'nin 15 basamağı: {math.pi:.15f}")
    print(f"e'nin 15 basamağı: {math.e:.15f}")
    
    # Pi hesaplama yaklaşımı
    print(f"\nPI YAKLASIMI (Leibniz formülü):")
    pi_yaklasim = 0
    for i in range(100000):
        pi_yaklasim += ((-1)**i) / (2*i + 1)
    pi_yaklasim *= 4
    print(f"100,000 terimle: {pi_yaklasim:.10f}")
    print(f"Gerçek Pi: {math.pi:.10f}")
    print(f"Hata: {abs(math.pi - pi_yaklasim):.10f}")

# SAYI OYUNLARI
def sayi_oyunlari():
    print("\nSAYI OYUNLARI")
    print("-" * 15)
    
    print("1. Asal Sayı Kontrolü")
    print("2. Fibonacci Dizisi")
    print("3. Mükemmel Sayılar")
    print("4. Armstrong Sayılar")
    
    try:
        secim = int(input("Seçiminiz (1-4): "))
        
        if secim == 1:
            sayi = int(input("Sayı girin: "))
            
            def asal_mi(n):
                if n < 2:
                    return False
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        return False
                return True
            
            if asal_mi(sayi):
                print(f"{sayi} bir asal sayıdır!")
            else:
                print(f"{sayi} asal sayı değildir!")
                
            # İlk 20 asal sayı
            asallar = [i for i in range(2, 100) if asal_mi(i)][:20]
            print(f"İlk 20 asal: {asallar}")
            
        elif secim == 2:
            n = int(input("Kaç terim: "))
            fib = [0, 1]
            
            for i in range(2, n):
                fib.append(fib[i-1] + fib[i-2])
            
            print(f"İlk {n} Fibonacci sayısı:")
            print(fib[:n])
            
            # Altın oran yaklaşımı
            if n > 1:
                oran = fib[-1] / fib[-2]
                print(f"Son iki terimin oranı: {oran:.6f}")
                print(f"Altın oran: {(1 + math.sqrt(5)) / 2:.6f}")
                
        elif secim == 3:
            limit = int(input("Hangi sayıya kadar: "))
            mukemmeller = []
            
            for sayi in range(1, limit + 1):
                bolenlerin_toplami = sum(i for i in range(1, sayi) if sayi % i == 0)
                if bolenlerin_toplami == sayi:
                    mukemmeller.append(sayi)
            
            print(f"1-{limit} arası mükemmel sayılar: {mukemmeller}")
            
        elif secim == 4:
            limit = int(input("Hangi sayıya kadar: "))
            armstronglar = []
            
            for sayi in range(1, limit + 1):
                basamak_sayisi = len(str(sayi))
                toplam = sum(int(rakam) ** basamak_sayisi for rakam in str(sayi))
                if toplam == sayi:
                    armstronglar.append(sayi)
            
            print(f"1-{limit} arası Armstrong sayılar: {armstronglar}")
            
    except ValueError:
        print("Geçerli sayı girin!")

# ANA PROGRAM
def main():
    while True:
        print("\n" + "="*35)
        print("SAYI TIPLERI VE DONUSUMLER")
        print("="*35)
        print("1. Sayı Tipi Analizi")
        print("2. Taban Dönüşümü")
        print("3. ASCII Dönüşümleri")
        print("4. Rastgele Sayı Üretici")
        print("5. Matematiksel Sabitler")
        print("6. Sayı Oyunları")
        print("7. Çıkış")
        
        try:
            secim = int(input("\nSeçiminiz (1-7): "))
            
            if secim == 1:
                sayi_tipi_analizi()
            elif secim == 2:
                taban_donusumu()
            elif secim == 3:
                ascii_donusumleri()
            elif secim == 4:
                rastgele_sayi_uretici()
            elif secim == 5:
                matematiksel_sabitler()
            elif secim == 6:
                sayi_oyunlari()
            elif secim == 7:
                print("Sayı dünyasından çıkılıyor!")
                break
            else:
                print("Geçersiz seçim!")
                
            input("\nDevam için Enter'a basın...")
            
        except ValueError:
            print("Lütfen 1-7 arası sayı girin!")
        except KeyboardInterrupt:
            print("\nProgram sonlandırılıyor...")
            break

if __name__ == "__main__":
    main()