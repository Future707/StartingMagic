"""
    Script: 08_programlama.py
    Açıklama: Kodlama dilleri hakkında bilgi veren interaktif eğitim uygulaması.
    Yazar: [Future Developer]
    Tarih: [15.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import random

print("KODLAMA DILLERI BILGI SISTEMI")
print("=" * 35)

# KODLAMA DILLERI VERITABANI
KODLAMA_DILLERI = {
    "Python": {
        "yil": 1991,
        "tip": "Yüksek Seviye",
        "paradigma": "Nesne Yönelimli, Prosedürel",
        "kullanim_alanlari": ["Web Geliştirme", "Veri Bilimi", "AI/ML", "Otomasyon"],
        "populerlik": 9,
        "ogrenme_zorlugu": 2,
        "avantajlar": ["Kolay sözdizimi", "Geniş kütüphane desteği", "Büyük topluluk"],
        "dezavantajlar": ["Yavaş hız", "GIL sorunu", "Mobil geliştirme sınırlı"],
        "ornek_kod": "print('Merhaba Dünya!')"
    },
    "JavaScript": {
        "yil": 1995,
        "tip": "Yüksek Seviye",
        "paradigma": "Nesne Yönelimli, Fonksiyonel",
        "kullanim_alanlari": ["Web Frontend", "Web Backend", "Mobil", "Desktop"],
        "populerlik": 10,
        "ogrenme_zorlugu": 3,
        "avantajlar": ["Her yerde çalışır", "Hızlı geliştirme", "Büyük ekosistem"],
        "dezavantajlar": ["Tip güvenliği yok", "Callback hell", "Browser uyumluluk"],
        "ornek_kod": "console.log('Merhaba Dünya!');"
    },
    "Java": {
        "yil": 1995,
        "tip": "Yüksek Seviye",
        "paradigma": "Nesne Yönelimli",
        "kullanim_alanlari": ["Enterprise", "Android", "Web Backend", "Big Data"],
        "populerlik": 8,
        "ogrenme_zorlugu": 4,
        "avantajlar": ["Platform bağımsız", "Güçlü tip sistemi", "Enterprise destek"],
        "dezavantajlar": ["Verbose sözdizimi", "Yavaş başlangıç", "Bellek tüketimi"],
        "ornek_kod": "System.out.println(\"Merhaba Dünya!\");"
    },
    "C++": {
        "yil": 1985,
        "tip": "Orta Seviye",
        "paradigma": "Nesne Yönelimli, Prosedürel",
        "kullanim_alanlari": ["Sistem Programlama", "Oyun", "Embedded", "HPC"],
        "populerlik": 6,
        "ogrenme_zorluğu": 8,
        "avantajlar": ["Yüksek performans", "Bellek kontrolü", "Geniş kullanım"],
        "dezavantajlar": ["Karmaşık sözdizimi", "Manuel bellek yönetimi", "Güvenlik"],
        "ornek_kod": "#include<iostream>\nstd::cout << \"Merhaba Dünya!\" << std::endl;"
    },
    "Go": {
        "yil": 2009,
        "tip": "Yüksek Seviye",
        "paradigma": "Prosedürel, Concurrent",
        "kullanim_alanlari": ["Cloud", "Mikroservisler", "DevOps", "Network"],
        "populerlik": 7,
        "ogrenme_zorlugu": 3,
        "avantajlar": ["Hızlı derleme", "Concurrency", "Basit sözdizimi"],
        "dezavantajlar": ["Sınırlı kütüphane", "Generics yok", "Yeni dil"],
        "ornek_kod": "package main\nfunc main() {\n    fmt.Println(\"Merhaba Dünya!\")\n}"
    },
    "Rust": {
        "yil": 2010,
        "tip": "Sistem Seviye",
        "paradigma": "Fonksiyonel, Prosedürel",
        "kullanim_alanlari": ["Sistem", "WebAssembly", "Blockchain", "Game Engine"],
        "populerlik": 5,
        "ogrenme_zorluğu": 9,
        "avantajlar": ["Bellek güvenliği", "Performans", "Thread güvenliği"],
        "dezavantajlar": ["Steep öğrenme eğrisi", "Compile time", "Küçük topluluk"],
        "ornek_kod": "fn main() {\n    println!(\"Merhaba Dünya!\");\n}"
    }
}

# DIL DETAY GOSTERME
def dil_detay_goster(dil_adi):
    if dil_adi not in KODLAMA_DILLERI:
        print("Dil bulunamadı!")
        return
    
    dil = KODLAMA_DILLERI[dil_adi]
    
    print(f"\n{dil_adi.upper()} DETAYLARI")
    print("=" * 25)
    print(f"Çıkış Yılı: {dil['yil']}")
    print(f"Tip: {dil['tip']}")
    print(f"Paradigma: {dil['paradigma']}")
    print(f"Popülerlik: {'⭐' * dil['populerlik']}/10")
    print(f"Öğrenme Zorluğu: {'🔥' * dil['ogrenme_zorluğu']}/10")
    
    print(f"\nKullanım Alanları:")
    for alan in dil['kullanim_alanlari']:
        print(f"- {alan}")
    
    print(f"\nAvantajları:")
    for avantaj in dil['avantajlar']:
        print(f"+ {avantaj}")
    
    print(f"\nDezavantajları:")
    for dezavantaj in dil['dezavantajlar']:
        print(f"- {dezavantaj}")
    
    print(f"\nÖrnek Kod:")
    print(f"```{dil_adi.lower()}")
    print(dil['ornek_kod'])
    print("```")

# DILLERI KARSILASTIRMA
def dil_karsilastirma():
    print("\nDIL KARSILASTIRMA")
    print("-" * 18)
    
    diller = list(KODLAMA_DILLERI.keys())
    print("Mevcut diller:")
    for i, dil in enumerate(diller, 1):
        print(f"{i}. {dil}")
    
    try:
        secim1 = int(input("\nİlk dil: ")) - 1
        secim2 = int(input("İkinci dil: ")) - 1
        
        if 0 <= secim1 < len(diller) and 0 <= secim2 < len(diller):
            dil1 = diller[secim1]
            dil2 = diller[secim2]
            
            print(f"\n{dil1} vs {dil2} KARSILASTIRMA")
            print("=" * 35)
            
            d1 = KODLAMA_DILLERI[dil1]
            d2 = KODLAMA_DILLERI[dil2]
            
            print(f"{'Kriter':<20} {dil1:<15} {dil2}")
            print("-" * 50)
            print(f"{'Çıkış Yılı':<20} {d1['yil']:<15} {d2['yil']}")
            print(f"{'Popülerlik':<20} {d1['populerlik']}/10{'':<10} {d2['populerlik']}/10")
            print(f"{'Öğrenme Zorluğu':<20} {d1['ogrenme_zorluğu']}/10{'':<10} {d2['ogrenme_zorluğu']}/10")
            print(f"{'Paradigma':<20} {d1['paradigma']:<15} {d2['paradigma']}")
            
            # Hangi dil daha iyi?
            print(f"\nDEGERLENDIRME:")
            puan1, puan2 = 0, 0
            
            if d1['populerlik'] > d2['populerlik']:
                print(f"- Popülerlik: {dil1} kazandı")
                puan1 += 1
            elif d2['populerlik'] > d1['populerlik']:
                print(f"- Popülerlik: {dil2} kazandı")
                puan2 += 1
            
            if d1['ogrenme_zorluğu'] < d2['ogrenme_zorluğu']:
                print(f"- Öğrenme Kolaylığı: {dil1} kazandı")
                puan1 += 1
            elif d2['ogrenme_zorluğu'] < d1['ogrenme_zorluğu']:
                print(f"- Öğrenme Kolaylığı: {dil2} kazandı")
                puan2 += 1
            
            print(f"\nSonuç: {dil1}({puan1}) - {dil2}({puan2})")
            
    except (ValueError, IndexError):
        print("Geçersiz seçim!")

# DIL ONERI SISTEMI
def dil_oneri_sistemi():
    print("\nDIL ONERI SISTEMI")
    print("-" * 19)
    
    print("Size uygun programlama dilini bulalım!")
    print("\nBirkaç soru soracağım:")
    
    try:
        # Soru 1: Deneyim seviyesi
        print("\n1. Programlama deneyiminiz nedir?")
        print("   1. Hiç yok (Başlangıç)")
        print("   2. Az var (1-2 yıl)")
        print("   3. Orta (2-5 yıl)")
        print("   4. İleri (5+ yıl)")
        deneyim = int(input("Seçim: "))
        
        # Soru 2: Hedef alan
        print("\n2. Hangi alanda çalışmak istiyorsunuz?")
        print("   1. Web Geliştirme")
        print("   2. Mobil Uygulama")
        print("   3. Veri Bilimi / AI")
        print("   4. Oyun Geliştirme")
        print("   5. Sistem Programlama")
        alan = int(input("Seçim: "))
        
        # Soru 3: Performans önceliği
        print("\n3. Performans ne kadar önemli?")
        print("   1. Çok önemli değil")
        print("   2. Orta derecede önemli")
        print("   3. Çok önemli")
        performans = int(input("Seçim: "))
        
        # Öneri algoritması
        oneriler = []
        
        if deneyim <= 2 and alan in [1, 3]:
            oneriler.append(("Python", "Başlangıç için mükemmel, kolay sözdizimi"))
        
        if alan == 1:  # Web
            oneriler.append(("JavaScript", "Web geliştirme için vazgeçilmez"))
            if deneyim >= 2:
                oneriler.append(("Java", "Enterprise web uygulamaları için"))
        
        if alan == 2:  # Mobil
            oneriler.append(("Java", "Android geliştirme için"))
            oneriler.append(("JavaScript", "Cross-platform mobil için"))
        
        if alan == 3:  # Veri Bilimi
            oneriler.append(("Python", "Veri biliminde lider dil"))
        
        if alan == 4:  # Oyun
            oneriler.append(("C++", "AAA oyun geliştirme için"))
        
        if alan == 5 or performans == 3:  # Sistem
            oneriler.append(("Rust", "Modern sistem programlama"))
            oneriler.append(("C++", "Yüksek performans için"))
            oneriler.append(("Go", "Cloud ve mikroservisler için"))
        
        print(f"\nSIZE UYGUN DILLER:")
        print("-" * 25)
        
        if oneriler:
            for i, (dil, aciklama) in enumerate(oneriler[:3], 1):
                pop = KODLAMA_DILLERI[dil]['populerlik']
                zor = KODLAMA_DILLERI[dil]['ogrenme_zorluğu']
                print(f"{i}. {dil}")
                print(f"   Sebep: {aciklama}")
                print(f"   Popülerlik: {pop}/10, Zorluk: {zor}/10")
                print()
        else:
            print("Maalesef uygun öneri bulunamadı!")
            
    except ValueError:
        print("Geçersiz seçim!")

# DIL QUIZ OYUNU
def dil_quiz():
    print("\nKODLAMA DILLERI QUIZ")
    print("-" * 23)
    
    sorular = [
        ("Hangi dil 1991'de çıktı?", "Python"),
        ("En popüler web dili hangisi?", "JavaScript"),
        ("Android geliştirme için hangi dil kullanılır?", "Java"),
        ("Hangi dil sistem programlama için idealdir?", "C++"),
        ("Google tarafından geliştirilen dil?", "Go"),
        ("Mozilla tarafından desteklenen güvenli dil?", "Rust")
    ]
    
    dogru_cevap = 0
    toplam_soru = len(sorular)
    
    print(f"Toplam {toplam_soru} soru sorulacak!")
    
    for i, (soru, cevap) in enumerate(sorular, 1):
        print(f"\nSoru {i}: {soru}")
        
        # Seçenekler oluştur
        diller = list(KODLAMA_DILLERI.keys())
        secenekler = [cevap]
        
        # Yanlış seçenekler ekle
        while len(secenekler) < 4:
            rastgele_dil = random.choice(diller)
            if rastgele_dil not in secenekler:
                secenekler.append(rastgele_dil)
        
        random.shuffle(secenekler)
        dogru_index = secenekler.index(cevap) + 1
        
        for j, secenek in enumerate(secenekler, 1):
            print(f"   {j}. {secenek}")
        
        try:
            kullanici_cevap = int(input("Cevabınız: "))
            if kullanici_cevap == dogru_index:
                print("Doğru! ✓")
                dogru_cevap += 1
            else:
                print(f"Yanlış! Doğru cevap: {cevap}")
        except ValueError:
            print(f"Geçersiz seçim! Doğru cevap: {cevap}")
    
    print(f"\nQUIZ TAMAMLANDI!")
    print(f"Sonuç: {dogru_cevap}/{toplam_soru} ({dogru_cevap/toplam_soru*100:.1f}%)")
    
    if dogru_cevap == toplam_soru:
        print("Mükemmel! Programlama dilleri konusunda expertsiniz!")
    elif dogru_cevap >= toplam_soru * 0.7:
        print("Çok iyi! Bilginiz oldukça yeterli.")
    elif dogru_cevap >= toplam_soru * 0.5:
        print("Fena değil! Biraz daha çalışmanız gerekiyor.")
    else:
        print("Daha fazla öğrenmeniz gerekiyor!")

# TREND ANALIZI
def trend_analizi():
    print("\nPROGRAMLAMA DILI TREND ANALIZI")
    print("-" * 35)
    
    # Popülerlik sıralaması
    dil_pop = [(dil, bilgi['populerlik']) for dil, bilgi in KODLAMA_DILLERI.items()]
    dil_pop.sort(key=lambda x: x[1], reverse=True)
    
    print("POPULERLIK SIRALAMASI:")
    for i, (dil, pop) in enumerate(dil_pop, 1):
        yildiz = "⭐" * pop
        print(f"{i}. {dil:<12} {yildiz} ({pop}/10)")
    
    # Öğrenme zorluğu
    print(f"\nOGRENME ZORLUK SIRALAMASI:")
    dil_zor = [(dil, bilgi['ogrenme_zorluğu']) for dil, bilgi in KODLAMA_DILLERI.items()]
    dil_zor.sort(key=lambda x: x[1])
    
    for i, (dil, zor) in enumerate(dil_zor, 1):
        if zor <= 3:
            seviye = "Kolay"
        elif zor <= 6:
            seviye = "Orta"
        else:
            seviye = "Zor"
        print(f"{i}. {dil:<12} {seviye:<6} ({zor}/10)")
    
    # Kullanım alanı analizi
    print(f"\nKULLANIM ALANI ANALIZI:")
    alan_sayilari = {}
    
    for dil_bilgi in KODLAMA_DILLERI.values():
        for alan in dil_bilgi['kullanim_alanlari']:
            alan_sayilari[alan] = alan_sayilari.get(alan, 0) + 1
    
    for alan, sayi in sorted(alan_sayilari.items(), key=lambda x: x[1], reverse=True):
        print(f"- {alan}: {sayi} dil")

# OGRENIM YOLU HARITASI
def ogrenim_yolu():
    print("\nOGRENIM YOLU HARITASI")
    print("-" * 24)
    
    haritalar = {
        "Web Geliştirici": [
            "1. HTML/CSS (Temel)",
            "2. JavaScript (Zorunlu)",
            "3. Python veya Java (Backend)",
            "4. Database (SQL)",
            "5. Framework öğren (React, Django vs.)"
        ],
        "Veri Bilimci": [
            "1. Python (Temel)",
            "2. Matematik/İstatistik",
            "3. Pandas, NumPy kütüphaneleri",
            "4. Machine Learning (Scikit-learn)",
            "5. Deep Learning (TensorFlow/PyTorch)"
        ],
        "Mobil Geliştirici": [
            "1. Java (Android için)",
            "2. Android Studio öğren",
            "3. UI/UX tasarım prensipleri",
            "4. Database ve API kullanımı",
            "5. Cross-platform (Flutter, React Native)"
        ],
        "Oyun Geliştirici": [
            "1. C++ (Temel)",
            "2. Matematik (Linear Algebra)",
            "3. Game Engine (Unity, Unreal)",
            "4. Graphics Programming",
            "5. Networking ve Multiplayer"
        ]
    }
    
    print("Kariyer yolları:")
    for i, yol in enumerate(haritalar.keys(), 1):
        print(f"{i}. {yol}")
    
    try:
        secim = int(input("Hangi yolu seçiyorsunuz: ")) - 1
        yol_adi = list(haritalar.keys())[secim]
        
        print(f"\n{yol_adi.upper()} YOLU:")
        print("-" * 25)
        
        for adim in haritalar[yol_adi]:
            print(adim)
        
        print(f"\nTahmini süre: 12-18 ay")
        print(f"Zorluk seviyesi: Orta-İleri")
        
    except (ValueError, IndexError):
        print("Geçersiz seçim!")

# ANA PROGRAM
def main():
    while True:
        print("\n" + "="*35)
        print("KODLAMA DILLERI BILGI SISTEMI")
        print("="*35)
        print("1. Dil Detayları")
        print("2. Dil Karşılaştırma")
        print("3. Dil Öneri Sistemi")
        print("4. Quiz Oyunu")
        print("5. Trend Analizi")
        print("6. Öğrenim Yolu Haritası")
        print("7. Çıkış")
        
        try:
            secim = int(input("\nSeçiminiz (1-7): "))
            
            if secim == 1:
                print("\nMevcut diller:")
                for i, dil in enumerate(KODLAMA_DILLERI.keys(), 1):
                    print(f"{i}. {dil}")
                try:
                    dil_secim = int(input("Hangi dil: ")) - 1
                    dil_adi = list(KODLAMA_DILLERI.keys())[dil_secim]
                    dil_detay_goster(dil_adi)
                except (ValueError, IndexError):
                    print("Geçersiz seçim!")
            elif secim == 2:
                dil_karsilastirma()
            elif secim == 3:
                dil_oneri_sistemi()
            elif secim == 4:
                dil_quiz()
            elif secim == 5:
                trend_analizi()
            elif secim == 6:
                ogrenim_yolu()
            elif secim == 7:
                print("Kodlama dünyasından çıkılıyor!")
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