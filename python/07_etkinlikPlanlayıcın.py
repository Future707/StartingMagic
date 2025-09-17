"""
    Script: 07_etkinlikPlanlayıcın.py
    Açıklama: Etkinlik planlama, takip ve yönetim uygulaması.
    Yazar: [Future Developer]
    Tarih: [13.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import datetime
import random

print("ETKINLIK YONETIMI VE PLANLAMA")
print("=" * 35)

class Etkinlik:
    def __init__(self, ad, tarih, saat, yer, katilimci_sayisi=0):
        self.ad = ad
        self.tarih = tarih
        self.saat = saat
        self.yer = yer
        self.katilimci_sayisi = katilimci_sayisi
        self.durum = "Planlandı"
        self.katilimcilar = []
        self.maliyet = 0
        
    def __str__(self):
        return f"{self.ad} - {self.tarih} {self.saat} - {self.yer}"

etkinlikler = []

# ETKINLIK EKLEME
def etkinlik_ekle():
    print("\nYENI ETKINLIK EKLEME")
    print("-" * 22)
    
    ad = input("Etkinlik adı: ").strip()
    if not ad:
        print("Etkinlik adı boş olamaz!")
        return
    
    try:
        tarih_str = input("Tarih (GG.AA.YYYY): ")
        gun, ay, yil = map(int, tarih_str.split('.'))
        tarih = datetime.date(yil, ay, gun)
        
        saat = input("Saat (SS:DD): ")
        yer = input("Yer: ").strip()
        katilimci_sayisi = int(input("Beklenen katılımcı sayısı: ") or 0)
        
        etkinlik = Etkinlik(ad, tarih, saat, yer, katilimci_sayisi)
        etkinlikler.append(etkinlik)
        
        print(f"'{ad}' etkinliği başarıyla eklendi!")
        
    except ValueError:
        print("Geçersiz tarih veya sayı formatı!")

# ETKINLIK LISTELEME
def etkinlik_listele():
    print("\nETKINLIK LISTESI")
    print("-" * 18)
    
    if not etkinlikler:
        print("Hiç etkinlik bulunamadı!")
        return
    
    # Tarihe göre sırala
    sirali_etkinlikler = sorted(etkinlikler, key=lambda e: e.tarih)
    
    for i, etkinlik in enumerate(sirali_etkinlikler, 1):
        kalan_gun = (etkinlik.tarih - datetime.date.today()).days
        durum_icon = "🟢" if kalan_gun > 7 else "🟡" if kalan_gun > 0 else "🔴"
        
        print(f"{i}. {etkinlik}")
        print(f"   Durum: {etkinlik.durum} {durum_icon}")
        print(f"   Katılımcı: {len(etkinlik.katilimcilar)}/{etkinlik.katilimci_sayisi}")
        print(f"   Kalan gün: {kalan_gun}")
        print()

# KATILIMCI YONETIMI
def katilimci_yonetimi():
    print("\nKATILIMCI YONETIMI")
    print("-" * 20)
    
    if not etkinlikler:
        print("Önce etkinlik eklemelisiniz!")
        return
    
    print("Etkinlikler:")
    for i, etkinlik in enumerate(etkinlikler, 1):
        print(f"{i}. {etkinlik.ad}")
    
    try:
        secim = int(input("Etkinlik seçin: ")) - 1
        if 0 <= secim < len(etkinlikler):
            etkinlik = etkinlikler[secim]
            
            print(f"\n{etkinlik.ad} - Katılımcı İşlemleri")
            print("1. Katılımcı Ekle")
            print("2. Katılımcıları Listele")
            print("3. Katılımcı Sil")
            
            islem = int(input("Seçiminiz: "))
            
            if islem == 1:
                ad_soyad = input("Katılımcı adı soyadı: ").strip()
                email = input("E-mail: ").strip()
                telefon = input("Telefon: ").strip()
                
                katilimci = {
                    "ad_soyad": ad_soyad,
                    "email": email,
                    "telefon": telefon,
                    "kayit_tarihi": datetime.date.today()
                }
                
                etkinlik.katilimcilar.append(katilimci)
                print("Katılımcı eklendi!")
                
            elif islem == 2:
                if etkinlik.katilimcilar:
                    for i, k in enumerate(etkinlik.katilimcilar, 1):
                        print(f"{i}. {k['ad_soyad']} - {k['email']}")
                else:
                    print("Henüz katılımcı yok!")
                    
            elif islem == 3:
                if etkinlik.katilimcilar:
                    for i, k in enumerate(etkinlik.katilimcilar, 1):
                        print(f"{i}. {k['ad_soyad']}")
                    
                    sil_idx = int(input("Silinecek katılımcı: ")) - 1
                    if 0 <= sil_idx < len(etkinlik.katilimcilar):
                        silinen = etkinlik.katilimcilar.pop(sil_idx)
                        print(f"{silinen['ad_soyad']} silindi!")
                else:
                    print("Silinecek katılımcı yok!")
                    
    except (ValueError, IndexError):
        print("Geçersiz seçim!")

# ETKINLIK TAKVIMI
def etkinlik_takvimi():
    print("\nETKINLIK TAKVIMI")
    print("-" * 18)
    
    if not etkinlikler:
        print("Hiç etkinlik bulunamadı!")
        return
    
    # Bu ay ve gelecek ay
    bugun = datetime.date.today()
    
    print("BU AYKI ETKINLIKLER:")
    bu_ay_etkinlikler = [e for e in etkinlikler if e.tarih.month == bugun.month and e.tarih.year == bugun.year]
    
    if bu_ay_etkinlikler:
        for etkinlik in sorted(bu_ay_etkinlikler, key=lambda e: e.tarih):
            print(f"- {etkinlik.tarih.day:2d}. gün: {etkinlik.ad}")
    else:
        print("Bu ay etkinlik yok.")
    
    # Yaklaşan etkinlikler
    print("\nYAKLASAN ETKINLIKLER (7 gün):")
    yaklasan = [e for e in etkinlikler if 0 <= (e.tarih - bugun).days <= 7]
    
    if yaklasan:
        for etkinlik in sorted(yaklasan, key=lambda e: e.tarih):
            kalan = (etkinlik.tarih - bugun).days
            print(f"- {kalan} gün kaldı: {etkinlik.ad}")
    else:
        print("Yaklaşan etkinlik yok.")

# ETKINLIK ISTATISTIKLERI
def etkinlik_istatistikleri():
    print("\nETKINLIK ISTATISTIKLERI")
    print("-" * 25)
    
    if not etkinlikler:
        print("İstatistik için etkinlik gerekli!")
        return
    
    toplam_etkinlik = len(etkinlikler)
    toplam_katilimci = sum(len(e.katilimcilar) for e in etkinlikler)
    
    # Durum istatistikleri
    durum_sayilari = {}
    for etkinlik in etkinlikler:
        durum = etkinlik.durum
        durum_sayilari[durum] = durum_sayilari.get(durum, 0) + 1
    
    # Yer istatistikleri
    yer_sayilari = {}
    for etkinlik in etkinlikler:
        yer = etkinlik.yer
        yer_sayilari[yer] = yer_sayilari.get(yer, 0) + 1
    
    print(f"Toplam etkinlik: {toplam_etkinlik}")
    print(f"Toplam katılımcı: {toplam_katilimci}")
    print(f"Ortalama katılımcı/etkinlik: {toplam_katilimci/toplam_etkinlik:.1f}")
    
    print(f"\nDURUM DAGILIMI:")
    for durum, sayi in durum_sayilari.items():
        print(f"- {durum}: {sayi}")
    
    print(f"\nPOPULER YERLER:")
    for yer, sayi in sorted(yer_sayilari.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"- {yer}: {sayi} etkinlik")

# ETKINLIK SABLONLARI
def etkinlik_sablonlari():
    print("\nETKINLIK SABLONLARI")
    print("-" * 21)
    
    sablonlar = {
        "Doğum Günü": {
            "yer": "Ev/Restoran",
            "katilimci": 15,
            "maliyet": 500
        },
        "İş Toplantısı": {
            "yer": "Ofis/Toplantı Salonu",
            "katilimci": 10,
            "maliyet": 200
        },
        "Düğün": {
            "yer": "Düğün Salonu",
            "katilimci": 200,
            "maliyet": 15000
        },
        "Konser": {
            "yer": "Konser Salonu",
            "katilimci": 500,
            "maliyet": 25000
        },
        "Workshop": {
            "yer": "Eğitim Merkezi",
            "katilimci": 25,
            "maliyet": 1000
        }
    }
    
    print("Mevcut şablonlar:")
    for i, (ad, bilgi) in enumerate(sablonlar.items(), 1):
        print(f"{i}. {ad}")
        print(f"   Önerilen yer: {bilgi['yer']}")
        print(f"   Ortalama katılımcı: {bilgi['katilimci']}")
        print(f"   Tahmini maliyet: {bilgi['maliyet']} TL")
        print()
    
    try:
        secim = int(input("Şablon seçin (0=İptal): "))
        if 1 <= secim <= len(sablonlar):
            sablon_adi = list(sablonlar.keys())[secim - 1]
            sablon = sablonlar[sablon_adi]
            
            print(f"\n{sablon_adi} şablonu seçildi!")
            ad = input(f"Etkinlik adı ({sablon_adi}): ").strip() or sablon_adi
            
            # Tarih alma
            tarih_str = input("Tarih (GG.AA.YYYY): ")
            gun, ay, yil = map(int, tarih_str.split('.'))
            tarih = datetime.date(yil, ay, gun)
            
            saat = input("Saat (SS:DD): ")
            yer = input(f"Yer ({sablon['yer']}): ").strip() or sablon['yer']
            
            etkinlik = Etkinlik(ad, tarih, saat, yer, sablon['katilimci'])
            etkinlik.maliyet = sablon['maliyet']
            etkinlikler.append(etkinlik)
            
            print(f"'{ad}' şablondan oluşturuldu!")
            
    except (ValueError, IndexError):
        print("Geçersiz seçim!")

# ANA PROGRAM
def main():
    # Örnek etkinlikler ekle
    ornek_etkinlikler = [
        Etkinlik("Python Eğitimi", datetime.date(2025, 7, 20), "14:00", "Online", 30),
        Etkinlik("Yıl Sonu Partisi", datetime.date(2025, 12, 31), "20:00", "Otel Ballroom", 100)
    ]
    etkinlikler.extend(ornek_etkinlikler)
    
    while True:
        print("\n" + "="*35)
        print("ETKINLIK YONETIMI VE PLANLAMA")
        print("="*35)
        print("1. Etkinlik Ekle")
        print("2. Etkinlikleri Listele")
        print("3. Katılımcı Yönetimi")
        print("4. Etkinlik Takvimi")
        print("5. Etkinlik İstatistikleri")
        print("6. Etkinlik Şablonları")
        print("7. Çıkış")
        
        try:
            secim = int(input("\nSeçiminiz (1-7): "))
            
            if secim == 1:
                etkinlik_ekle()
            elif secim == 2:
                etkinlik_listele()
            elif secim == 3:
                katilimci_yonetimi()
            elif secim == 4:
                etkinlik_takvimi()
            elif secim == 5:
                etkinlik_istatistikleri()
            elif secim == 6:
                etkinlik_sablonlari()
            elif secim == 7:
                print("Etkinlik yönetiminden çıkılıyor!")
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