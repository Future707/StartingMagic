"""
    Script: 01_pythonGramerimsi.py
    Açıklama: Python'da temel veri tipleri, değişkenler ve operatörler öğretimi.
    Yazar: [Future Developer]
    Tarih: [01.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import math
import datetime

print("PYTHON TEMELLERI VE DEGISKENLER")
print("=" * 50)

# VERI TIPLERI OGRENME MODULU
def veri_tipleri_ogret():
    print("\nVERI TIPLERI DERSI")
    print("-" * 25)
    
    # String (Metin)
    isim = "StartingMagic"
    print(f"String: {isim} - Tip: {type(isim)}")
    
    # Integer (Tam Sayı)
    yas = 25
    print(f"Integer: {yas} - Tip: {type(yas)}")
    
    # Float (Ondalık Sayı)
    boy = 1.75
    print(f"Float: {boy} - Tip: {type(boy)}")
    
    # Boolean (Doğru/Yanlış)
    aktif_mi = True
    print(f"Boolean: {aktif_mi} - Tip: {type(aktif_mi)}")
    
    # List (Liste)
    hobiler = ["kodlama", "müzik", "spor"]
    print(f"List: {hobiler} - Tip: {type(hobiler)}")
    
    return isim, yas, boy, aktif_mi, hobiler

# OPERATORLER TESTI
def operatorler_testi():
    print("\nOPERATORLER TESTI")
    print("-" * 20)
    
    try:
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        
        print(f"\nSONUCLAR:")
        print(f"Toplama: {sayi1} + {sayi2} = {sayi1 + sayi2}")
        print(f"Çıkarma: {sayi1} - {sayi2} = {sayi1 - sayi2}")
        print(f"Çarpma: {sayi1} * {sayi2} = {sayi1 * sayi2}")
        
        if sayi2 != 0:
            print(f"Bölme: {sayi1} / {sayi2} = {sayi1 / sayi2:.2f}")
            print(f"Tam Bölme: {sayi1} // {sayi2} = {sayi1 // sayi2}")
            print(f"Mod (Kalan): {sayi1} % {sayi2} = {sayi1 % sayi2}")
        else:
            print("Bölme: Sıfıra bölme hatası!")
        
        print(f"Üs Alma: {sayi1} ** {sayi2} = {sayi1 ** sayi2}")
        
    except ValueError:
        print("HATA: Lütfen geçerli bir sayı girin!")

# KISISEL BILGI TOPLAYICI
def kisisel_bilgi_toplayici():
    print("\nKISISEL BILGI TOPLAYICI")
    print("-" * 30)
    
    bilgiler = {}
    
    try:
        bilgiler['isim'] = input("Adınız: ").strip()
        bilgiler['soyisim'] = input("Soyadınız: ").strip()
        bilgiler['yas'] = int(input("Yaşınız: "))
        bilgiler['meslek'] = input("Mesleğiniz: ").strip()
        bilgiler['sehir'] = input("Şehriniz: ").strip()
        
        print(f"\nBILGILERINIZ KAYIT EDILDI")
        print("-" * 35)
        print(f"Ad Soyad: {bilgiler['isim']} {bilgiler['soyisim']}")
        print(f"Yaş: {bilgiler['yas']}")
        print(f"Meslek: {bilgiler['meslek']}")
        print(f"Şehir: {bilgiler['sehir']}")
        
        # Yaş analizi
        if bilgiler['yas'] < 18:
            kategori = "Genç"
        elif bilgiler['yas'] < 65:
            kategori = "Yetişkin"
        else:
            kategori = "Yaşlı"
        
        print(f"Kategori: {kategori}")
        
        # Doğum yılı hesaplama
        dogum_yili = datetime.datetime.now().year - bilgiler['yas']
        print(f"Tahmini Doğum Yılı: {dogum_yili}")
        
    except ValueError:
        print("HATA: Yaş için geçerli bir sayı girin!")

# STRING MANIPULASYON OYUNU
def string_oyunu():
    print("\nSTRING MANIPULASYON OYUNU")
    print("-" * 35)
    
    cumle = input("Bir cümle yazın: ").strip()
    
    if not cumle:
        print("Boş cümle giremezsiniz!")
        return
    
    print(f"\nORIJINAL: {cumle}")
    print(f"BUYUK HARF: {cumle.upper()}")
    print(f"kucuk harf: {cumle.lower()}")
    print(f"Ilk Harf Buyuk: {cumle.title()}")
    print(f"Ters Cevrilmis: {cumle[::-1]}")
    print(f"Karakter Sayısı: {len(cumle)}")
    print(f"Kelime Sayısı: {len(cumle.split())}")
    
    # Sesli harf sayma
    sesli_harfler = "aeiouAEIOU"
    sesli_sayi = sum(1 for harf in cumle if harf in sesli_harfler)
    print(f"Sesli Harf Sayısı: {sesli_sayi}")

# MAIN PROGRAM
def main():
    while True:
        print("\n" + "="*50)
        print("PYTHON TEMELLERI - MENU")
        print("="*50)
        print("1. Veri Tiplerini Ogren")
        print("2. Operatorler Testi")
        print("3. Kisisel Bilgi Toplayici")
        print("4. String Oyunu")
        print("5. Cikis")
        
        try:
            secim = int(input("\nSeçiminiz (1-5): "))
            
            if secim == 1:
                veri_tipleri_ogret()
            elif secim == 2:
                operatorler_testi()
            elif secim == 3:
                kisisel_bilgi_toplayici()
            elif secim == 4:
                string_oyunu()
            elif secim == 5:
                print("StartingMagic Python Egitimine veda! Gorusuruz!")
                break
            else:
                print("Gecersiz secim! Lutfen 1-5 arası bir sayı girin.")
                
            input("\nDevam etmek için Enter'a basın...")
            
        except ValueError:
            print("HATA: Lütfen geçerli bir sayı girin!")
            input("\nDevam etmek için Enter'a basın...")
        except KeyboardInterrupt:
            print("\nProgram sonlandırılıyor...")
            break

if __name__ == "__main__":
    main()