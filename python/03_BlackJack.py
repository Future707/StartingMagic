"""
    Script: 03_blackJack.py
    Açıklama: BlackJack kart oyunu simülasyonu ve oyun mantığı öğretimi.
    Yazar: [Future Developer]
    Tarih: [05.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import random

print("BLACKJACK KART OYUNU")
print("=" * 30)

class BlackJack:
    def __init__(self):
        self.kartlar = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.renkler = ['Maça', 'Kupa', 'Sinek', 'Karo']
        self.deste = []
        self.oyuncu_eli = []
        self.krupiye_eli = []
        self.oyuncu_para = 1000
        self.bahis = 0
        
    def deste_olustur(self):
        """Yeni deste oluştur"""
        self.deste = []
        for renk in self.renkler:
            for kart in self.kartlar:
                self.deste.append((kart, renk))
        random.shuffle(self.deste)
        
    def kart_degeri(self, kart):
        """Kartın değerini hesapla"""
        if kart == 'A':
            return 11
        elif kart in ['J', 'Q', 'K']:
            return 10
        else:
            return int(kart)
            
    def el_degeri(self, el):
        """Elin toplam değerini hesapla"""
        toplam = 0
        as_sayisi = 0
        
        for kart, _ in el:
            deger = self.kart_degeri(kart)
            toplam += deger
            if kart == 'A':
                as_sayisi += 1
        
        # As'ları 1 olarak hesapla gerekirse
        while toplam > 21 and as_sayisi > 0:
            toplam -= 10
            as_sayisi -= 1
            
        return toplam
    
    def kart_cek(self):
        """Desteden kart çek"""
        if len(self.deste) < 10:  # Deste azaldıysa yenile
            self.deste_olustur()
        return self.deste.pop()
    
    def eli_goster(self, el, gizli=False):
        """Eli ekranda göster"""
        if gizli:
            # Krupiye'nin ilk kartını gizle
            print(f"[Gizli Kart] - {el[1][0]} {el[1][1]}")
        else:
            for kart, renk in el:
                print(f"{kart} {renk}", end=" - ")
            print(f"\nToplam: {self.el_degeri(el)}")
    
    def baslangic_dagitimi(self):
        """Oyuna 2'şer kart dağıt"""
        self.oyuncu_eli = []
        self.krupiye_eli = []
        
        for _ in range(2):
            self.oyuncu_eli.append(self.kart_cek())
            self.krupiye_eli.append(self.kart_cek())
    
    def oyuncu_turu(self):
        """Oyuncunun kartlarını çekme turu"""
        while True:
            print(f"\nOYUNCU ELI:")
            self.eli_goster(self.oyuncu_eli)
            
            if self.el_degeri(self.oyuncu_eli) > 21:
                print("BUST! 21'i aştınız!")
                return False
            elif self.el_degeri(self.oyuncu_eli) == 21:
                print("21! Mükemmel!")
                return True
                
            print("\n1. Kart Çek (Hit)")
            print("2. Dur (Stand)")
            
            try:
                secim = int(input("Seçiminiz (1-2): "))
                if secim == 1:
                    self.oyuncu_eli.append(self.kart_cek())
                elif secim == 2:
                    return True
                else:
                    print("Geçersiz seçim!")
            except ValueError:
                print("Lütfen 1 veya 2 girin!")
    
    def krupiye_turu(self):
        """Krupiyenin kartlarını çekme turu"""
        print(f"\nKRUPIYE ELI:")
        self.eli_goster(self.krupiye_eli)
        
        while self.el_degeri(self.krupiye_eli) < 17:
            print("\nKrupiye kart çekiyor...")
            input("Devam için Enter'a basın...")
            self.krupiye_eli.append(self.kart_cek())
            print(f"KRUPIYE ELI:")
            self.eli_goster(self.krupiye_eli)
        
        return self.el_degeri(self.krupiye_eli) <= 21
    
    def kazanani_belirle(self):
        """Oyunun kazananını belirle"""
        oyuncu_puan = self.el_degeri(self.oyuncu_eli)
        krupiye_puan = self.el_degeri(self.krupiye_eli)
        
        print(f"\nSONUC:")
        print(f"Oyuncu: {oyuncu_puan}")
        print(f"Krupiye: {krupiye_puan}")
        
        if oyuncu_puan > 21:
            print("Oyuncu kaybetti - BUST!")
            return "krupiye"
        elif krupiye_puan > 21:
            print("Krupiye kaybetti - BUST!")
            return "oyuncu"
        elif oyuncu_puan > krupiye_puan:
            print("Oyuncu kazandı!")
            return "oyuncu"
        elif krupiye_puan > oyuncu_puan:
            print("Krupiye kazandı!")
            return "krupiye"
        else:
            print("Beraberlik!")
            return "berabere"
    
    def bahis_al(self):
        """Oyuncudan bahis al"""
        print(f"\nMevcud paranız: ${self.oyuncu_para}")
        
        while True:
            try:
                bahis = int(input("Bahis miktarı: $"))
                if bahis <= 0:
                    print("Bahis pozitif olmalı!")
                elif bahis > self.oyuncu_para:
                    print("Yeterli paranız yok!")
                else:
                    self.bahis = bahis
                    return True
            except ValueError:
                print("Geçerli bir miktar girin!")
    
    def para_hesapla(self, kazanan):
        """Para hesaplaması yap"""
        if kazanan == "oyuncu":
            self.oyuncu_para += self.bahis
            print(f"${self.bahis} kazandınız!")
        elif kazanan == "krupiye":
            self.oyuncu_para -= self.bahis
            print(f"${self.bahis} kaybettiniz!")
        else:
            print("Bahis iade edildi!")
        
        print(f"Yeni bakiye: ${self.oyuncu_para}")
    
    def oyun_dongusu(self):
        """Ana oyun döngüsü"""
        self.deste_olustur()
        
        while self.oyuncu_para > 0:
            print("\n" + "="*40)
            print("YENİ OYUN")
            print("="*40)
            
            if not self.bahis_al():
                break
                
            self.baslangic_dagitimi()
            
            print(f"\nKRUPIYE ELI:")
            self.eli_goster(self.krupiye_eli, gizli=True)
            
            # Oyuncu turu
            if self.oyuncu_turu():
                # Krupiye turu
                self.krupiye_turu()
            
            # Kazanan belirleme
            kazanan = self.kazanani_belirle()
            self.para_hesapla(kazanan)
            
            if self.oyuncu_para <= 0:
                print("\nParanız bitti! Oyun sona erdi.")
                break
            
            devam = input("\nYeni oyun oynamak ister misiniz? (e/h): ").lower()
            if devam != 'e':
                break
        
        print(f"\nOyun sona erdi! Final bakiye: ${self.oyuncu_para}")

