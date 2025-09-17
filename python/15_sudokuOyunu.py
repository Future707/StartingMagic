'''
    Script: 15_sudokuOyunu.py
    Açıklama: Konsol tabanlı Sudoku oyunu. Kullanıcı hamle yapar, sistem geçerliliğini kontrol eder ve çözümü doğrular.
    Yazar: [Future Developer]
    Tarih: [09.07.2025]
    Sürüm: 1.00
    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
'''

import random

class Sudoku:
    def __init__(self, boyut=9):
        self.boyut = boyut
        self.tahta = [[0 for _ in range(boyut)] for _ in range(boyut)]
        self.cozum = [[0 for _ in range(boyut)] for _ in range(boyut)]
        self.olustur()

    def gecerli(self, tahta, satir, sutun, sayi):
        for i in range(9):
            if tahta[satir][i] == sayi or tahta[i][sutun] == sayi:
                return False
        bas_satir, bas_sutun = (satir // 3) * 3, (sutun // 3) * 3
        for i in range(bas_satir, bas_satir + 3):
            for j in range(bas_sutun, bas_sutun + 3):
                if tahta[i][j] == sayi:
                    return False
        return True

    def sudoku_coz(self, tahta):
        for satir in range(9):
            for sutun in range(9):
                if tahta[satir][sutun] == 0:
                    for sayi in range(1, 10):
                        if self.gecerli(tahta, satir, sutun, sayi):
                            tahta[satir][sutun] = sayi
                            if self.sudoku_coz(tahta):
                                return True
                            tahta[satir][sutun] = 0
                    return False
        return True

    def olustur(self):
        self.sudoku_coz(self.cozum)
        self.tahta = [satir[:] for satir in self.cozum]
        bos_sayisi = 40
        while bos_sayisi > 0:
            satir, sutun = random.randint(0, 8), random.randint(0, 8)
            if self.tahta[satir][sutun] != 0:
                self.tahta[satir][sutun] = 0
                bos_sayisi -= 1

    def yazdir(self):
        for i, satir in enumerate(self.tahta):
            if i % 3 == 0 and i != 0:
                print("------+-------+------")
            for j, deger in enumerate(satir):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(deger if deger != 0 else ".", end=" ")
            print()

    def hamle(self, satir, sutun, sayi):
        if self.tahta[satir][sutun] == 0 and self.gecerli(self.tahta, satir, sutun, sayi):
            self.tahta[satir][sutun] = sayi
            return True
        return False

    def tamamlandi_mi(self):
        for satir in self.tahta:
            if 0 in satir:
                return False
        return True


def oyun():
    sudoku = Sudoku()
    print("Sudoku oyununa hoş geldiniz!")
    while not sudoku.tamamlandi_mi():
        sudoku.yazdir()
        try:
            satir = int(input("Satır (0-8): "))
            sutun = int(input("Sütun (0-8): "))
            sayi = int(input("Sayı (1-9): "))
        except ValueError:
            print("Geçersiz giriş.")
            continue

        if not (0 <= satir < 9 and 0 <= sutun < 9 and 1 <= sayi <= 9):
            print("Aralık dışında giriş.")
            continue

        if sudoku.hamle(satir, sutun, sayi):
            print("Hamle başarılı.")
        else:
            print("Geçersiz hamle.")

    print("Tebrikler! Sudoku'yu tamamladınız.")

if __name__ == "__main__":
    oyun()