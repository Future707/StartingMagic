# 
#     Script: 16_detayliAtm.py
#     Açıklama: Gelişmiş ATM simülasyonu. Çoklu para birimi desteği (TRY, USD, EUR), kullanıcı hesap girişi (hesap no + PIN), bakiye görüntüleme, para yatırma/çekme, para transferi (aynı bankadaki farklı hesaplara), döviz dönüşümü ile para çekme/yatırma, işlem geçmişi, basit admin paneli (döviz kurları güncelleme, kullanıcı yönetimi) ve veritabanı için JSON kalıcılığı içerir.
#     Yazar: [Future Developer]
#     Tarih: [11.07.2025]
#     Sürüm: 1.00
#     Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
#       
#     Dosyayı çalıştırdığnız dizininizde big_atm_db.json dosyası 
#     kullanıcı bilgisini ve verisini saklamak için oluşturulacaktır... 
#

import json
import os
import time
import getpass
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

DB_FILE = "big_atm_db.json"
SUPPORTED_CURRENCIES = ["TRY", "USD", "EUR"]


def moneyfmt(amount):
    # Decimal ile düzgün yuvarlama
    d = Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"{d:.2f}"


class BankDB:
    def __init__(self, path=DB_FILE):
        self.path = path
        self.data = {"accounts": {}, "rates": {"USD": 0.05, "EUR": 0.045}, "next_acc": 2001}
        # rates: 1 TRY -> X foreign (i.e. 1 TRY = 0.05 USD means 1 USD = 20 TRY)
        # store rates as quote per 1 TRY to currency
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            # bootstrap with two demo accounts
            self.data["accounts"] = {
                "1001": {"name": "Ali Veli", "pin": "1234", "balances": {"TRY": 2000.0, "USD": 50.0, "EUR": 10.0}, "history": []},
                "1002": {"name": "Ayşe Demir", "pin": "4321", "balances": {"TRY": 500.0, "USD": 0.0, "EUR": 5.0}, "history": []}
            }
            self.data["next_acc"] = 2001
            self.save()

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def create_account(self, name, pin):
        acc_no = str(self.data.get("next_acc", 2001))
        self.data["next_acc"] = int(acc_no) + 1
        self.data["accounts"][acc_no] = {"name": name, "pin": pin, "balances": {c: 0.0 for c in SUPPORTED_CURRENCIES}, "history": []}
        self.save()
        return acc_no

    def get_account(self, acc_no):
        return self.data["accounts"].get(acc_no)

    def set_rate(self, currency, rate_per_try):
        # rate_per_try: how much of currency equals 1 TRY (e.g., 0.05 USD per TRY)
        self.data["rates"][currency] = rate_per_try
        self.save()

    def get_rate(self, currency):
        return self.data["rates"].get(currency)


