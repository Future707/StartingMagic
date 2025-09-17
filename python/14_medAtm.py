'''
    Script: 14_medAtm.py
    Açıklama: Küçük boyutlu ATM simülasyonu. Kullanıcı giriş yapar, bakiye görüntüler, para yatırır, çeker ve işlem geçmişini takip eder.
    Yazar: [Future Developer]
    Tarih: [07.07.2025]
    Sürüm: 1.08
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
'''

import time
import getpass

class MedATM:
    def __init__(self):
        self.hesaplar = {
            "1001": {"sifre": "1234", "bakiye": 1000.0, "gecmis": []},
            "1002": {"sifre": "4321", "bakiye": 500.0, "gecmis": []}
        }
        self.giris_hesap = None

    def giris(self):
        print("\n--- MedATM Giriş ---")
        hesap_no = input("Hesap numaranızı girin: ")
        sifre = getpass.getpass("Şifrenizi girin: ")

        if hesap_no in self.hesaplar and self.hesaplar[hesap_no]["sifre"] == sifre:
            self.giris_hesap = hesap_no
            print("Başarıyla giriş yapıldı.")
            return True
        else:
            print("Hatalı hesap numarası veya şifre.")
            return False

    def bakiye_goster(self):
        bakiye = self.hesaplar[self.giris_hesap]["bakiye"]
        print(f"Mevcut bakiyeniz: {bakiye:.2f} TL")

    def para_yatir(self):
        try:
            miktar = float(input("Yatırılacak miktar: "))
        except ValueError:
            print("Geçersiz miktar.")
            return
        if miktar <= 0:
            print("Miktar sıfır veya negatif olamaz.")
            return
        self.hesaplar[self.giris_hesap]["bakiye"] += miktar
        self.hesaplar[self.giris_hesap]["gecmis"].append((time.ctime(), f"+{miktar:.2f} TL yatırıldı"))
        print(f"{miktar:.2f} TL yatırıldı.")

    def para_cek(self):
        try:
            miktar = float(input("Çekilecek miktar: "))
        except ValueError:
            print("Geçersiz miktar.")
            return
        if miktar <= 0:
            print("Miktar sıfır veya negatif olamaz.")
            return
        if miktar > self.hesaplar[self.giris_hesap]["bakiye"]:
            print("Yetersiz bakiye.")
            return
        self.hesaplar[self.giris_hesap]["bakiye"] -= miktar
        self.hesaplar[self.giris_hesap]["gecmis"].append((time.ctime(), f"-{miktar:.2f} TL çekildi"))
        print(f"{miktar:.2f} TL çekildi.")

    def gecmis_goster(self):
        print("\n--- İşlem Geçmişi ---")
        for tarih, islem in self.hesaplar[self.giris_hesap]["gecmis"]:
            print(f"{tarih} - {islem}")
        if not self.hesaplar[self.giris_hesap]["gecmis"]:
            print("Henüz işlem yapılmadı.")

    def menu(self):
        while True:
            print("\n--- MedATM Menü ---")
            print("1. Bakiye Görüntüle")
            print("2. Para Yatır")
            print("3. Para Çek")
            print("4. İşlem Geçmişi")
            print("5. Çıkış")

            secim = input("Seçiminiz: ")

            if secim == "1":
                self.bakiye_goster()
            elif secim == "2":
                self.para_yatir()
            elif secim == "3":
                self.para_cek()
            elif secim == "4":
                self.gecmis_goster()
            elif secim == "5":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim.")

if __name__ == "__main__":
    atm = MedATM()
    if atm.giris():
        atm.menu()
