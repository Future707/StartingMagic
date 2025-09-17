"""
    Script: 05_TurtleKullanımı.py
    Açıklama: Turtle kütüphanesi ile grafik çizim ve geometrik şekiller uygulaması.
    Yazar: [Future Developer]
    Tarih: [09.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
"""

import turtle
import math
import random
import colorsys

print("TURTLE GRAFIK CIZIM UYGULAMALARI")
print("=" * 40)

# --- ORTAK KURULUM ---
def turtle_kurulum():
    """Turtle penceresini hazırla"""
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("StartingMagic - Turtle Graphics")
    screen.setup(800, 600)

    pen = turtle.Turtle()
    pen.speed(0)  # En hızlı
    pen.shape("turtle")

    return screen, pen

# --- TEMEL ŞEKİLLER ---
def temel_sekiller():
    try:
        print("\nTEMEL ŞEKILLER CIZILIYOR...")
        screen, pen = turtle_kurulum()

        pen.penup()
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]
        color_index = 0

        def cizim_yap(x, y):
            nonlocal color_index
            pen.goto(x, y)
            pen.pendown()
            pen.color(colors[color_index % len(colors)])
            pen.circle(10)
            pen.penup()
            color_index += 1

        screen.onclick(cizim_yap)
        screen.listen()
        screen.exitonclick()
    except Exception as e:
        print(f"[HATA] Temel şekiller çizilirken sorun oluştu: {e}")

# --- GEOMETRİK SANAT ---
def geometrik_sanat():
    try:
        print("\nGEOMETRIK SANAT CIZILIYOR...")
        screen, pen = turtle_kurulum()

        for i in range(50):
            pen.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))
            pen.penup()
            pen.goto(random.randint(-300, 300), random.randint(-200, 200))
            pen.pendown()
            sekil = random.choice(["kare", "ucgen", "daire"])
            boyut = random.randint(10, 50)

            if sekil == "kare":
                for _ in range(4):
                    pen.forward(boyut)
                    pen.right(90)
            elif sekil == "ucgen":
                for _ in range(3):
                    pen.forward(boyut)
                    pen.right(120)
            else:
                pen.circle(boyut // 2)

        screen.exitonclick()
    except Exception as e:
        print(f"[HATA] Geometrik sanat çiziminde problem: {e}")

# --- MATEMATİK FONKSİYONLARI ---
def matematik_fonksiyonlari():
    try:
        print("\nMATEMATIK FONKSIYONLARI GRAFIGI...")
        screen, pen = turtle_kurulum()

        # Eksenler
        pen.color("gray")
        pen.width(1)
        pen.penup(); pen.goto(-400, 0); pen.pendown(); pen.goto(400, 0)
        pen.penup(); pen.goto(0, -300); pen.pendown(); pen.goto(0, 300)

        # Sin
        pen.color("red"); pen.width(2); pen.penup()
        for x in range(-360, 361, 5):
            y = 100 * math.sin(math.radians(x))
            if x == -360:
                pen.goto(x, y); pen.pendown()
            else:
                pen.goto(x, y)

        # Cos
        pen.color("blue"); pen.penup()
        for x in range(-360, 361, 5):
            y = 100 * math.cos(math.radians(x))
            if x == -360:
                pen.goto(x, y); pen.pendown()
            else:
                pen.goto(x, y)

        screen.exitonclick()
    except Exception as e:
        print(f"[HATA] Matematik fonksiyonları çiziminde hata: {e}")

# --- INTERAKTİF ÇİZİM ---
def interaktif_cizim():
    try:
        print("\nINTERAKTIF CIZIM MODU")
        print("Fareyle tıklayarak çizim yapın!")
        print("Pencereyi kapatmak için herhangi bir yere tıklayın.")

        screen, pen = turtle_kurulum()
        pen.penup()
        pen.color("blue")

        def ciz(x, y):
            try:
                pen.goto(x, y)
                pen.pendown()
                pen.circle(10)
                pen.penup()
            except Exception as e:
                print(f"[HATA] Çizim sırasında sorun: {e}")

        screen.onclick(ciz)
        screen.exitonclick()
    except Exception as e:
        print(f"[HATA] İnteraktif çizim başlatılamadı: {e}")

# --- ANA PROGRAM ---
def main():
    while True:
        print("\n" + "=" * 40)
        print("TURTLE GRAFIK CIZIM UYGULAMALARI")
        print("=" * 40)
        print("1. Temel Şekiller")
        print("2. Geometrik Sanat")
        print("3. Matematik Fonksiyonları")
        print("4. İnteraktif Çizim")
        print("5. Çıkış")

        try:
            secim = int(input("Seçiminiz (1-5): "))

            if secim == 1:
                temel_sekiller()
            elif secim == 2:
                geometrik_sanat()
            elif secim == 3:
                matematik_fonksiyonlari()
            elif secim == 4:
                interaktif_cizim()
            elif secim == 5:
                print("Programdan çıkılıyor...")
                break
            else:
                print("Geçersiz seçim!")
        except ValueError:
            print("Lütfen sayı girin (1-5).")
        except KeyboardInterrupt:
            print("\nKullanıcı çıkış yaptı.")
            break
        except Exception as e:
            print(f"[GENEL HATA] {e}")

if __name__ == "__main__":
    main()