class BigATM:
    def __init__(self):
        self.db = BankDB()
        self.current_account = None

    # ---------- Utility ----------
    def timestamp(self):
        return datetime.now().isoformat(sep=' ', timespec='seconds')

    def record(self, acc_no, text):
        acc = self.db.get_account(acc_no)
        if acc is None:
            return
        acc["history"].append({"time": self.timestamp(), "text": text})
        self.db.save()

    # ---------- Authentication ----------
    def login(self):
        print("Giriş için hesap numarası ve PIN giriniz.")
        acc_no = input("Hesap No: ").strip()
        if acc_no == "admin":
            pin = getpass.getpass("Admin şifresi: ")
            if pin == "admin":
                print("Admin olarak giriş yapıldı.")
                self.current_account = "admin"
                return True
            else:
                print("Admin şifresi hatalı.")
                return False
        acc = self.db.get_account(acc_no)
        if not acc:
            print("Hesap bulunamadı.")
            return False
        pin = getpass.getpass("PIN: ")
        if pin == acc.get("pin"):
            self.current_account = acc_no
            print(f"{acc.get('name')} hesabına giriş yapıldı.")
            return True
        else:
            print("Hatalı PIN.")
            return False

    def logout(self):
        self.current_account = None

    # ---------- Account Operations ----------
    def show_balances(self, acc_no=None):
        if acc_no is None:
            acc_no = self.current_account
        acc = self.db.get_account(acc_no)
        print(f"Hesap: {acc_no} - {acc.get('name')}")
        for cur, amt in acc["balances"].items():
            print(f"  {cur}: {moneyfmt(amt)}")

    def deposit(self):
        acc_no = self.current_account
        acc = self.db.get_account(acc_no)
        cur = input(f"Para birimi {SUPPORTED_CURRENCIES}: ").strip().upper()
        if cur not in SUPPORTED_CURRENCIES:
            print("Desteklenmeyen para birimi.")
            return
        try:
            amount = float(input("Miktar: "))
        except ValueError:
            print("Geçersiz sayı.")
            return
        if amount <= 0:
            print("Miktar pozitif olmalı.")
            return
        acc["balances"][cur] += amount
        self.record(acc_no, f"Depozit: +{moneyfmt(amount)} {cur}")
        print("İşlem kaydedildi.")

    def withdraw(self):
        acc_no = self.current_account
        acc = self.db.get_account(acc_no)
        cur = input(f"Çekmek istediğiniz para birimi {SUPPORTED_CURRENCIES}: ").strip().upper()
        if cur not in SUPPORTED_CURRENCIES:
            print("Desteklenmeyen para birimi.")
            return
        try:
            amount = float(input("Miktar: "))
        except ValueError:
            print("Geçersiz sayı.")
            return
        if amount <= 0:
            print("Miktar pozitif olmalı.")
            return
        if acc["balances"][cur] < amount:
            # attempt to convert from TRY or other currencies if allowed
            print("Bu para biriminde yeterli bakiye yok.")
            choice = input("Diğer birimlerden otomatik dönüşüm ile çekmek ister misiniz? (e/h): ").strip().lower()
            if choice != 'e':
                return
            # try to find funds by converting other balances (greedy approach: TRY first)
            needed = amount - acc["balances"][cur]
            success = self.attempt_cross_currency_withdraw(acc, cur, needed)
            if not success:
                print("Yeterli toplam fon bulunamadı.")
                return
        acc["balances"][cur] -= amount
        self.record(acc_no, f"Çekme: -{moneyfmt(amount)} {cur}")
        print("Çekme başarılı.")

    def attempt_cross_currency_withdraw(self, acc, target_cur, needed_amount):
        # Convert other currencies into target_cur using rates and consume
        # needed_amount is in target_cur units
        # We'll check all other currencies and convert TRY first for simplicity
        # rates: stored as X foreign per 1 TRY
        # To convert from currency A to target_cur:
        #   normalize A -> TRY -> target_cur
        balances = acc["balances"]
        # calculate total available in target_cur
        total_available = balances[target_cur]
        rate_try_to_target = self.db.get_rate(target_cur) if target_cur != 'TRY' else 1.0
        # try using TRY balance
        if balances["TRY"] > 0:
            # TRY -> target_cur
            try_in_target = balances["TRY"] * rate_try_to_target
            use_try = min(try_in_target, needed_amount)
            if use_try > 0:
                # deduct equivalent TRY
                try_needed_try = use_try / rate_try_to_target if rate_try_to_target != 0 else 0
                balances["TRY"] -= try_needed_try
                total_available += use_try
                needed_amount -= use_try
        # if still needed, use other foreign balances converting via TRY
        for cur in [c for c in SUPPORTED_CURRENCIES if c not in (target_cur, 'TRY')]:
            if needed_amount <= 0:
                break
            cur_balance = balances[cur]
            if cur_balance <= 0:
                continue
            # cur -> TRY: since rates are TRY -> cur (x cur per 1 TRY), 1 cur = 1 / rate TRY
            rate_try_to_cur = self.db.get_rate(cur)
            if not rate_try_to_cur or rate_try_to_cur == 0:
                continue
            # cur in target_cur: cur_amount * (TRY per cur) * (target_cur per TRY)
            try_per_cur = 1.0 / rate_try_to_cur
            cur_in_target = cur_balance * try_per_cur * (self.db.get_rate(target_cur) if target_cur != 'TRY' else 1.0)
            use_cur_in_target = min(cur_in_target, needed_amount)
            if use_cur_in_target > 0:
                # convert needed back to cur to deduct
                cur_needed = use_cur_in_target / (try_per_cur * (self.db.get_rate(target_cur) if target_cur != 'TRY' else 1.0))
                balances[cur] -= cur_needed
                needed_amount -= use_cur_in_target
                total_available += use_cur_in_target
        # if after conversions needed_amount <= 0, success
        if needed_amount <= 0:
            return True
        return False

    def transfer(self):
        src = self.current_account
        dst = input("Hesap numarası (hedef): ").strip()
        if dst == src:
            print("Kendinize transfer yapamazsınız.")
            return
        dst_acc = self.db.get_account(dst)
        if not dst_acc:
            print("Hedef hesap bulunamadı.")
            return
        cur = input(f"Para birimi {SUPPORTED_CURRENCIES}: ").strip().upper()
        if cur not in SUPPORTED_CURRENCIES:
            print("Desteklenmeyen para birimi.")
            return
        try:
            amount = float(input("Miktar: "))
        except ValueError:
            print("Geçersiz miktar.")
            return
        acc = self.db.get_account(src)
        if acc["balances"][cur] < amount:
            print("Yetersiz bakiye.")
            return
        acc["balances"][cur] -= amount
        dst_acc["balances"][cur] += amount
        self.record(src, f"Transfer: -{moneyfmt(amount)} {cur} -> {dst}")
        self.record(dst, f"Transfer alındı: +{moneyfmt(amount)} {cur} from {src}")
        print("Transfer başarılı.")

    def show_history(self, acc_no=None):
        if acc_no is None:
            acc_no = self.current_account
        acc = self.db.get_account(acc_no)
        print(f"İşlem geçmişi - {acc_no} - {acc.get('name')}")
        for h in acc["history"]:
            print(f"{h['time']} - {h['text']}")
        if not acc["history"]:
            print("İşlem bulunamadı.")

    # ---------- Admin ----------
    def admin_menu(self):
        while True:
            print("\n--- ADMIN PANELI ---")
            print("1 - Döviz kurlarını göster")
            print("2 - Döviz kuru güncelle")
            print("3 - Kullanıcı oluştur")
            print("4 - Tüm kullanıcıları listele")
            print("0 - Geri")
            ch = input("Seçim: ")
            if ch == '1':
                for cur, r in self.db.data.get('rates', {}).items():
                    # Show as 1 CUR = X TRY for readability
                    if r == 0:
                        print(f"{cur}: rate undefined")
                        continue
                    try_per_cur = 1.0 / r
                    print(f"1 {cur} = {moneyfmt(try_per_cur)} TRY (internal: {r} {cur}/TRY)")
            elif ch == '2':
                cur = input("Güncellenecek para (USD/EUR): ").strip().upper()
                if cur not in SUPPORTED_CURRENCIES or cur == 'TRY':
                    print("Geçersiz para birimi.")
                    continue
                try:
                    val = float(input("Yeni kur (örnek: 0.05 -> 1 TRY = 0.05 USD): "))
                except ValueError:
                    print("Geçersiz sayı.")
                    continue
                self.db.set_rate(cur, val)
                print("Kurlar güncellendi.")
            elif ch == '3':
                name = input("Yeni kullanıcı adı: ")
                pin = getpass.getpass("PIN (4 haneli önerilir): ")
                acc_no = self.db.create_account(name, pin)
                print(f"Kullanıcı oluşturuldu: {acc_no}")
            elif ch == '4':
                for no, acc in self.db.data['accounts'].items():
                    print(f"{no} - {acc['name']} - Balances: {', '.join([f'{c}:{moneyfmt(v)}' for c,v in acc['balances'].items()])}")
            elif ch == '0':
                break
            else:
                print("Geçersiz seçim.")

    # ---------- Main Menu Handlers ----------
    def user_menu(self):
        while True:
            print("\n--- MedATM (Gelişmiş) ---")
            print("1 - Bakiye Görüntüle")
            print("2 - Para Yatır (hesap içi)")
            print("3 - Para Çek")
            print("4 - Transfer")
            print("5 - İşlem Geçmişi")
            print("6 - Çıkış")
            choice = input("Seçim: ")
            if choice == '1':
                self.show_balances()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.transfer()
            elif choice == '5':
                self.show_history()
            elif choice == '6':
                self.logout()
                break
            else:
                print("Geçersiz seçim.")

    def main_loop(self):
        while True:
            print("\n=== MedATM Gelişmiş ===")
            print("1 - Giriş")
            print("2 - Yeni Hesap Oluştur")
            print("0 - Çıkış")
            sel = input("Seçim: ")
            if sel == '1':
                if self.login():
                    if self.current_account == 'admin':
                        self.admin_menu()
                        self.logout()
                    else:
                        self.user_menu()
                else:
                    print("Giriş başarısız.")
            elif sel == '2':
                name = input("Ad Soyad: ")
                pin = getpass.getpass("PIN (4 haneli önerilir): ")
                acc_no = self.db.create_account(name, pin)
                print(f"Hesap oluşturuldu. Hesap No: {acc_no}")
            elif sel == '0':
                print("Çıkış yapılıyor.")
                break
            else:
                print("Geçersiz seçim.")


if __name__ == '__main__':
    atm = BigATM()
    atm.main_loop()
