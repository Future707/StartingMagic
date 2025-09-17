"""
Script: p17_kutuphaneFuture.py
Açıklama: FutureX kütüphane sistemi - kullanıcı kayıtları, kitap ödünç alma, iade, arama, listeleme.
Yazar: [Future Developer]
Tarih: [01.09.2025]
Sürüm: 1.00
Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import json
import os

DATA_FILE = "futurex_library.json"

class Kutuphane:
    def __init__(self, sahibi="Elon Musk", adi="FutureX"):
        self.sahibi = sahibi
        self.adi = adi
        self.kitaplar = []
        self.uyeler = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.kitaplar = data.get("kitaplar", [])
                self.uyeler = data.get("uyeler", [])
        else:
            self.varsayilan_kitaplar_yukle()
            self.save_data()

    def save_data(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({"kitaplar": self.kitaplar, "uyeler": self.uyeler}, f, ensure_ascii=False, indent=4)

    def varsayilan_kitaplar_yukle(self):
        self.kitaplar = [
            {"title": "Python Programlamaya Giriş", "author": "Guido van Rossum", "category": "Programlama", "count": 5},
            {"title": "Java: Temelleri", "author": "James Gosling", "category": "Programlama", "count": 3},
            {"title": "Makine Öğrenmesi 101", "author": "Andrew Ng", "category": "Yapay Zeka", "count": 4},
            {"title": "Derin Öğrenme", "author": "Ian Goodfellow", "category": "Yapay Zeka", "count": 2},
            {"title": "Uzay Yolculuğu", "author": "Carl Sagan", "category": "Bilim", "count": 6},
            {"title": "Zamanın Kısa Tarihi", "author": "Stephen Hawking", "category": "Bilim", "count": 4},
            {"title": "Ben, Robot", "author": "Isaac Asimov", "category": "Bilimkurgu", "count": 5},
            {"title": "1984", "author": "George Orwell", "category": "Roman", "count": 5},
            {"title": "Suç ve Ceza", "author": "Fyodor Dostoyevski", "category": "Roman", "count": 3},
            {"title": "Sefiller", "author": "Victor Hugo", "category": "Roman", "count": 2},
            {"title": "Sherlock Holmes", "author": "Arthur Conan Doyle", "category": "Dedektif", "count": 5},
            {"title": "Kayıp Zamanın İzinde", "author": "Marcel Proust", "category": "Roman", "count": 2},
            {"title": "Yapay Zeka ve Gelecek", "author": "Nick Bostrom", "category": "Yapay Zeka", "count": 4},
            {"title": "Elon Musk: Tesla, SpaceX", "author": "Ashlee Vance", "category": "Biyografi", "count": 6},
            {"title": "Steve Jobs", "author": "Walter Isaacson", "category": "Biyografi", "count": 3},
            {"title": "Benjamin Franklin", "author": "Walter Isaacson", "category": "Biyografi", "count": 2},
            {"title": "İnovasyon ve Gelecek", "author": "Peter Thiel", "category": "İş Dünyası", "count": 4},
            {"title": "Zero to One", "author": "Peter Thiel", "category": "İş Dünyası", "count": 4},
            {"title": "Zengin Baba Yoksul Baba", "author": "Robert Kiyosaki", "category": "Kişisel Gelişim", "count": 5},
            {"title": "Alışkanlıkların Gücü", "author": "Charles Duhigg", "category": "Kişisel Gelişim", "count": 3},
            {"title": "Matematiksel Düşünme", "author": "Terence Tao", "category": "Matematik", "count": 3},
            {"title": "Fizik 101", "author": "Richard Feynman", "category": "Bilim", "count": 4},
            {"title": "Astronomi Rehberi", "author": "Neil deGrasse Tyson", "category": "Bilim", "count": 4},
            {"title": "Mars Günlükleri", "author": "Ray Bradbury", "category": "Bilimkurgu", "count": 3},
            {"title": "Dune", "author": "Frank Herbert", "category": "Bilimkurgu", "count": 3},
            {"title": "Vakıf", "author": "Isaac Asimov", "category": "Bilimkurgu", "count": 4},
            {"title": "Geleceğin Kısa Tarihi", "author": "Yuval Noah Harari", "category": "Bilim", "count": 5},
            {"title": "Hayvan Çiftliği", "author": "George Orwell", "category": "Roman", "count": 3},
            {"title": "Cesur Yeni Dünya", "author": "Aldous Huxley", "category": "Roman", "count": 3},
            {"title": "Körlük", "author": "José Saramago", "category": "Roman", "count": 2},
            {"title": "Simyacı", "author": "Paulo Coelho", "category": "Roman", "count": 4},
            {"title": "Satranç", "author": "Stefan Zweig", "category": "Roman", "count": 3},
            {"title": "Yeraltından Notlar", "author": "Dostoyevski", "category": "Roman", "count": 2},
            {"title": "Çocukluğun Soğuk Geceleri", "author": "Tezer Özlü", "category": "Roman", "count": 2},
            {"title": "Kürk Mantolu Madonna", "author": "Sabahattin Ali", "category": "Roman", "count": 3},
            {"title": "Tutunamayanlar", "author": "Oğuz Atay", "category": "Roman", "count": 3},
            {"title": "Bir Bilim Adamının Romanı", "author": "Oğuz Atay", "category": "Biyografi", "count": 2},
            {"title": "Matematiksel Yolculuk", "author": "Cédric Villani", "category": "Matematik", "count": 3},
            {"title": "Kriptografi 101", "author": "Bruce Schneier", "category": "Bilgisayar", "count": 3},
            {"title": "Bilgisayar Ağları", "author": "Andrew Tanenbaum", "category": "Bilgisayar", "count": 3},
            {"title": "Veri Bilimine Giriş", "author": "Joel Grus", "category": "Programlama", "count": 4},
            {"title": "Algoritmalar", "author": "Thomas H. Cormen", "category": "Programlama", "count": 3},
            {"title": "Clean Code", "author": "Robert C. Martin", "category": "Programlama", "count": 3},
            {"title": "Design Patterns", "author": "Erich Gamma", "category": "Programlama", "count": 3},
            {"title": "Refactoring", "author": "Martin Fowler", "category": "Programlama", "count": 2},
            {"title": "Pragmatic Programmer", "author": "Andy Hunt", "category": "Programlama", "count": 2},
            {"title": "Etkili İnsanların 7 Alışkanlığı", "author": "Stephen Covey", "category": "Kişisel Gelişim", "count": 3},
            {"title": "İkna Psikolojisi", "author": "Robert Cialdini", "category": "Kişisel Gelişim", "count": 2},
            {"title": "Kara Delikler", "author": "Stephen Hawking", "category": "Bilim", "count": 3},
            {"title": "Evrenin Yapısı", "author": "Brian Greene", "category": "Bilim", "count": 3},
            {"title": "Astrofizik 101", "author": "Michio Kaku", "category": "Bilim", "count": 3},
            {"title": "Paralel Evrenler", "author": "Max Tegmark", "category": "Bilim", "count": 2},
        ]

    def kitaplari_listele(self):
        print(f"\n📚 {self.adi} Kütüphanesi - Kitap Listesi:")
        for i, kitap in enumerate(self.kitaplar, 1):
            print(f"{i}. {kitap['title']} - {kitap['author']} ({kitap['category']}) | Adet: {kitap['count']}")

    def uye_ekle(self, isim):
        if isim not in self.uyeler:
            self.uyeler.append(isim)
            print(f"{isim} kütüphaneye üye oldu!")
            self.save_data()
        else:
            print("Bu isim zaten üye.")

    def kitap_al(self, uye, aranan):
        if uye not in self.uyeler:
            print("Önce üye olun.")
            return

        eslesenler = [k for k in self.kitaplar if aranan.lower() in k['title'].lower()]
        if not eslesenler:
            print("Bu isimle eşleşen kitap yok.")
            return

        print("\nEşleşen kitaplar:")
        for i, kitap in enumerate(eslesenler, 1):
            print(f"{i}. {kitap['title']} - {kitap['author']} (Adet: {kitap['count']})")

        secim = input("Numara girin: ")
        if not secim.isdigit() or not (1 <= int(secim) <= len(eslesenler)):
            print("Geçersiz seçim.")
            return

        kitap = eslesenler[int(secim) - 1]
        if kitap["count"] > 0:
            kitap["count"] -= 1
            print(f"{uye}, {kitap['title']} kitabını aldı.")
            self.save_data()
        else:
            print("Kitap kalmamış.")

    def kitap_iade(self, uye, aranan):
        eslesenler = [k for k in self.kitaplar if aranan.lower() in k['title'].lower()]
        if not eslesenler:
            print("Böyle bir kitap yok.")
            return
        kitap = eslesenler[0]
        kitap["count"] += 1
        print(f"{uye}, {kitap['title']} kitabını iade etti.")
        self.save_data()


def main():
    kutuphane = Kutuphane()

    while True:
        print("\nFutureX Kütüphane Sistemi")
        print("1. Üye Ol")
        print("2. Kitap Al")
        print("3. Kitap İade Et")
        print("4. Kitapları Listele")
        print("5. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("İsim girin: ")
            kutuphane.uye_ekle(isim)

        elif secim == "2":
            uye = input("İsminizi girin: ")
            aranan = input("Kitap isminin bir kısmını yazın: ")
            kutuphane.kitap_al(uye, aranan)

        elif secim == "3":
            uye = input("İsminizi girin: ")
            aranan = input("Kitap isminin bir kısmını yazın: ")
            kutuphane.kitap_iade(uye, aranan)

        elif secim == "4":
            kutuphane.kitaplari_listele()

        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
