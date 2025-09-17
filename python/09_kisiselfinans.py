"""
    Script: 09_kisiselfinans.py
    Açıklama: Kişisel gelir-gider takibi ve bütçe yönetim uygulaması.
    Yazar: [Future Developer]
    Tarih: [17.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import datetime
import math

print("KISISEL FINANS TAKIP SISTEMI")
print("=" * 35)

# GLOBAL VERILER
gelirler = []
giderler = []
butce_limitleri = {}

class FinansIslem:
    def __init__(self, miktar, kategori, aciklama, tarih=None):
        self.miktar = miktar
        self.kategori = kategori
        self.aciklama = aciklama
        self.tarih = tarih or datetime.date.today()
        
    def __str__(self):
        return f"{self.tarih} - {self.kategori}: {self.miktar} TL ({self.aciklama})"

# GELIR EKLEME
def gelir_ekle():
    print("\nGELIR EKLEME")
    print("-" * 13)
    
    try:
        miktar = float(input("Gelir miktarı (TL): "))
        if miktar <= 0:
            print("Gelir miktarı pozitif olmalı!")
            return
            
        print("Gelir kategorileri:")
        kategoriler = ["Maaş", "Freelance", "Yatırım", "Kira Geliri", "Diğer"]
        for i, kat in enumerate(kategoriler, 1):
            print(f"{i}. {kat}")
        
        kat_secim = int(input("Kategori seçin (1-5): ")) - 1
        if 0 <= kat_secim < len(kategoriler):
            kategori = kategoriler[kat_secim]
        else:
            kategori = "Diğer"
        
        aciklama = input("Açıklama (opsiyonel): ").strip()
        
        gelir = FinansIslem(miktar, kategori, aciklama)
        gelirler.append(gelir)
        
        print(f"{miktar} TL gelir eklendi!")
        
    except ValueError:
        print("Geçerli bir miktar girin!")

# GIDER EKLEME
def gider_ekle():
    print("\nGIDER EKLEME")
    print("-" * 13)
    
    try:
        miktar = float(input("Gider miktarı (TL): "))
        if miktar <= 0:
            print("Gider miktarı pozitif olmalı!")
            return
            
        print("Gider kategorileri:")
        kategoriler = ["Yemek", "Ulaşım", "Barınma", "Sağlık", "Eğlence", "Alışveriş", "Diğer"]
        for i, kat in enumerate(kategoriler, 1):
            print(f"{i}. {kat}")
        
        kat_secim = int(input("Kategori seçin (1-7): ")) - 1
        if 0 <= kat_secim < len(kategoriler):
            kategori = kategoriler[kat_secim]
        else:
            kategori = "Diğer"
        
        aciklama = input("Açıklama (opsiyonel): ").strip()
        
        gider = FinansIslem(miktar, kategori, aciklama)
        giderler.append(gider)
        
        # Bütçe kontrolü
        if kategori in butce_limitleri:
            ay_gideri = sum(g.miktar for g in giderler 
                          if g.kategori == kategori 
                          and g.tarih.month == datetime.date.today().month)
            
            if ay_gideri > butce_limitleri[kategori]:
                print(f"UYARI: {kategori} bütçesini aştınız!")
                print(f"Limit: {butce_limitleri[kategori]} TL")
                print(f"Harcanan: {ay_gideri} TL")
        
        print(f"{miktar} TL gider eklendi!")
        
    except ValueError:
        print("Geçerli bir miktar girin!")

# OZET RAPORU
def ozet_raporu():
    print("\nFINANS OZET RAPORU")
    print("-" * 20)
    
    if not gelirler and not giderler:
        print("Henüz kayıt bulunmuyor!")
        return
    
    # Bu ay verileri
    bugun = datetime.date.today()
    bu_ay_gelir = sum(g.miktar for g in gelirler if g.tarih.month == bugun.month)
    bu_ay_gider = sum(g.miktar for g in giderler if g.tarih.month == bugun.month)
    net_kazanc = bu_ay_gelir - bu_ay_gider
    
    print(f"BU AY ({bugun.month}/{bugun.year}):")
    print(f"Toplam Gelir: {bu_ay_gelir:,.2f} TL")
    print(f"Toplam Gider: {bu_ay_gider:,.2f} TL")
    print(f"Net: {net_kazanc:,.2f} TL")
    
    if net_kazanc > 0:
        print("🟢 Bu ay kar ettiniz!")
    elif net_kazanc < 0:
        print("🔴 Bu ay zarar ettiniz!")
    else:
        print("🟡 Bu ay başa baş çıktınız!")
    
    # Kategoriye göre giderler
    if giderler:
        print(f"\nKATEGORI BAZLI GIDERLER:")
        kategori_giderleri = {}
        for gider in giderler:
            if gider.tarih.month == bugun.month:
                kategori_giderleri[gider.kategori] = kategori_giderleri.get(gider.kategori, 0) + gider.miktar
        
        for kategori, miktar in sorted(kategori_giderleri.items(), key=lambda x: x[1], reverse=True):
            yuzde = (miktar / bu_ay_gider * 100) if bu_ay_gider > 0 else 0
            print(f"- {kategori}: {miktar:,.2f} TL (%{yuzde:.1f})")

# BUTCE YONETIMI
def butce_yonetimi():
    print("\nBUTCE YONETIMI")
    print("-" * 15)
    
    print("1. Bütçe Limiti Belirleme")
    print("2. Mevcut Limitler")
    print("3. Bütçe Durumu")
    
    try:
        secim = int(input("Seçiminiz (1-3): "))
        
        if secim == 1:
            kategoriler = ["Yemek", "Ulaşım", "Eğlence", "Alışveriş", "Sağlık"]
            print("Kategoriler:")
            for i, kat in enumerate(kategoriler, 1):
                print(f"{i}. {kat}")
            
            kat_secim = int(input("Kategori seçin: ")) - 1
            if 0 <= kat_secim < len(kategoriler):
                kategori = kategoriler[kat_secim]
                limit = float(input(f"{kategori} için aylık limit (TL): "))
                butce_limitleri[kategori] = limit
                print(f"{kategori} için {limit} TL limit belirlendi!")
        
        elif secim == 2:
            if butce_limitleri:
                print("MEVCUT LIMITLER:")
                for kategori, limit in butce_limitleri.items():
                    print(f"- {kategori}: {limit:,.2f} TL")
            else:
                print("Henüz limit belirlenmemiş!")
        
        elif secim == 3:
            if butce_limitleri:
                bugun = datetime.date.today()
                print("BUTCE DURUMU:")
                
                for kategori, limit in butce_limitleri.items():
                    harcanan = sum(g.miktar for g in giderler 
                                 if g.kategori == kategori 
                                 and g.tarih.month == bugun.month)
                    
                    kalan = limit - harcanan
                    yuzde = (harcanan / limit * 100) if limit > 0 else 0
                    
                    durum = "🟢" if yuzde < 80 else "🟡" if yuzde < 100 else "🔴"
                    
                    print(f"{durum} {kategori}:")
                    print(f"   Limit: {limit:,.2f} TL")
                    print(f"   Harcanan: {harcanan:,.2f} TL (%{yuzde:.1f})")
                    print(f"   Kalan: {kalan:,.2f} TL")
                    print()
            else:
                print("Henüz bütçe limiti belirlenmemiş!")
                
    except ValueError:
        print("Geçerli değer girin!")

# ISTATISTIKLER
def istatistikler():
    print("\nFINANSAL ISTATISTIKLER")
    print("-" * 25)
    
    if not gelirler and not giderler:
        print("İstatistik için veri bulunmuyor!")
        return
    
    # Genel istatistikler
    toplam_gelir = sum(g.miktar for g in gelirler)
    toplam_gider = sum(g.miktar for g in giderler)
    
    print(f"GENEL ISTATISTIKLER:")
    print(f"Toplam Gelir: {toplam_gelir:,.2f} TL")
    print(f"Toplam Gider: {toplam_gider:,.2f} TL")
    print(f"Net Durum: {toplam_gelir - toplam_gider:,.2f} TL")
    
    # Ortalamalar
    if gelirler:
        ort_gelir = toplam_gelir / len(gelirler)
        print(f"Ortalama Gelir/İşlem: {ort_gelir:,.2f} TL")
    
    if giderler:
        ort_gider = toplam_gider / len(giderler)
        print(f"Ortalama Gider/İşlem: {ort_gider:,.2f} TL")
    
    # En büyük işlemler
    if gelirler:
        en_buyuk_gelir = max(gelirler, key=lambda x: x.miktar)
        print(f"\nEn büyük gelir: {en_buyuk_gelir}")
    
    if giderler:
        en_buyuk_gider = max(giderler, key=lambda x: x.miktar)
        print(f"En büyük gider: {en_buyuk_gider}")
    
    # Aylık trend
    print(f"\nAYLIK TREND:")
    aylar = {}
    
    for gelir in gelirler:
        ay_key = f"{gelir.tarih.year}-{gelir.tarih.month:02d}"
        if ay_key not in aylar:
            aylar[ay_key] = {"gelir": 0, "gider": 0}
        aylar[ay_key]["gelir"] += gelir.miktar
    
    for gider in giderler:
        ay_key = f"{gider.tarih.year}-{gider.tarih.month:02d}"
        if ay_key not in aylar:
            aylar[ay_key] = {"gelir": 0, "gider": 0}
        aylar[ay_key]["gider"] += gider.miktar
    
    for ay, veriler in sorted(aylar.items()):
        net = veriler["gelir"] - veriler["gider"]
        durum = "📈" if net > 0 else "📉" if net < 0 else "➡️"
        print(f"{ay}: {durum} {net:,.2f} TL")

# HEDEF BELIRLEME
def hedef_belirleme():
    print("\nFINANSAL HEDEF BELIRLEME")
    print("-" * 27)
    
    try:
        print("Hedef türü seçin:")
        print("1. Birikim Hedefi")
        print("2. Gider Azaltma Hedefi")
        print("3. Gelir Artırma Hedefi")
        
        secim = int(input("Seçiminiz (1-3): "))
        
        if secim == 1:
            hedef_miktar = float(input("Hedef birikim miktarı (TL): "))
            sure = int(input("Kaç ayda biriktirmek istiyorsunz: "))
            
            aylik_birikim = hedef_miktar / sure
            
            # Mevcut durum analizi
            bugun = datetime.date.today()
            bu_ay_gelir = sum(g.miktar for g in gelirler if g.tarih.month == bugun.month)
            bu_ay_gider = sum(g.miktar for g in giderler if g.tarih.month == bugun.month)
            mevcut_birikim = bu_ay_gelir - bu_ay_gider
            
            print(f"\nHEDEF ANALIZI:")
            print(f"Hedef: {hedef_miktar:,.2f} TL")
            print(f"Süre: {sure} ay")
            print(f"Aylık birikim gereği: {aylik_birikim:,.2f} TL")
            print(f"Mevcut aylık birikim: {mevcut_birikim:,.2f} TL")
            
            if mevcut_birikim >= aylik_birikim:
                print("🟢 Hedefintize ulaşabilirsiniz!")
            else:
                eksik = aylik_birikim - mevcut_birikim
                print(f"🔴 Aylık {eksik:,.2f} TL daha biriktirmeniz gerekiyor!")
                print("Öneriler:")
                print(f"- Giderlerinizi {eksik/2:,.2f} TL azaltın")
                print(f"- Gelirinizi {eksik/2:,.2f} TL artırın")
        
        elif secim == 2:
            kategori = input("Hangi kategoride azaltma yapmak istiyorsunuz: ").title()
            azaltma_orani = float(input("Yüzde kaç azaltmak istiyorsunuz: "))
            
            # Mevcut durum
            bugun = datetime.date.today()
            mevcut_gider = sum(g.miktar for g in giderler 
                             if g.kategori == kategori and g.tarih.month == bugun.month)
            
            hedef_gider = mevcut_gider * (1 - azaltma_orani/100)
            tasarruf = mevcut_gider - hedef_gider
            
            print(f"\nAZALTMA HEDEFI:")
            print(f"Kategori: {kategori}")
            print(f"Mevcut aylık gider: {mevcut_gider:,.2f} TL")
            print(f"Hedef gider: {hedef_gider:,.2f} TL")
            print(f"Aylık tasarruf: {tasarruf:,.2f} TL")
            print(f"Yıllık tasarruf: {tasarruf * 12:,.2f} TL")
            
        elif secim == 3:
            artis_hedefi = float(input("Ne kadar gelir artışı hedefliyorsunuz (TL): "))
            
            bugun = datetime.date.today()
            mevcut_gelir = sum(g.miktar for g in gelirler if g.tarih.month == bugun.month)
            hedef_gelir = mevcut_gelir + artis_hedefi
            artis_orani = (artis_hedefi / mevcut_gelir * 100) if mevcut_gelir > 0 else 0
            
            print(f"\nGELIR ARTIRMA HEDEFI:")
            print(f"Mevcut aylık gelir: {mevcut_gelir:,.2f} TL")
            print(f"Hedef gelir: {hedef_gelir:,.2f} TL")
            print(f"Gerekli artış: %{artis_orani:.1f}")
            
            print(f"\nÖNERILER:")
            print(f"- Ek iş bulun: {artis_hedefi/2:,.2f} TL")
            print(f"- Yatırım yapın: {artis_hedefi/3:,.2f} TL")
            print(f"- Freelance çalışın: {artis_hedefi/4:,.2f} TL")
            
    except ValueError:
        print("Geçerli değerler girin!")

# ANA PROGRAM
def main():
    # Örnek veriler
    ornek_gelir = FinansIslem(5000, "Maaş", "Aylık maaş")
    ornek_gider1 = FinansIslem(1200, "Barınma", "Kira")
    ornek_gider2 = FinansIslem(800, "Yemek", "Market alışverişi")
    
    gelirler.append(ornek_gelir)
    giderler.extend([ornek_gider1, ornek_gider2])
    
    while True:
        print("\n" + "="*35)
        print("KISISEL FINANS TAKIP SISTEMI")
        print("="*35)
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Özet Rapor")
        print("4. Bütçe Yönetimi")
        print("5. İstatistikler")
        print("6. Hedef Belirleme")
        print("7. Çıkış")
        
        try:
            secim = int(input("\nSeçiminiz (1-7): "))
            
            if secim == 1:
                gelir_ekle()
            elif secim == 2:
                gider_ekle()
            elif secim == 3:
                ozet_raporu()
            elif secim == 4:
                butce_yonetimi()
            elif secim == 5:
                istatistikler()
            elif secim == 6:
                hedef_belirleme()
            elif secim == 7:
                print("Finans takibinden çıkılıyor!")
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