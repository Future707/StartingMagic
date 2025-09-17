"""
    Script: 06_arabaFiyatKıyas.py
    Açıklama: Araba fiyat analizi, karşılaştırma ve satın alma danışmanlık uygulaması.
    Yazar: [Future Developer]
    Tarih: [11.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import random
import math

print("ARABA FIYAT ANALIZI VE KARSILASTIRMA")
print("=" * 45)

class Araba:
    def __init__(self, marka, model, yil, km, yakit, fiyat, renk="Beyaz"):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.km = km
        self.yakit = yakit
        self.fiyat = fiyat
        self.renk = renk
        self.yas = 2025 - yil
    
    def __str__(self):
        return f"{self.yil} {self.marka} {self.model} - {self.km:,} km - {self.fiyat:,} TL"
    
    def deger_kaybı_hesapla(self):
        """Yıllık değer kaybını hesapla"""
        if self.yas == 0:
            return 0
        
        # Markaya göre değer kaybı oranları
        marka_oranlari = {
            "Toyota": 0.85,
            "Honda": 0.87,
            "BMW": 0.75,
            "Mercedes": 0.72,
            "Audi": 0.74,
            "Volkswagen": 0.80,
            "Ford": 0.78,
            "Renault": 0.76,
            "Fiat": 0.73,
            "Hyundai": 0.82
        }
        
        katsayi = marka_oranlari.get(self.marka, 0.78)
        return (1 - (katsayi ** self.yas)) * 100
    
    def yakit_tüketim_tahmini(self):
        """100 km'deki yakıt tüketimini tahmin et"""
        yakit_tüketimleri = {
            "Benzin": random.uniform(6.5, 9.5),
            "Dizel": random.uniform(4.5, 7.0),
            "Hybrid": random.uniform(3.5, 5.5),
            "Elektrik": random.uniform(15, 25)  # kWh/100km
        }
        return yakit_tüketimleri.get(self.yakit, 7.0)

# ARABA VERİTABANI
def araba_veritabani_olustur():
    """Örnek araba veritabanı oluştur"""
    markalar = ["Toyota", "Honda", "BMW", "Mercedes", "Audi", "Volkswagen", "Ford", "Renault", "Fiat", "Hyundai"]
    modeller = {
        "Toyota": ["Corolla", "Camry", "RAV4", "Prius"],
        "Honda": ["Civic", "Accord", "CR-V", "Jazz"],
        "BMW": ["3 Serisi", "5 Serisi", "X3", "X5"],
        "Mercedes": ["C-Class", "E-Class", "GLC", "A-Class"],
        "Audi": ["A3", "A4", "Q3", "Q5"],
        "Volkswagen": ["Golf", "Passat", "Tiguan", "Polo"],
        "Ford": ["Focus", "Fiesta", "Kuga", "Mondeo"],
        "Renault": ["Clio", "Megane", "Kadjar", "Captur"],
        "Fiat": ["Egea", "500", "Tipo", "Panda"],
        "Hyundai": ["i20", "Elantra", "Tucson", "i30"]
    }
    
    yakitlar = ["Benzin", "Dizel", "Hybrid", "Elektrik"]
    renkler = ["Beyaz", "Siyah", "Gri", "Mavi", "Kırmızı", "Gümüş"]
    
    arabalar = []
    
    for _ in range(50):
        marka = random.choice(markalar)
        model = random.choice(modeller[marka])
        yil = random.randint(2015, 2024)
        km = random.randint(5000, 200000)
        yakit = random.choice(yakitlar)
        renk = random.choice(renkler)
        
        # Fiyat hesaplama (basit algoritma)
        base_fiyat = random.randint(300000, 1500000)
        yas_faktoru = max(0.5, 1 - (2025 - yil) * 0.08)
        km_faktoru = max(0.3, 1 - km / 300000)
        
        fiyat = int(base_fiyat * yas_faktoru * km_faktoru)
        
        arabalar.append(Araba(marka, model, yil, km, yakit, fiyat, renk))
    
    return arabalar

