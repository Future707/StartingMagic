"""
    Script: 02_hesapMakinesi.py
    Açıklama: Gelişmiş hesap makinesi ve matematiksel işlemler uygulaması.
    Yazar: [Future Developer]
    Tarih: [03.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import math
import random

print("GELISMIS HESAP MAKINESI")
print("=" * 40)

# TEMEL HESAP MAKINESI
def temel_hesap_makinesi():
    print("\nTEMEL HESAP MAKINESI")
    print("-" * 25)
    
    try:
        sayi1 = float(input("İlk sayıyı girin: "))
        print("İşlemler: +, -, *, /, //, %, **")
        islem = input("İşlemi seçin: ").strip()
        sayi2 = float(input("İkinci sayıyı girin: "))
        
        if islem == '+':
            sonuc = sayi1 + sayi2
            print(f"Sonuç: {sayi1} + {sayi2} = {sonuc}")
        elif islem == '-':
            sonuc = sayi1 - sayi2
            print(f"Sonuç: {sayi1} - {sayi2} = {sonuc}")
        elif islem == '*':
            sonuc = sayi1 * sayi2
            print(f"Sonuç: {sayi1} * {sayi2} = {sonuc}")
        elif islem == '/':
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
                print(f"Sonuç: {sayi1} / {sayi2} = {sonuc:.4f}")
            else:
                print("HATA: Sıfıra bölme!")
        elif islem == '//':
            if sayi2 != 0:
                sonuc = sayi1 // sayi2
                print(f"Sonuç: {sayi1} // {sayi2} = {sonuc}")
            else:
                print("HATA: Sıfıra bölme!")
        elif islem == '%':
            if sayi2 != 0:
                sonuc = sayi1 % sayi2
                print(f"Sonuç: {sayi1} % {sayi2} = {sonuc}")
            else:
                print("HATA: Sıfıra bölme!")
        elif islem == '**':
            sonuc = sayi1 ** sayi2
            print(f"Sonuç: {sayi1} ** {sayi2} = {sonuc}")
        else:
            print("Geçersiz işlem!")
            
    except ValueError:
        print("HATA: Geçerli sayı girin!")

# BILIMSEL HESAP MAKINESI
def bilimsel_hesap_makinesi():
    print("\nBILIMSEL HESAP MAKINESI")
    print("-" * 30)
    
    try:
        print("1. Sin, Cos, Tan")
        print("2. Logaritma (ln, log10)")
        print("3. Karekök ve Faktöriyel")
        print("4. Derece/Radyan Dönüşümü")
        
        secim = int(input("Seçiminiz (1-4): "))
        
        if secim == 1:
            aci = float(input("Açıyı girin (derece): "))
            radyan = math.radians(aci)
            print(f"Sin({aci} derece) = {math.sin(radyan):.4f}")
            print(f"Cos({aci} derece) = {math.cos(radyan):.4f}")
            print(f"Tan({aci} derece) = {math.tan(radyan):.4f}")
            
        elif secim == 2:
            sayi = float(input("Sayıyı girin: "))
            if sayi > 0:
                print(f"ln({sayi}) = {math.log(sayi):.4f}")
                print(f"log10({sayi}) = {math.log10(sayi):.4f}")
            else:
                print("HATA: Logaritma için pozitif sayı gerekli!")
                
        elif secim == 3:
            sayi = float(input("Sayıyı girin: "))
            if sayi >= 0:
                print(f"Karekök({sayi}) = {math.sqrt(sayi):.4f}")
                if sayi == int(sayi) and 0 <= sayi <= 20:
                    print(f"{int(sayi)}! = {math.factorial(int(sayi))}")
                else:
                    print("Faktöriyel için 0-20 arası tam sayı gerekli!")
            else:
                print("HATA: Karekök için pozitif sayı gerekli!")
                
        elif secim == 4:
            print("1. Derece to Radyan")
            print("2. Radyan to Derece")
            tip = int(input("Seçim: "))
            deger = float(input("Değer: "))
            
            if tip == 1:
                radyan = math.radians(deger)
                print(f"{deger} derece = {radyan:.4f} radyan")
            elif tip == 2:
                derece = math.degrees(deger)
                print(f"{deger} radyan = {derece:.4f} derece")
                
    except ValueError:
        print("HATA: Geçerli bir değer girin!")
    except:
        print("HATA: Beklenmeyen hata!")

# SAYI TAHMIN OYUNU
def sayi_tahmin_oyunu():
    print("\nSAYI TAHMIN OYUNU")
    print("-" * 25)
    
    print("1. Kolay (1-10)")
    print("2. Orta (1-50)")
    print("3. Zor (1-100)")
    
    try:
        seviye = int(input("Zorluk seviyesi (1-3): "))
        
        if seviye == 1:
            max_sayi = 10
            max_deneme = 4
        elif seviye == 2:
            max_sayi = 50
            max_deneme = 6
        elif seviye == 3:
            max_sayi = 100
            max_deneme = 7
        else:
            print("Geçersiz seviye!")
            return
        
        gizli_sayi = random.randint(1, max_sayi)
        deneme = 0
        
        print(f"\n1-{max_sayi} arası bir sayı tuttum!")
        print(f"{max_deneme} deneme hakkınız var!")
        
        while deneme < max_deneme:
            try:
                tahmin = int(input(f"\nTahmin {deneme + 1}: "))
                deneme += 1
                
                if tahmin == gizli_sayi:
                    print(f"TEBRIKLER! {deneme} denemede buldunuz!")
                    print(f"Doğru cevap: {gizli_sayi}")
                    return
                elif tahmin < gizli_sayi:
                    print("Daha büyük bir sayı deneyin!")
                else:
                    print("Daha küçük bir sayı deneyin!")
                    
                if deneme < max_deneme:
                    print(f"Kalan deneme: {max_deneme - deneme}")
                    
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")
                deneme -= 1
        
        print(f"\nOyun bitti! Doğru cevap: {gizli_sayi}")
        
    except ValueError:
        print("Geçersiz seviye seçimi!")

# ISTATISTIK HESAPLAYICI
def istatistik_hesaplayici():
    print("\nISTATISTIK HESAPLAYICI")
    print("-" * 28)
    
    try:
        sayilar = []
        print("Sayıları girin (bitirmek için 'q' yazın):")
        
        while True:
            girdi = input("Sayı: ").strip()
            if girdi.lower() == 'q':
                break
            try:
                sayi = float(girdi)
                sayilar.append(sayi)
            except ValueError:
                print("Geçerli bir sayı girin veya çıkmak için 'q' yazın!")
        
        if not sayilar:
            print("Hiç sayı girilmedi!")
            return
        
        # İstatistikler
        toplam = sum(sayilar)
        ortalama = toplam / len(sayilar)
        minimum = min(sayilar)
        maksimum = max(sayilar)
        
        # Medyan hesaplama
        sirali = sorted(sayilar)
        n = len(sirali)
        if n % 2 == 0:
            medyan = (sirali[n//2 - 1] + sirali[n//2]) / 2
        else:
            medyan = sirali[n//2]
        
        # Standart sapma
        varyans = sum((x - ortalama) ** 2 for x in sayilar) / len(sayilar)
        std_sapma = math.sqrt(varyans)
        
        print(f"\nISTATISTIK SONUCLARI")
        print("-" * 20)
        print(f"Sayı adedi: {len(sayilar)}")
        print(f"Toplam: {toplam:.2f}")
        print(f"Ortalama: {ortalama:.2f}")
        print(f"Medyan: {medyan:.2f}")
        print(f"Minimum: {minimum:.2f}")
        print(f"Maksimum: {maksimum:.2f}")
        print(f"Standart Sapma: {std_sapma:.2f}")
        
    except Exception as e:
        print(f"Hata: {e}")

# MAIN PROGRAM
def main():
    while True:
        print("\n" + "="*40)
        print("HESAP MAKINESI - MENU")
        print("="*40)
        print("1. Temel Hesap Makinesi")
        print("2. Bilimsel Hesap Makinesi")
        print("3. Sayı Tahmin Oyunu")
        print("4. İstatistik Hesaplayıcı")
        print("5. Çıkış")
        
        try:
            secim = int(input("\nSeçiminiz (1-5): "))
            
            if secim == 1:
                temel_hesap_makinesi()
            elif secim == 2:
                bilimsel_hesap_makinesi()
            elif secim == 3:
                sayi_tahmin_oyunu()
            elif secim == 4:
                istatistik_hesaplayici()
            elif secim == 5:
                print("StartingMagic Python Eğitimine veda! Görüşürüz!")
                break
            else:
                print("Geçersiz seçim! Lütfen 1-5 arası bir sayı girin.")
                
            input("\nDevam etmek için Enter'a basın...")
            
        except ValueError:
            print("HATA: Lütfen geçerli bir sayı girin!")
            input("\nDevam etmek için Enter'a basın...")
        except KeyboardInterrupt:
            print("\nProgram sonlandırılıyor...")
            break

if __name__ == "__main__":
    main()