# OYUN İSTATİSTİKLERİ
def oyun_istatistikleri():
    """Blackjack hakkında bilgi ver"""
    print("\nBLACKJACK OYUN KURALLARI")
    print("-" * 30)
    print("1. Amaç: 21'e en yakın skoru yapmak")
    print("2. 21'i aşmak = Kaybetmek (BUST)")
    print("3. As = 1 veya 11 (otomatik hesap)")
    print("4. J, Q, K = 10 puan")
    print("5. Krupiye 17'de durmak zorunda")
    print("\nKART DEĞERLERİ:")
    kartlar = {'A': '1 veya 11', '2-10': 'Yazılı değer', 'J,Q,K': '10'}
    for kart, deger in kartlar.items():
        print(f"{kart}: {deger}")

# KART SAYMA EĞİTİMİ
def kart_sayma_egitimi():
    """Basit kart sayma stratejisi öğret"""
    print("\nBASİT KART SAYMA STRATEJİSİ")
    print("-" * 35)
    print("Hi-Lo Sistem:")
    print("+1: 2, 3, 4, 5, 6")
    print(" 0: 7, 8, 9")
    print("-1: 10, J, Q, K, A")
    print("\nYüksek sayım = Daha fazla yüksek kart kaldı")
    print("Düşük sayım = Daha fazla düşük kart kaldı")
    
    print("\nÖRNEK KARTLAR:")
    ornekler = [('5', '+1'), ('K', '-1'), ('8', '0'), ('A', '-1'), ('3', '+1')]
    toplam = 0
    
    for kart, deger in ornekler:
        print(f"Kart: {kart} -> {deger}")
        if deger == '+1':
            toplam += 1
        elif deger == '-1':
            toplam -= 1
    
    print(f"Toplam sayım: {toplam}")

# PROB Hesaplama
def olasilik_hesaplama():
    """Blackjack olasılıkları göster"""
    print("\nBLACKJACK OLASILİKLARI")
    print("-" * 25)
    
    # Temel olasılıklar
    olasiliklar = {
        "Blackjack (ilk 2 kart)": "4.8%",
        "Bust olma (12-16 arası)": "31-62%",
        "Krupiye bust olma": "28.4%",
        "21 yapma şansı": "7.4%"
    }
    
    for durum, oran in olasiliklar.items():
        print(f"{durum}: {oran}")
    
    print("\nSTRATEJİ İPUÇLARI:")
    ipuclari = [
        "12-16 arası: Krupiye 7+ ise kart çek",
        "17+: Her zaman dur",
        "11 ve altı: Her zaman kart çek",
        "As-8: Kart çekmeyi düşün"
    ]
    
    for i, ipucu in enumerate(ipuclari, 1):
        print(f"{i}. {ipucu}")

# ANA PROGRAM
def main():
    oyun = BlackJack()
    
    while True:
        print("\n" + "="*40)
        print("BLACKJACK MERKEZI")
        print("="*40)
        print("1. Blackjack Oyna")
        print("2. Oyun Kuralları")
        print("3. Kart Sayma Eğitimi")
        print("4. Olasılık Hesaplamaları")
        print("5. Çıkış")
        
        try:
            secim = int(input("\nSeçiminiz (1-5): "))
            
            if secim == 1:
                oyun.oyun_dongusu()
            elif secim == 2:
                oyun_istatistikleri()
            elif secim == 3:
                kart_sayma_egitimi()
            elif secim == 4:
                olasilik_hesaplama()
            elif secim == 5:
                print("Blackjack'ten çıkılıyor. Good luck!")
                break
            else:
                print("Geçersiz seçim!")
                
            input("\nDevam için Enter'a basın...")
            
        except ValueError:
            print("Lütfen 1-5 arası sayı girin!")
        except KeyboardInterrupt:
            print("\nProgram sonlandırılıyor...")
            break

if __name__ == "__main__":
    main()