# FİYAT ANALİZİ
def fiyat_analizi(arabalar):
    print("\nFIYAT ANALIZI")
    print("-" * 15)
    
    if not arabalar:
        print("Analiz için araba bulunamadı!")
        return
    
    fiyatlar = [araba.fiyat for araba in arabalar]
    
    print(f"Toplam araba sayısı: {len(arabalar)}")
    print(f"En düşük fiyat: {min(fiyatlar):,} TL")
    print(f"En yüksek fiyat: {max(fiyatlar):,} TL")
    print(f"Ortalama fiyat: {sum(fiyatlar) / len(fiyatlar):,.0f} TL")
    
    # Medyan hesaplama
    sirali_fiyatlar = sorted(fiyatlar)
    n = len(sirali_fiyatlar)
    if n % 2 == 0:
        medyan = (sirali_fiyatlar[n//2 - 1] + sirali_fiyatlar[n//2]) / 2
    else:
        medyan = sirali_fiyatlar[n//2]
    
    print(f"Medyan fiyat: {medyan:,.0f} TL")
    
    # Fiyat aralıkları
    araliklar = {
        "0-500K": len([f for f in fiyatlar if f < 500000]),
        "500K-1M": len([f for f in fiyatlar if 500000 <= f < 1000000]),
        "1M+": len([f for f in fiyatlar if f >= 1000000])
    }
    
    print("\nFIYAT DAGILIMI:")
    for aralik, sayi in araliklar.items():
        print(f"{aralik}: {sayi} araba ({sayi/len(arabalar)*100:.1f}%)")

# MARKA ANALİZİ
def marka_analizi(arabalar):
    print("\nMARKA ANALIZI")
    print("-" * 15)
    
    marka_sayilari = {}
    marka_fiyatlari = {}
    
    for araba in arabalar:
        marka = araba.marka
        
        if marka not in marka_sayilari:
            marka_sayilari[marka] = 0
            marka_fiyatlari[marka] = []
        
        marka_sayilari[marka] += 1
        marka_fiyatlari[marka].append(araba.fiyat)
    
    print("MARKA DAGILIMI:")
    for marka, sayi in sorted(marka_sayilari.items(), key=lambda x: x[1], reverse=True):
        ortalama = sum(marka_fiyatlari[marka]) / len(marka_fiyatlari[marka])
        print(f"{marka}: {sayi} araba - Ort: {ortalama:,.0f} TL")

# ARABA ARAMA
def araba_arama(arabalar):
    print("\nARABA ARAMA")
    print("-" * 12)
    
    print("Arama kriterleri:")
    marka = input("Marka (boş bırakabilirsiniz): ").strip().title()
    
    try:
        min_fiyat = int(input("Minimum fiyat (0 = sınırsız): ") or 0)
        max_fiyat = int(input("Maksimum fiyat (0 = sınırsız): ") or float('inf'))
        max_km = int(input("Maksimum KM (0 = sınırsız): ") or float('inf'))
        min_yil = int(input("Minimum yıl (0 = sınırsız): ") or 0)
    except ValueError:
        print("Geçersiz sayı formatı!")
        return
    
    # Filtreleme
    sonuclar = []
    for araba in arabalar:
        if (not marka or araba.marka == marka) and \
           (min_fiyat <= araba.fiyat <= max_fiyat) and \
           (araba.km <= max_km) and \
           (araba.yil >= min_yil):
            sonuclar.append(araba)
    
    print(f"\nARAMA SONUCU: {len(sonuclar)} araba bulundu")
    print("-" * 40)
    
    if sonuclar:
        for i, araba in enumerate(sonuclar[:10], 1):  # İlk 10 sonuç
            deger_kaybi = araba.deger_kaybı_hesapla()
            yakit_tuketimi = araba.yakit_tüketim_tahmini()
            
            print(f"{i}. {araba}")
            print(f"   Değer kaybı: %{deger_kaybi:.1f}")
            print(f"   Yakıt tüketimi: {yakit_tuketimi:.1f}L/100km")
            print(f"   Renk: {araba.renk}")
            print()
    else:
        print("Kriterlere uygun araba bulunamadı!")

# ARABA KARSILASTIRMA
def araba_karsilastirma(arabalar):
    print("\nARABA KARSILASTIRMA")
    print("-" * 20)
    
    if len(arabalar) < 2:
        print("Karşılaştırma için en az 2 araba gerekli!")
        return
    
    print("Karşılaştırılacak arabaları seçin:")
    for i, araba in enumerate(arabalar[:20], 1):
        print(f"{i}. {araba}")
    
    try:
        secim1 = int(input("\nİlk araba numarası: ")) - 1
        secim2 = int(input("İkinci araba numarası: ")) - 1
        
        if 0 <= secim1 < len(arabalar) and 0 <= secim2 < len(arabalar):
            araba1 = arabalar[secim1]
            araba2 = arabalar[secim2]
            
            print(f"\nKARSILASTIRMA SONUCU")
            print("=" * 25)
            
            kategoriler = [
                ("Marka-Model", f"{araba1.marka} {araba1.model}", f"{araba2.marka} {araba2.model}"),
                ("Yıl", araba1.yil, araba2.yil),
                ("KM", f"{araba1.km:,}", f"{araba2.km:,}"),
                ("Fiyat", f"{araba1.fiyat:,} TL", f"{araba2.fiyat:,} TL"),
                ("Yakıt Tipi", araba1.yakit, araba2.yakit),
                ("Değer Kaybı", f"%{araba1.deger_kaybı_hesapla():.1f}", f"%{araba2.deger_kaybı_hesapla():.1f}"),
                ("Yakıt Tüketimi", f"{araba1.yakit_tüketim_tahmini():.1f}L", f"{araba2.yakit_tüketim_tahmini():.1f}L")
            ]
            
            for kategori, deger1, deger2 in kategoriler:
                print(f"{kategori:<15}: {deger1:<20} vs {deger2}")
            
            # Öneri
            print(f"\nONERI SISTEMI:")
            puan1, puan2 = 0, 0
            
            # Fiyat karşılaştırması
            if araba1.fiyat < araba2.fiyat:
                puan1 += 2
                print("- Fiyat avantajı: Araba 1")
            elif araba2.fiyat < araba1.fiyat:
                puan2 += 2
                print("- Fiyat avantajı: Araba 2")
            
            # KM karşılaştırması
            if araba1.km < araba2.km:
                puan1 += 1
                print("- KM avantajı: Araba 1")
            elif araba2.km < araba1.km:
                puan2 += 1
                print("- KM avantajı: Araba 2")
            
            # Yaş karşılaştırması
            if araba1.yil > araba2.yil:
                puan1 += 1
                print("- Yaş avantajı: Araba 1")
            elif araba2.yil > araba1.yil:
                puan2 += 1
                print("- Yaş avantajı: Araba 2")
            
            if puan1 > puan2:
                print(f"\nSonuç: Araba 1 daha avantajlı! (Puan: {puan1}-{puan2})")
            elif puan2 > puan1:
                print(f"\nSonuç: Araba 2 daha avantajlı! (Puan: {puan2}-{puan1})")
            else:
                print(f"\nSonuç: Her iki araba da eşit avantajlı!")
        
    except (ValueError, IndexError):
        print("Geçersiz seçim!")

# YAKIT MALIYETİ HESAPLAYICI
def yakit_maliyet_hesapla():
    print("\nYAKIT MALIYET HESAPLAYICI")
    print("-" * 30)
    
    try:
        gunluk_km = float(input("Günlük KM: "))
        yakit_fiyati = float(input("Yakıt fiyatı (TL/Litre): "))
        tuketim = float(input("Yakıt tüketimi (L/100km): "))
        
        gunluk_maliyet = (gunluk_km * tuketim / 100) * yakit_fiyati
        aylik_maliyet = gunluk_maliyet * 30
        yillik_maliyet = gunluk_maliyet * 365
        
        print(f"\nMALIYET HESAPLARI:")
        print(f"Günlük yakıt maliyeti: {gunluk_maliyet:.2f} TL")
        print(f"Aylık yakıt maliyeti: {aylik_maliyet:.2f} TL")
        print(f"Yıllık yakıt maliyeti: {yillik_maliyet:.2f} TL")
        
        # 5 yıllık projeksiyon
        print(f"\n5 YILLIK PROJEKSIYON:")
        for yil in range(1, 6):
            toplam = yillik_maliyet * yil
            print(f"{yil} yıl: {toplam:,.0f} TL")
            
    except ValueError:
        print("Geçerli sayılar girin!")

# ANA PROGRAM
def main():
    print("Araba veritabanı hazırlanıyor...")
    arabalar = araba_veritabani_olustur()
    print(f"{len(arabalar)} araba yüklendi!")
    
    while True:
        print("\n" + "="*45)
        print("ARABA FIYAT ANALIZI VE KARSILASTIRMA")
        print("="*45)
        print("1. Fiyat Analizi")
        print("2. Marka Analizi")
        print("3. Araba Arama")
        print("4. Araba Karşılaştırma")
        print("5. Yakıt Maliyet Hesaplama")
        print("6. Yeni Araba Ekle")
        print("7. Çıkış")
        
        try:
            secim = int(input("\nSeçiminiz (1-7): "))
            
            if secim == 1:
                fiyat_analizi(arabalar)
            elif secim == 2:
                marka_analizi(arabalar)
            elif secim == 3:
                araba_arama(arabalar)
            elif secim == 4:
                araba_karsilastirma(arabalar)
            elif secim == 5:
                yakit_maliyet_hesapla()
            elif secim == 6:
                print("Yeni araba ekleme özelliği gelecek sürümde!")
            elif secim == 7:
                print("Araba dünyasından çıkılıyor!")
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