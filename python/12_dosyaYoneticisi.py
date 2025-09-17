# /* 
#     Script: 12_dosyaYoneticisi.py
#     Açıklama: Konsol tabanlı mini dosya yöneticisi. Klasör ve dosya listeleme, oluşturma, silme, yeniden adlandırma ve taşıma işlemleri yapılabilir.
#     Yazar: [Future Developer]
#     Tarih: [03.07.2025]
#     Sürüm: 1.00
#     Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
# */

import os
import shutil

class DosyaYoneticisi:
    def __init__(self):
        self.cwd = os.getcwd()

    def listele(self):
        print(f"Mevcut klasör: {self.cwd}")
        try:
            with os.scandir(self.cwd) as it:
                for entry in it:
                    tip = "[DIR]" if entry.is_dir() else "[FILE]"
                    print(f"{tip} {entry.name}")
        except Exception as e:
            print("Hata:", e)

    def klasor_degistir(self, path):
        new_path = os.path.join(self.cwd, path)
        if os.path.isdir(new_path):
            self.cwd = os.path.abspath(new_path)
            print("Klasör değiştirildi:", self.cwd)
        else:
            print("Böyle bir klasör yok.")

    def klasor_olustur(self, name):
        try:
            os.mkdir(os.path.join(self.cwd, name))
            print("Klasör oluşturuldu.")
        except Exception as e:
            print("Hata:", e)

    def dosya_olustur(self, name, content=""):
        try:
            with open(os.path.join(self.cwd, name), "w", encoding="utf-8") as f:
                f.write(content)
            print("Dosya oluşturuldu.")
        except Exception as e:
            print("Hata:", e)

    def dosya_sil(self, name):
        try:
            os.remove(os.path.join(self.cwd, name))
            print("Dosya silindi.")
        except Exception as e:
            print("Hata:", e)

    def klasor_sil(self, name):
        try:
            shutil.rmtree(os.path.join(self.cwd, name))
            print("Klasör ve içindekiler silindi.")
        except Exception as e:
            print("Hata:", e)

    def yeniden_adlandir(self, eski, yeni):
        try:
            os.rename(os.path.join(self.cwd, eski), os.path.join(self.cwd, yeni))
            print("Ad değiştirildi.")
        except Exception as e:
            print("Hata:", e)

    def tasi(self, kaynak, hedef):
        try:
            shutil.move(os.path.join(self.cwd, kaynak), os.path.join(self.cwd, hedef))
            print("Taşıma başarılı.")
        except Exception as e:
            print("Hata:", e)


def menu():
    dy = DosyaYoneticisi()
    while True:
        print("\n--- DOSYA YÖNETİCİSİ ---")
        print("1 - Listele")
        print("2 - Klasör Değiştir")
        print("3 - Klasör Oluştur")
        print("4 - Dosya Oluştur")
        print("5 - Dosya Sil")
        print("6 - Klasör Sil")
        print("7 - Yeniden Adlandır")
        print("8 - Taşı")
        print("0 - Çıkış")
        secim = input("Seçiminiz: ")
        if secim == "1":
            dy.listele()
        elif secim == "2":
            path = input("Klasör adı: ")
            dy.klasor_degistir(path)
        elif secim == "3":
            name = input("Yeni klasör adı: ")
            dy.klasor_olustur(name)
        elif secim == "4":
            name = input("Dosya adı: ")
            content = input("İçerik (boş bırakabilirsiniz): ")
            dy.dosya_olustur(name, content)
        elif secim == "5":
            name = input("Silinecek dosya adı: ")
            dy.dosya_sil(name)
        elif secim == "6":
            name = input("Silinecek klasör adı: ")
            dy.klasor_sil(name)
        elif secim == "7":
            eski = input("Eski ad: ")
            yeni = input("Yeni ad: ")
            dy.yeniden_adlandir(eski, yeni)
        elif secim == "8":
            kaynak = input("Taşınacak dosya/klasör adı: ")
            hedef = input("Hedef klasör: ")
            dy.tasi(kaynak, hedef)
        elif secim == "0":
            print("Çıkılıyor.")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    menu()