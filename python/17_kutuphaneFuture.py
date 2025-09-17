"""
Script: p17_kutuphaneFuture.py
Açıklama: FutureX kütüphane sistemi - kullanıcı kayıtları, kitap ödünç alma, iade, arama, listeleme, istatistikler, admin panel.
Yazar: [Future Developer]
Tarih: [01.09.2025]
Sürüm: 2.50 (Detaylı Eğitim Versiyonu - ~500 satır)
Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı örneğin geliştirilmiş halidir.
"""

import json
import os
import datetime

DATA_FILE = "futurex_library.json"
ADMIN_PASS = "admin123"


# ============================================================
# Yardımcı Fonksiyonlar
# ============================================================

def cls():
    """Konsolu temizler (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Devam etmek için enter bekler."""
    input("\nDevam etmek için Enter'a basın...")


def tarih():
    """Bugünün tarihini döndürür."""
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M")


# ============================================================
# Kutuphane Sınıfı
# ============================================================

class Kutuphane:
    def __init__(self, sahibi="Elon Musk", adi="FutureX"):
        self.sahibi = sahibi
        self.adi = adi
        self.kitaplar = []
        self.uyeler = []
        self.load_data()

    # ------------------ Data İşlemleri ------------------

    def load_data(self):
        """JSON dosyasından veri yükler."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.kitaplar = data.get("kitaplar", [])
                self.uyeler = data.get("uyeler", [])
        else:
            self.varsayilan_kitaplar_yukle()
            self.save_data()

    def save_data(self):
        """JSON dosyasına veri kaydeder."""
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(
                {"kitaplar": self.kitaplar, "uyeler": self.uyeler},
                f,
                ensure_ascii=False,
                indent=4
            )

    def varsayilan_kitaplar_yukle(self):
        """Varsayılan kitapları yükler."""
        self.kitaplar = [
            {"id": 1, "title": "Python Programlamaya Giriş", "author": "Guido van Rossum",
             "category": "Programlama", "year": 1991, "isbn": "978-0-12-345678-9",
             "desc": "Python diline başlangıç kitabı.", "count": 5, "taken": 0},

            {"id": 2, "title": "Makine Öğrenmesi 101", "author": "Andrew Ng",
             "category": "Yapay Zeka", "year": 2015, "isbn": "978-0-98-765432-1",
             "desc": "Makine öğrenmesine giriş ders kitabı.", "count": 4, "taken": 0},

            {"id": 3, "title": "Uzay Yolculuğu", "author": "Carl Sagan",
             "category": "Bilim", "year": 1980, "isbn": "978-1-23-456789-0",
             "desc": "Evreni ve uzay yolculuklarını anlatan popüler bilim eseri.", "count": 6, "taken": 0},
        ]

    # ------------------ Kitap İşlemleri ------------------

    def kitaplari_listele(self):
        """Tüm kitapları listeler."""
        print(f"\n📚 {self.adi} Kütüphanesi - Kitap Listesi:")
        for i, kitap in enumerate(self.kitaplar, 1):
            print(f"{i}. {kitap['title']} - {kitap['author']} ({kitap['category']}, {kitap['year']})"
                  f" | Adet: {kitap['count']} | Alınma: {kitap['taken']} kez")

    def kitap_ekle(self, title, author, category, year, isbn, desc, count=1):
        """Yeni kitap ekler (admin)."""
        yeni_id = max([k["id"] for k in self.kitaplar], default=0) + 1
        self.kitaplar.append({
            "id": yeni_id,
            "title": title,
            "author": author,
            "category": category,
            "year": year,
            "isbn": isbn,
            "desc": desc,
            "count": count,
            "taken": 0
        })
        print(f"✅ '{title}' eklendi.")
        self.save_data()

    def kitap_sil(self, kitap_id):
        """Kitap siler (admin)."""
        kitap = next((k for k in self.kitaplar if k["id"] == kitap_id), None)
        if kitap:
            self.kitaplar.remove(kitap)
            print(f"❌ '{kitap['title']}' silindi.")
            self.save_data()
        else:
            print("Böyle bir kitap yok.")

    def kitap_duzenle(self, kitap_id, yeni_bilgi):
        """Kitap bilgilerini düzenler (admin)."""
        for kitap in self.kitaplar:
            if kitap["id"] == kitap_id:
                kitap.update(yeni_bilgi)
                print(f"✏️ '{kitap['title']}' güncellendi.")
                self.save_data()
                return
        print("Kitap bulunamadı.")

    def kitap_arama(self, kelime):
        """Kitap arar (kullanıcı)."""
        eslesenler = [k for k in self.kitaplar if kelime.lower() in k['title'].lower()
                      or kelime.lower() in k['author'].lower()
                      or kelime.lower() in k['category'].lower()]
        return eslesenler

    # ------------------ Üye İşlemleri ------------------

    def uye_ekle(self, isim):
        """Yeni üye ekler."""
        if any(u["isim"] == isim for u in self.uyeler):
            print("⚠️ Bu isim zaten üye.")
            return
        self.uyeler.append({"isim": isim, "kayit": tarih(), "kitaplar": []})
        print(f"👤 {isim} kütüphaneye üye oldu!")
        self.save_data()

    def kitap_al(self, uye, kitap_id):
        """Üye kitap alır."""
        uye_data = next((u for u in self.uyeler if u["isim"] == uye), None)
        kitap = next((k for k in self.kitaplar if k["id"] == kitap_id), None)

        if not uye_data:
            print("⚠️ Önce üye olun.")
            return
        if not kitap:
            print("⚠️ Kitap bulunamadı.")
            return
        if kitap["count"] <= 0:
            print("⚠️ Kitap kalmamış.")
            return

        kitap["count"] -= 1
        kitap["taken"] += 1
        uye_data["kitaplar"].append({"id": kitap["id"], "title": kitap["title"], "aldigi_tarih": tarih()})
        print(f"📖 {uye}, '{kitap['title']}' kitabını aldı.")
        self.save_data()

    def kitap_iade(self, uye, kitap_id):
        """Üye kitap iade eder."""
        uye_data = next((u for u in self.uyeler if u["isim"] == uye), None)
        if not uye_data:
            print("⚠️ Önce üye olun.")
            return

        kitap = next((k for k in self.kitaplar if k["id"] == kitap_id), None)
        if not kitap:
            print("⚠️ Kitap bulunamadı.")
            return

        uye_kitap = next((bk for bk in uye_data["kitaplar"] if bk["id"] == kitap_id), None)
        if not uye_kitap:
            print("⚠️ Bu kitap sizde değil.")
            return

        kitap["count"] += 1
        uye_data["kitaplar"].remove(uye_kitap)
        print(f"📦 {uye}, '{kitap['title']}' kitabını iade etti.")
        self.save_data()

    # ------------------ İstatistikler ------------------

    def en_populer_kitaplar(self, n=3):
        """En çok alınan kitapları listeler."""
        sirali = sorted(self.kitaplar, key=lambda x: x["taken"], reverse=True)
        return sirali[:n]

    def aktif_uyeler(self, n=3):
        """En çok kitap almış üyeleri listeler."""
        sirali = sorted(self.uyeler, key=lambda u: len(u["kitaplar"]), reverse=True)
        return sirali[:n]


# ============================================================
# Kullanıcı Arayüzü
# ============================================================

def kullanici_menu(kutuphane: Kutuphane):
    while True:
        cls()
        print("\n===== 📚 FutureX Kütüphane - Kullanıcı Paneli =====")
        print("1. Üye Ol")
        print("2. Kitap Ara")
        print("3. Kitap Al")
        print("4. Kitap İade Et")
        print("5. Kitapları Listele")
        print("6. Çıkış")

        secim = input("Seçiminiz: ")
        if secim == "1":
            isim = input("İsim girin: ")
            kutuphane.uye_ekle(isim)
            pause()
        elif secim == "2":
            kelime = input("Aranacak kelime: ")
            sonuc = kutuphane.kitap_arama(kelime)
            for k in sonuc:
                print(f"{k['id']} - {k['title']} ({k['author']}) [{k['category']}]")
            pause()
        elif secim == "3":
            uye = input("İsminizi girin: ")
            kitap_id = int(input("Kitap ID: "))
            kutuphane.kitap_al(uye, kitap_id)
            pause()
        elif secim == "4":
            uye = input("İsminizi girin: ")
            kitap_id = int(input("Kitap ID: "))
            kutuphane.kitap_iade(uye, kitap_id)
            pause()
        elif secim == "5":
            kutuphane.kitaplari_listele()
            pause()
        elif secim == "6":
            break
        else:
            print("Geçersiz seçim.")
            pause()


def admin_menu(kutuphane: Kutuphane):
    while True:
        cls()
        print("\n===== 🔑 FutureX Kütüphane - Admin Panel =====")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Düzenle")
        print("4. İstatistikler")
        print("5. Çıkış")

        secim = input("Seçiminiz: ")
        if secim == "1":
            title = input("Kitap adı: ")
            author = input("Yazar: ")
            category = input("Kategori: ")
            year = int(input("Yıl: "))
            isbn = input("ISBN: ")
            desc = input("Açıklama: ")
            count = int(input("Adet: "))
            kutuphane.kitap_ekle(title, author, category, year, isbn, desc, count)
            pause()
        elif secim == "2":
            kitap_id = int(input("Silinecek kitap ID: "))
            kutuphane.kitap_sil(kitap_id)
            pause()
        elif secim == "3":
            kitap_id = int(input("Düzenlenecek kitap ID: "))
            yeni_bilgi = {}
            yeni_ad = input("Yeni isim (boş bırak geç): ")
            if yeni_ad:
                yeni_bilgi["title"] = yeni_ad
            yeni_yazar = input("Yeni yazar: ")
            if yeni_yazar:
                yeni_bilgi["author"] = yeni_yazar
            kutuphane.kitap_duzenle(kitap_id, yeni_bilgi)
            pause()
        elif secim == "4":
            print("📊 En popüler kitaplar:")
            for k in kutuphane.en_populer_kitaplar():
                print(f"{k['title']} ({k['taken']} kez alınmış)")
            print("\n👥 En aktif üyeler:")
            for u in kutuphane.aktif_uyeler():
                print(f"{u['isim']} ({len(u['kitaplar'])} kitap almış)")
            pause()
        elif secim == "5":
            break
        else:
            print("Geçersiz seçim.")
            pause()


# ============================================================
# Ana Program
# ============================================================

def main():
    kutuphane = Kutuphane()

    while True:
        cls()
        print("\n===== 🚀 FutureX Kütüphane Sistemi =====")
        print("1. Kullanıcı Paneli")
        print("2. Admin Paneli")
        print("3. Çıkış")

        secim = input("Seçiminiz: ")
        if secim == "1":
            kullanici_menu(kutuphane)
        elif secim == "2":
            sifre = input("Admin şifresi: ")
            if sifre == ADMIN_PASS:
                admin_menu(kutuphane)
            else:
                print("⚠️ Hatalı şifre.")
                pause()
        elif secim == "3":
            print("👋 Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")
            pause()


if __name__ == "__main__":
    main()
