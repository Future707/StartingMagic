'''
    Script: 13_ogrenciNotSistemi.py
    Açıklama: Öğrenci notlarını kaydeden, ortalama hesaplayan ve başarı durumlarını raporlayan sistem.
    Yazar: [Future Developer]
    Tarih: [05.07.2025]
    Sürüm: 1.06
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
'''

import json
import os

class Ogrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.notlar = []

    def not_ekle(self, ders, puan):
        self.notlar.append({"ders": ders, "puan": puan})

    def ortalama(self):
        if not self.notlar:
            return 0
        return sum([n["puan"] for n in self.notlar]) / len(self.notlar)

    def durum(self):
        ort = self.ortalama()
        if ort >= 85:
            return "Başarılı - Pekiyi"
        elif ort >= 70:
            return "Başarılı"
        elif ort >= 50:
            return "Geçti"
        else:
            return "Kaldı"

    def to_dict(self):
        return {
            "ad": self.ad,
            "soyad": self.soyad,
            "numara": self.numara,
            "notlar": self.notlar
        }

    @staticmethod
    def from_dict(data):
        ogr = Ogrenci(data["ad"], data["soyad"], data["numara"])
        ogr.notlar = data["notlar"]
        return ogr

class OgrenciNotSistemi:
    def __init__(self, dosya="ogrenciler.json"):
        self.dosya = dosya
        self.ogrenciler = []
        self.yukle()

    def yukle(self):
        if os.path.exists(self.dosya):
            with open(self.dosya, "r", encoding="utf-8") as f:
                veriler = json.load(f)
                self.ogrenciler = [Ogrenci.from_dict(v) for v in veriler]

    def kaydet(self):
        with open(self.dosya, "w", encoding="utf-8") as f:
            json.dump([o.to_dict() for o in self.ogrenciler], f, ensure_ascii=False, indent=4)

    def ogrenci_ekle(self, ad, soyad, numara):
        ogr = Ogrenci(ad, soyad, numara)
        self.ogrenciler.append(ogr)
        self.kaydet()

    def not_ekle(self, numara, ders, puan):
        for ogr in self.ogrenciler:
            if ogr.numara == numara:
                ogr.not_ekle(ders, puan)
                self.kaydet()
                return True
        return False

    def rapor(self, numara):
        for ogr in self.ogrenciler:
            if ogr.numara == numara:
                print(f"\nRapor - {ogr.ad} {ogr.soyad} ({ogr.numara})")
                for n in ogr.notlar:
                    print(f"{n['ders']}: {n['puan']}")
                print(f"Ortalama: {ogr.ortalama():.2f}")
                print(f"Durum: {ogr.durum()}")
                return
        print("Öğrenci bulunamadı.")

    def listele(self):
        print("\nTüm Öğrenciler:")
        for ogr in self.ogrenciler:
            print(f"{ogr.numara} - {ogr.ad} {ogr.soyad} - Ortalama: {ogr.ortalama():.2f} - {ogr.durum()}")


def menu():
    sistem = OgrenciNotSistemi()
    while True:
        print("\n--- Öğrenci Not Sistemi ---")
        print("1. Öğrenci Ekle")
        print("2. Not Ekle")
        print("3. Rapor Al")
        print("4. Öğrencileri Listele")
        print("5. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            numara = input("Numara: ")
            sistem.ogrenci_ekle(ad, soyad, numara)
            print("Öğrenci eklendi.")

        elif secim == "2":
            numara = input("Öğrenci numarası: ")
            ders = input("Ders adı: ")
            try:
                puan = float(input("Puan: "))
            except ValueError:
                print("Geçersiz puan girdiniz.")
                continue
            if sistem.not_ekle(numara, ders, puan):
                print("Not eklendi.")
            else:
                print("Öğrenci bulunamadı.")

        elif secim == "3":
            numara = input("Öğrenci numarası: ")
            sistem.rapor(numara)

        elif secim == "4":
            sistem.listele()

        elif secim == "5":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    menu()
