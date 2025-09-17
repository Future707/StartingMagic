#  
#     Script: 11_quizMaster.py
#     Açıklama: Konsol tabanlı çoktan seçmeli bilgi yarışması. Kullanıcı puan toplar, yanlışları listelenir ve zamanlı mod seçenekleri vardır. Sorular JSON dosyasından yüklenir ve skorlar kaydedilir.
#     Yazar: [Future Developer]
#     Tarih: [01.07.2025]
#     Sürüm: 1.00
#     Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
#

import json
import os
import random
import time
from datetime import datetime

QUESTION_FILE = "questions.json"
SCORES_FILE = "quiz_scores.json"


class Question:
    def __init__(self, prompt, choices, answer, category=None, difficulty=None):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def display(self):
        print(self.prompt)
        for idx, ch in enumerate(self.choices, 1):
            print(f"  {idx}. {ch}")


class QuizMaster:
    def __init__(self):
        self.questions = []
        self.load_questions()
        self.scores = self.load_scores()

    def load_questions(self):
        if not os.path.exists(QUESTION_FILE):
            # create a small default set
            default_questions = [
                {
                    "prompt": "Python'da bir listenin sonuna eleman eklemek için hangi metot kullanılır?",
                    "choices": ["append", "add", "push", "insert"],
                    "answer": 1,
                    "category": "python",
                    "difficulty": "kolay",
                },
                {
                    "prompt": "Dünyanın en büyük okyanusu hangisidir?",
                    "choices": ["Hint Okyanusu", "Büyük Okyanus", "Atlantik", "Arktik"],
                    "answer": 2,
                    "category": "coğrafya",
                    "difficulty": "kolay",
                },
                {
                    "prompt": "HTML'de başlık etiketi hangi harfle başlar?",
                    "choices": ["H", "T", "B", "S"],
                    "answer": 1,
                    "category": "web",
                    "difficulty": "kolay",
                },
            ]
            with open(QUESTION_FILE, "w", encoding="utf-8") as f:
                json.dump(default_questions, f, ensure_ascii=False, indent=2)
        with open(QUESTION_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.questions = [Question(q["prompt"], q["choices"], q["answer"], q.get("category"), q.get("difficulty")) for q in data]

    def save_questions(self, questions_list):
        serializable = []
        for q in questions_list:
            serializable.append({
                "prompt": q.prompt,
                "choices": q.choices,
                "answer": q.answer,
                "category": q.category,
                "difficulty": q.difficulty,
            })
        with open(QUESTION_FILE, "w", encoding="utf-8") as f:
            json.dump(serializable, f, ensure_ascii=False, indent=2)

    def load_scores(self):
        if not os.path.exists(SCORES_FILE):
            return []
        with open(SCORES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_score(self, username, score, total, mode):
        entry = {
            "user": username,
            "score": score,
            "total": total,
            "mode": mode,
            "time": datetime.now().isoformat()
        }
        self.scores.append(entry)
        with open(SCORES_FILE, "w", encoding="utf-8") as f:
            json.dump(self.scores, f, ensure_ascii=False, indent=2)

    def add_question_interactive(self):
        prompt = input("Soru metni: ")
        choices = []
        print("Seçenekleri gir. Bitirmek için boş bırak.")
        while True:
            ch = input(f"Seçenek {len(choices)+1}: ")
            if ch.strip() == "":
                break
            choices.append(ch)
        if len(choices) < 2:
            print("En az iki seçenek girilmelidir.")
            return
        while True:
            try:
                ans = int(input("Doğru seçenek numarası (1-based): "))
                if 1 <= ans <= len(choices):
                    break
                else:
                    print("Geçersiz numara.")
            except ValueError:
                print("Sayı girin.")
        cat = input("Kategori (isteğe bağlı): ") or None
        diff = input("Zorluk (kolay/orta/zor) (isteğe bağlı): ") or None
        newq = Question(prompt, choices, ans, cat, diff)
        self.questions.append(newq)
        self.save_questions(self.questions)
        print("Soru kaydedildi.")

    def pick_questions(self, count=10, categories=None, difficulties=None):
        pool = self.questions[:]
        if categories:
            pool = [q for q in pool if q.category in categories]
        if difficulties:
            pool = [q for q in pool if q.difficulty in difficulties]
        if not pool:
            return []
        random.shuffle(pool)
        return pool[:min(count, len(pool))]

    def run_quiz(self, mode="standart"):
        print(f"Quiz modu: {mode}")
        username = input("Kullanıcı adı: ")
        try:
            num = int(input("Kaç soru olmalı? (varsayılan 10): ") or 10)
        except ValueError:
            num = 10
        qlist = self.pick_questions(count=num)
        if not qlist:
            print("Soru bulunamadı. Yeni sorular ekleyin.")
            return
        score = 0
        wrongs = []
        total_time = 0
        for i, q in enumerate(qlist, 1):
            print(f"\nSoru {i}/{len(qlist)}")
            q.display()
            if mode == "zamanli":
                limit = 10  # saniye
                print(f"Bu soru için {limit} saniyeniz var.")
                start = time.time()
                answer = self.get_answer_with_timeout(len(q.choices), limit)
                elapsed = time.time() - start
                total_time += elapsed
                if answer is None:
                    print("Süre doldu.")
                    wrongs.append((q, None))
                    continue
            else:
                start = time.time()
                answer = self.get_answer(len(q.choices))
                elapsed = time.time() - start
                total_time += elapsed
            if answer == q.answer:
                print("Doğru.")
                score += 1
            else:
                print(f"Yanlış. Doğru cevap: {q.answer}. {q.choices[q.answer-1]}")
                wrongs.append((q, answer))
        print("\nQuiz tamamlandı.")
        print(f"Puan: {score}/{len(qlist)}")
        avg_time = total_time / len(qlist) if qlist else 0
        print(f"Ortalama süre/soru: {avg_time:.2f}s")
        self.save_score(username, score, len(qlist), mode)
        if wrongs:
            print("\nYanlışlar:")
            for q, given in wrongs:
                print(f"- {q.prompt}")
                print(f"  Verilen: {given} | Doğru: {q.answer} - {q.choices[q.answer-1]}")

    def get_answer(self, max_choice):
        while True:
            a = input("Cevabınız (sayi): ")
            try:
                ai = int(a)
                if 1 <= ai <= max_choice:
                    return ai
                else:
                    print("Seçenek aralığında sayı girin.")
            except ValueError:
                print("Sayı girin.")

    def get_answer_with_timeout(self, max_choice, limit):
        # Basit timeout: kullanıcı süreyi aşarsa None döner. Bu implementasyon
        # tam olarak signal/timer kullanmıyor çünkü cross-platform sorunları var.
        # Burada her 0.1 saniyede kontrol edip input'a bakmak yerine, kullanıcının
        # zamanında cevaplaması beklenecek; alternatif olarak threading kullanılabilir.
        # Daha güvenilir bir yöntem için platforma özel kod yazılmalıdır.
        print("Cevap için girin ve Enter'a basın (zaman sayılıyor)...")
        start = time.time()
        # fallback: normal input, süreyi kontrol et
        try:
            a = input()
            if time.time() - start > limit:
                return None
            ai = int(a)
            if 1 <= ai <= max_choice:
                return ai
            else:
                return None
        except Exception:
            return None

    def show_leaderboard(self, top=10):
        if not self.scores:
            print("Henüz skor kaydı yok.")
            return
        sorted_scores = sorted(self.scores, key=lambda x: (x["score"]/x["total"]), reverse=True)
        print("Kelime sıralama (başarı oranına göre):")
        for i, entry in enumerate(sorted_scores[:top], 1):
            ratio = entry["score"]/entry["total"] if entry["total"] else 0
            print(f"{i}. {entry['user']} - {entry['score']}/{entry['total']} ({ratio:.2%}) - {entry['mode']} - {entry['time']}")

    def admin_menu(self):
        while True:
            print("\nAdmin Menüsü")
            print("1 - Soru Ekle")
            print("2 - Soruları Listele")
            print("3 - Soruları Kaydet")
            print("0 - Geri")
            ch = input("Seçiminiz: ")
            if ch == "1":
                self.add_question_interactive()
            elif ch == "2":
                for i, q in enumerate(self.questions, 1):
                    print(f"{i}. {q.prompt} (Kategori: {q.category} Zorluk: {q.difficulty})")
            elif ch == "3":
                self.save_questions(self.questions)
                print("Sorular kaydedildi.")
            elif ch == "0":
                break
            else:
                print("Geçersiz seçim.")


def main_menu():
    qm = QuizMaster()
    while True:
        print("\n--- QUIZ MASTER ---")
        print("1 - Quiz Başlat (standart)")
        print("2 - Quiz Başlat (zamanlı)")
        print("3 - Lider Tablosu")
        print("4 - Admin Menüsü")
        print("5 - Soruları Dışa Aktar (JSON)")
        print("0 - Çıkış")
        choice = input("Seçiminiz: ")
        if choice == "1":
            qm.run_quiz(mode="standart")
        elif choice == "2":
            qm.run_quiz(mode="zamanli")
        elif choice == "3":
            qm.show_leaderboard()
        elif choice == "4":
            qm.admin_menu()
        elif choice == "5":
            out = input("Dışa aktarılacak dosya adı (varsayılan export_questions.json): ") or "export_questions.json"
            qm.save_questions(qm.questions)
            os.replace(QUESTION_FILE, out) if os.path.exists(QUESTION_FILE) else None
            print(f"Sorular {out} olarak kaydedildi.")
        elif choice == "0":
            print("Çıkılıyor.")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == '__main__':
    main_menu()
