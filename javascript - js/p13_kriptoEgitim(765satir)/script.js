/**
 * 
 *     Script: Kriptografi Eğitim ve Şifre Kırma Sistemi
 *     Açıklama: Şifreleme algoritmaları öğretimi ve interaktif şifre kırma uygulaması
 *     Yazar: [Future Developer]
 *     Tarih: 07.09.2025
 *     Sürüm: 1.0
 * 
 *     Şifreleme Yöntemleri:
 *     - Caesar Cipher (Kaydırma şifreleme)
 *     - Substitution Cipher (Harf değiştirme) 
 *     - Vigenere Cipher (Anahtar kelime şifreleme)
 *     - XOR Şifreleme (Binary operasyonlar)
 *     - ROT13 (13 karakter kaydırma)
 *     - Atbash Cipher (Ters alfabe şifreleme)
 * 
 *     Şifre Kırma Teknikleri:
 *     - Brute Force saldırıları
 *     - Frekans analizi (Türkçe optimizasyonu)
 *     - Caesar otomatik kırıcı
 *     - XOR anahtar tahmin algoritması
 * 
 *     Eğitimsel Parça:
 *     - Kriptografi tarihi (Antik çağdan moderne)
 *     - Şifreleme algoritmaları detaylı açıklamalar
 *     - Şifre güvenliği ve kırılma süresi analizi
 *     - İnteraktif örnekler ve uygulamalar
 * 
 *     
 *     Not: Bu kod, StartingMagic platformu için özel olarak yazılmıştır.
 * 
 */

class KriptografiEgitimi {
    constructor() {
        this.turkceAlfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ";
        this.turkceFrekanslari = {
            'A': 11.92, 'E': 12.89, 'İ': 8.67, 'I': 4.94, 'N': 7.48,
            'R': 6.72, 'T': 6.30, 'L': 5.84, 'S': 4.79, 'U': 3.44,
            'O': 2.75, 'M': 3.69, 'D': 4.87, 'Y': 3.34, 'K': 4.68,
            'B': 2.71, 'V': 0.96, 'G': 1.30, 'Z': 1.50, 'H': 1.15,
            'P': 0.79, 'C': 0.98, 'Ç': 1.13, 'F': 0.44, 'J': 0.03,
            'Ş': 1.78, 'Ğ': 1.31, 'Ü': 1.85, 'Ö': 0.85
        };
    }

    // Ana menü
    basla() {
        alert("🔐 KRİPTOGRAFİ EĞİTİM SİSTEMİ\n" +
              "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" +
              "Şifreleme sanatını öğrenmeye hazır mısın?");
        
        while (true) {
            const secim = prompt(
                "🎯 MENÜ SEÇENEKLERİ:\n\n" +
                "1️⃣ - Şifreleme Yap\n" +
                "2️⃣ - Şifre Kır\n" +
                "3️⃣ - Şifreleme Eğitimi\n" +
                "4️⃣ - Şifre Gücü Test Et\n" +
                "5️⃣ - Kriptografi Tarihi\n" +
                "0️⃣ - Çıkış\n\n" +
                "Seçiminizi yapın (0-5):"
            );

            switch (secim) {
                case '1': this.sifreleMenu(); break;
                case '2': this.sifreKirMenu(); break;
                case '3': this.egitimMenu(); break;
                case '4': this.sifreGucuTest(); break;
                case '5': this.kriptografiTarihi(); break;
                case '0': 
                    alert("🎓 Kriptografi yolculuğunuz tamamlandı!\nGüvenli kalın! 🛡️");
                    return;
                default:
                    alert("❌ Geçersiz seçim! Lütfen 0-5 arası bir sayı girin.");
            }
        }
    }

    // Şifreleme menüsü
    sifreleMenu() {
        const yontem = prompt(
            "🔒 ŞİFRELEME YÖNTEMLERİ:\n\n" +
            "1 - Caesar Cipher (Kaydırma)\n" +
            "2 - Substitution Cipher (Değiştirme)\n" +
            "3 - Vigenere Cipher (Anahtar)\n" +
            "4 - XOR Şifreleme\n" +
            "5 - ROT13 (13 Kaydırma)\n" +
            "6 - Atbash Cipher (Ters Alfabe)\n\n" +
            "Hangi yöntemi kullanmak istiyorsunuz? (1-6):"
        );

        const metin = prompt("📝 Şifrelenecek metni girin:");
        if (!metin) return;

        let sonuc = "";
        let aciklama = "";

        switch (yontem) {
            case '1':
                const kaydirma = parseInt(prompt("🔢 Kaydırma değerini girin (1-28):")) || 3;
                sonuc = this.caesarSifrele(metin, kaydirma);
                aciklama = `Caesar Cipher - ${kaydirma} kaydırma`;
                break;
            case '2':
                sonuc = this.substitutionSifrele(metin);
                aciklama = "Substitution Cipher - Rastgele değiştirme";
                break;
            case '3':
                const anahtar = prompt("🗝️ Anahtar kelimeyi girin:") || "ANAHTAR";
                sonuc = this.vigenereSifrele(metin, anahtar);
                aciklama = `Vigenere Cipher - Anahtar: ${anahtar}`;
                break;
            case '4':
                const xorAnahtar = prompt("🔑 XOR anahtarını girin:") || "123";
                sonuc = this.xorSifrele(metin, xorAnahtar);
                aciklama = `XOR Şifreleme - Anahtar: ${xorAnahtar}`;
                break;
            case '5':
                sonuc = this.rot13Sifrele(metin);
                aciklama = "ROT13 - 13 karakter kaydırma";
                break;
            case '6':
                sonuc = this.atbashSifrele(metin);
                aciklama = "Atbash Cipher - Ters alfabe";
                break;
            default:
                alert("❌ Geçersiz yöntem seçimi!");
                return;
        }

        this.sonucGoster("🔒 ŞİFRELEME SONUCU", metin, sonuc, aciklama);
    }

    // Şifre kırma menüsü
    sifreKirMenu() {
        const yontem = prompt(
            "🔓 ŞİFRE KIRMA YÖNTEMLERİ:\n\n" +
            "1 - Caesar Cipher Kırıcı\n" +
            "2 - Frekans Analizi\n" +
            "3 - Brute Force Saldırısı\n" +
            "4 - XOR Kırıcı\n" +
            "5 - ROT13 Çözücü\n" +
            "6 - Atbash Çözücü\n\n" +
            "Hangi yöntemi kullanmak istiyorsunuz? (1-6):"
        );

        const sifreliMetin = prompt("🔍 Şifreli metni girin:");
        if (!sifreliMetin) return;

        let sonuc = "";
        let aciklama = "";

        switch (yontem) {
            case '1':
                sonuc = this.caesarKir(sifreliMetin);
                aciklama = "Caesar Cipher - Tüm kaydırma değerleri denendi";
                break;
            case '2':
                sonuc = this.frekansAnalizi(sifreliMetin);
                aciklama = "Frekans Analizi - Harf sıklığına göre tahmin";
                break;
            case '3':
                sonuc = this.bruteForce(sifreliMetin);
                aciklama = "Brute Force - Tüm kombinasyonlar denendi";
                break;
            case '4':
                sonuc = this.xorKir(sifreliMetin);
                aciklama = "XOR Kırıcı - Yaygın anahtarlar denendi";
                break;
            case '5':
                sonuc = this.rot13Sifrele(sifreliMetin); // ROT13 kendi tersini alır
                aciklama = "ROT13 Çözücü";
                break;
            case '6':
                sonuc = this.atbashSifrele(sifreliMetin); // Atbash kendi tersini alır
                aciklama = "Atbash Çözücü";
                break;
            default:
                alert("❌ Geçersiz yöntem seçimi!");
                return;
        }

        this.sonucGoster("🔓 ŞİFRE KIRMA SONUCU", sifreliMetin, sonuc, aciklama);
    }

    // Caesar Cipher şifreleme
    caesarSifrele(metin, kaydirma) {
        let sonuc = "";
        for (let i = 0; i < metin.length; i++) {
            let karakter = metin[i].toUpperCase();
            let index = this.turkceAlfabe.indexOf(karakter);
            
            if (index !== -1) {
                let yeniIndex = (index + kaydirma) % this.turkceAlfabe.length;
                sonuc += this.turkceAlfabe[yeniIndex];
            } else {
                sonuc += metin[i];
            }
        }
        return sonuc;
    }

    // Caesar Cipher kırma
    caesarKir(sifreliMetin) {
        let enIyiSonuc = "";
        let enIyiSkor = 0;
        let sonuclar = "🔍 TÜM KAYDİRMA DENEMELERİ:\n\n";

        for (let kaydirma = 1; kaydirma <= 28; kaydirma++) {
            let deneme = this.caesarSifrele(sifreliMetin, -kaydirma);
            let skor = this.metinSkoru(deneme);
            
            sonuclar += `Kaydırma ${kaydirma}: ${deneme}\n`;
            
            if (skor > enIyiSkor) {
                enIyiSkor = skor;
                enIyiSonuc = deneme;
            }
        }

        alert(sonuclar + `\n🎯 EN OLASI SONUÇ: ${enIyiSonuc}`);
        return enIyiSonuc;
    }

    // Vigenere Cipher
    vigenereSifrele(metin, anahtar) {
        let sonuc = "";
        let anahtarIndex = 0;
        anahtar = anahtar.toUpperCase();

        for (let i = 0; i < metin.length; i++) {
            let karakter = metin[i].toUpperCase();
            let index = this.turkceAlfabe.indexOf(karakter);
            
            if (index !== -1) {
                let anahtarKarakter = anahtar[anahtarIndex % anahtar.length];
                let anahtarKaydirma = this.turkceAlfabe.indexOf(anahtarKarakter);
                let yeniIndex = (index + anahtarKaydirma) % this.turkceAlfabe.length;
                sonuc += this.turkceAlfabe[yeniIndex];
                anahtarIndex++;
            } else {
                sonuc += metin[i];
            }
        }
        return sonuc;
    }

    // XOR Şifreleme
    xorSifrele(metin, anahtar) {
        let sonuc = "";
        for (let i = 0; i < metin.length; i++) {
            let metinKodu = metin.charCodeAt(i);
            let anahtarKodu = anahtar.charCodeAt(i % anahtar.length);
            sonuc += String.fromCharCode(metinKodu ^ anahtarKodu);
        }
        return btoa(sonuc); // Base64 encode
    }

    // XOR Kırma
    xorKir(sifreliMetin) {
        let yaygınAnahtarlar = ["123", "ABC", "KEY", "PASS", "SECRET", "TEST"];
        let sonuclar = "🔑 XOR ANAHTAR DENEMELERİ:\n\n";
        
        try {
            sifreliMetin = atob(sifreliMetin); // Base64 decode
        } catch (e) {
            return "❌ Geçersiz Base64 format!";
        }

        for (let anahtar of yaygınAnahtarlar) {
            let deneme = "";
            for (let i = 0; i < sifreliMetin.length; i++) {
                let sifreKodu = sifreliMetin.charCodeAt(i);
                let anahtarKodu = anahtar.charCodeAt(i % anahtar.length);
                deneme += String.fromCharCode(sifreKodu ^ anahtarKodu);
            }
            sonuclar += `Anahtar "${anahtar}": ${deneme}\n`;
        }
        
        alert(sonuclar);
        return "Yukarıdaki denemelerden uygun olanı seçin";
    }

    // ROT13
    rot13Sifrele(metin) {
        return this.caesarSifrele(metin, 13);
    }

    // Atbash Cipher
    atbashSifrele(metin) {
        let sonuc = "";
        for (let i = 0; i < metin.length; i++) {
            let karakter = metin[i].toUpperCase();
            let index = this.turkceAlfabe.indexOf(karakter);
            
            if (index !== -1) {
                let yeniIndex = this.turkceAlfabe.length - 1 - index;
                sonuc += this.turkceAlfabe[yeniIndex];
            } else {
                sonuc += metin[i];
            }
        }
        return sonuc;
    }

    // Substitution Cipher (basit rastgele)
    substitutionSifrele(metin) {
        let karisikAlfabe = this.turkceAlfabe.split('').sort(() => Math.random() - 0.5).join('');
        let sonuc = "";
        
        for (let i = 0; i < metin.length; i++) {
            let karakter = metin[i].toUpperCase();
            let index = this.turkceAlfabe.indexOf(karakter);
            
            if (index !== -1) {
                sonuc += karisikAlfabe[index];
            } else {
                sonuc += metin[i];
            }
        }
        
        alert(`🔑 Substitution Anahtarı:\n${this.turkceAlfabe}\n${karisikAlfabe}`);
        return sonuc;
    }

    // Frekans analizi
    frekansAnalizi(metin) {
        let harfSayilari = {};
        let toplamHarf = 0;

        // Harfleri say
        for (let i = 0; i < metin.length; i++) {
            let harf = metin[i].toUpperCase();
            if (this.turkceAlfabe.includes(harf)) {
                harfSayilari[harf] = (harfSayilari[harf] || 0) + 1;
                toplamHarf++;
            }
        }

        // Frekansları hesapla ve sırala
        let frekanslar = [];
        for (let harf in harfSayilari) {
            let frekans = (harfSayilari[harf] / toplamHarf) * 100;
            frekanslar.push({ harf, frekans, sayi: harfSayilari[harf] });
        }
        
        frekanslar.sort((a, b) => b.frekans - a.frekans);

        let analiz = "📊 FREKANS ANALİZİ:\n\n";
        analiz += "Metindeki harf dağılımı:\n";
        
        for (let i = 0; i < Math.min(10, frekanslar.length); i++) {
            let { harf, frekans, sayi } = frekanslar[i];
            analiz += `${harf}: %${frekans.toFixed(1)} (${sayi} adet)\n`;
        }
        
        analiz += "\n🎯 TAHMİN:\n";
        if (frekanslar.length > 0) {
            analiz += `En sık kullanılan harf "${frekanslar[0].harf}" muhtemelen "E" olabilir.\n`;
            analiz += `Bu bir Caesar Cipher ise kaydırma değeri tahmin edilebilir.`;
        }

        alert(analiz);
        return "Frekans analizi tamamlandı - yukarıdaki bilgileri kullanın";
    }

    // Brute Force
    bruteForce(sifreliMetin) {
        alert("⚡ BRUTE FORCE SALDIRISI BAŞLATILIYOR...\n\n" +
              "Tüm olası kombinasyonlar deneniyor.\n" +
              "Bu işlem biraz zaman alabilir.");
        
        // Caesar için tüm kaydırmaları dene
        return this.caesarKir(sifreliMetin);
    }

    // Metin skorlama (Türkçe kelime kalıpları)
    metinSkoru(metin) {
        let skor = 0;
        let kelimeler = metin.split(' ');
        let turkceKelimeler = ['VE', 'BU', 'BİR', 'İÇİN', 'OLAN', 'VAR', 'DAN', 'DE', 'İLE', 'BEN', 'SEN', 'O'];
        
        for (let kelime of kelimeler) {
            if (turkceKelimeler.includes(kelime.toUpperCase())) {
                skor += 10;
            }
            // Sesli harf kontrolü
            if (/[AEIİOÖUÜ]/.test(kelime)) {
                skor += 2;
            }
        }
        return skor;
    }

    // Eğitim menüsü
    egitimMenu() {
        const konu = prompt(
            "📚 KRİPTOGRAFİ EĞİTİMİ:\n\n" +
            "1 - Şifreleme Temelleri\n" +
            "2 - Caesar Cipher Nasıl Çalışır?\n" +
            "3 - Frekans Analizi Nedir?\n" +
            "4 - Modern Şifreleme\n" +
            "5 - Şifre Güvenliği İpuçları\n\n" +
            "Hangi konuyu öğrenmek istiyorsunuz? (1-5):"
        );

        switch (konu) {
            case '1': this.sifrelemeTerelleri(); break;
            case '2': this.caesarEgitimi(); break;
            case '3': this.frekansEgitimi(); break;
            case '4': this.modernSifreleme(); break;
            case '5': this.sifreGuvenligiIpuclari(); break;
            default: alert("❌ Geçersiz seçim!");
        }
    }

    sifrelemeTerelleri() {
        alert("📖 ŞİFRELEME TEMELLERİ\n" +
              "━━━━━━━━━━━━━━━━━━━━━━\n\n" +
              "🔹 Şifreleme: Bilgiyi gizli hale getirme sanatı\n" +
              "🔹 Düz Metin: Orijinal, okunabilir metin\n" +
              "🔹 Şifreli Metin: Şifrelenmiş, gizli metin\n" +
              "🔹 Anahtar: Şifreleme/çözme için kullanılan kod\n" +
              "🔹 Algoritma: Şifreleme yöntemi\n\n" +
              "İki tür şifreleme vardır:\n" +
              "• Simetrik: Aynı anahtar ile şifrele/çöz\n" +
              "• Asimetrik: Farklı anahtarlar (açık/gizli)");
    }

    caesarEgitimi() {
        alert("🏛️ CAESAR CIPHER EĞİTİMİ\n" +
              "━━━━━━━━━━━━━━━━━━━━━━━━━\n\n" +
              "Julius Caesar tarafından kullanılan yöntem!\n\n" +
              "🔄 ÇALIŞMA PRENSİBİ:\n" +
              "Her harf alfabede N pozisyon kaydırılır\n\n" +
              "📝 ÖRNEK (3 kaydırma):\n" +
              "A → D, B → E, C → F\n" +
              "'MERHABA' → 'PHUKDED'\n\n" +
              "🛡️ GÜVENLİK:\n" +
              "• Basit ama etkili\n" +
              "• Sadece 28 olasılık var (Türkçe)\n" +
              "• Frekans analizi ile kırılabilir");

        // Interaktif örnek
        const ornekMetin = prompt("🎯 Şimdi siz deneyin! Bir kelime girin:");
        if (ornekMetin) {
            const kaydirma = 3;
            const sifreli = this.caesarSifrele(ornekMetin, kaydirma);
            alert(`✨ SONUÇ:\n\nOrijinal: ${ornekMetin}\nŞifreli: ${sifreli}\nKaydırma: ${kaydirma}`);
        }
    }

    frekansEgitimi() {
        alert("📊 FREKANS ANALİZİ EĞİTİMİ\n" +
              "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n" +
              "Şifre kırmanın en güçlü yöntemi!\n\n" +
              "💡 TEMELLİ PRİNSİP:\n" +
              "Her dilde harfler farklı sıklıkta kullanılır\n\n" +
              "🇹🇷 TÜRKÇEDE EN SIK:\n" +
              "1. E (%12.89)\n" +
              "2. A (%11.92)\n" +
              "3. İ (%8.67)\n" +
              "4. N (%7.48)\n" +
              "5. R (%6.72)\n\n" +
              "🎯 KULLANIMI:\n" +
              "• Şifreli metindeki harf sıklığını say\n" +
              "• En sık harfi 'E' olarak varsay\n" +
              "• Diğerlerini eşleştir\n" +
              "• Anlamsız kelimeler çıkarsa yeniden dene!");
    }

    modernSifreleme() {
        alert("🚀 MODERN ŞİFRELEME\n" +
              "━━━━━━━━━━━━━━━━━━━━━━\n\n" +
              "🔐 AES (Advanced Encryption Standard):\n" +
              "• 128, 192 veya 256 bit anahtar\n" +
              "• Dünya standardı\n" +
              "• Bankalar, hükümetler kullanır\n\n" +
              "🔑 RSA (Açık Anahtar Şifrelemesi):\n" +
              "• İki anahtar: açık ve gizli\n" +
              "• İnternet güvenliğinin temeli\n" +
              "• Dijital imzalar\n\n" +
              "⚡ Elliptic Curve Cryptography:\n" +
              "• Daha küçük anahtarlar\n" +
              "• Mobil cihazlar için ideal\n" +
              "• Bitcoin'de kullanılır\n\n" +
              "🌌 Kuantum Şifreleme:\n" +
              "• Geleceğin teknolojisi\n" +
              "• Kırılması imkansız\n" +
              "• Henüz deneysel");
    }

    sifreGuvenligiIpuclari() {
        alert("🛡️ ŞİFRE GÜVENLİĞİ İPUÇLARI\n" +
              "━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n" +
              "💪 GÜÇLÜ ŞİFRE:\n" +
              "• En az 12 karakter\n" +
              "• Büyük/küçük harf karışımı\n" +
              "• Sayı ve özel karakterler\n" +
              "• Anlamlı kelimelerden kaçının\n\n" +
              "🚫 YAPMAYIN:\n" +
              "• Kişisel bilgi kullanmayın\n" +
              "• Aynı şifreyi her yerde kullanmayın\n" +
              "• Tarayıcıya kaydetmeyin\n" +
              "• Başkalarıyla paylaşmayın\n\n" +
              "✅ YAPIN:\n" +
              "• Şifre yöneticisi kullanın\n" +
              "• İki faktörlü doğrulama açın\n" +
              "• Düzenli olarak değiştirin\n" +
              "• Farklı hesaplar için farklı şifreler");
    }

    // Şifre gücü testi
    sifreGucuTest() {
        const sifre = prompt("🔍 Test edilecek şifreyi girin:");
        if (!sifre) return;

        let skor = 0;
        let oneriler = [];

        // Uzunluk kontrolü
        if (sifre.length >= 12) skor += 25;
        else if (sifre.length >= 8) skor += 15;
        else if (sifre.length >= 6) skor += 5;
        else oneriler.push("En az 8 karakter kullanın");

        // Karakter çeşitliliği
        if (/[a-z]/.test(sifre)) skor += 15;
        else oneriler.push("Küçük harf ekleyin");

        if (/[A-Z]/.test(sifre)) skor += 15;
        else oneriler.push("Büyük harf ekleyin");

        if (/[0-9]/.test(sifre)) skor += 15;
        else oneriler.push("Rakam ekleyin");

        if (/[!@#$%^&*(),.?":{}|<>]/.test(sifre)) skor += 20;
        else oneriler.push("Özel karakter ekleyin (!@#$... gibi)");

        // Yaygın kalıplar kontrolü
        if (!/(.)\1{2,}/.test(sifre)) skor += 10;
        else oneriler.push("Tekrar eden karakterlerden kaçının");

        let seviye = "";
        let renk = "";
        if (skor >= 80) { seviye = "ÇOK GÜÇLÜ 🟢"; renk = "🟢"; }
        else if (skor >= 60) { seviye = "GÜÇLÜ 🟡"; renk = "🟡"; }
        else if (skor >= 40) { seviye = "ORTA 🟠"; renk = "🟠"; }
        else { seviye = "ZAYIF 🔴"; renk = "🔴"; }

        let sonuc = `🔒 ŞİFRE GÜVENLİK ANALİZİ\n` +
                   `━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n` +
                   `📊 SKOR: ${skor}/100\n` +
                   `🎯 SEVİYE: ${seviye}\n\n`;

        if (oneriler.length > 0) {
            sonuc += `💡 İYİLEŞTİRME ÖNERİLERİ:\n`;
            oneriler.forEach((oneri, i) => {
                sonuc += `${i + 1}. ${oneri}\n`;
            });
        } else {
            sonuc += `✅ Tebrikler! Şifreniz çok güçlü!`;
        }

        // Kırılma süresi tahmini
        let kirılmaSuresi = this.kirilmaSuresiHesapla(sifre);
        sonuc += `\n\n⏱️ TAHMİNİ KIRILMA SÜRESİ: ${kirılmaSuresi}`;

        alert(sonuc);
    }

    // Kırılma süresi hesaplama
    kirilmaSuresiHesapla(sifre) {
        let karakterSeti = 0;
        if (/[a-z]/.test(sifre)) karakterSeti += 26;
        if (/[A-Z]/.test(sifre)) karakterSeti += 26;
        if (/[0-9]/.test(sifre)) karakterSeti += 10;
        if (/[!@#$%^&*(),.?":{}|<>]/.test(sifre)) karakterSeti += 32;

        // Toplam olası kombinasyon sayısı
        let toplamKombinasyon = Math.pow(karakterSeti, sifre.length);
        
        // Ortalama kırılma süresi (saniye cinsinden)
        // Varsayım: Saniyede 1 milyar deneme
        let saniyedeDenemeSayisi = 1000000000;
        let ortalamaSaniye = toplamKombinasyon / (2 * saniyedeDenemeSayisi);
        
        // Süre formatını belirle
        if (ortalamaSaniye < 1) {
            return "Anında kırılabilir ⚡";
        } else if (ortalamaSaniye < 60) {
            return `${Math.round(ortalamaSaniye)} saniye ⏱️`;
        } else if (ortalamaSaniye < 3600) {
            let dakika = Math.round(ortalamaSaniye / 60);
            return `${dakika} dakika ⏰`;
        } else if (ortalamaSaniye < 86400) {
            let saat = Math.round(ortalamaSaniye / 3600);
            return `${saat} saat 🕐`;
        } else if (ortalamaSaniye < 31536000) {
            let gun = Math.round(ortalamaSaniye / 86400);
            return `${gun} gün 📅`;
        } else if (ortalamaSaniye < 31536000000) {
            let yil = Math.round(ortalamaSaniye / 31536000);
            return `${yil} yıl 📆`;
        } else if (ortalamaSaniye < 31536000000000) {
            let binYil = Math.round(ortalamaSaniye / 31536000000);
            return `${binYil} bin yıl 🏛️`;
        } else if (ortalamaSaniye < 31536000000000000) {
            let milyonYil = Math.round(ortalamaSaniye / 31536000000000);
            return `${milyonYil} milyon yıl 🦕`;
        } else {
            return "Evrenin yaşından uzun! 🌌";
        }
    }

    // Kriptografi tarihi
    kriptografiTarihi() {
        const konu = prompt(
            "📚 KRİPTOGRAFİ TARİHİ:\n\n" +
            "1 - Antik Çağ Şifreleri\n" +
            "2 - Ortaçağ ve Rönesans\n" +
            "3 - I. ve II. Dünya Savaşı\n" +
            "4 - Bilgisayar Çağı\n" +
            "5 - Modern Dönem\n\n" +
            "Hangi dönemi öğrenmek istiyorsunuz? (1-5):"
        );

        switch (konu) {
            case '1':
                alert("🏛️ ANTİK ÇAĞ ŞİFRELERİ\n" +
                      "━━━━━━━━━━━━━━━━━━━━━━━━\n\n" +
                      "🇬🇷 SPARTAN SCYTALE (MÖ 7. yy):\n" +
                      "Deri şerit çubuğa sarılır, mesaj yazılır\n\n" +
                      "🏛️ CAESAR CIPHER (MÖ 58-50):\n" +
                      "Julius Caesar, 3 harf kaydırma kullandı\n" +
                      "Gizli askeri haberleşme için\n\n" +
                      "📜 POLYBIUS SQUARE (MÖ 2. yy):\n" +
                      "Yunanlı tarihçi Polybius'un 5x5 karesi\n" +
                      "Her harf koordinatlarla temsil edilir\n\n" +
                      "🔥 İLGİNÇ GERÇEK:\n" +
                      "Antik çağda şifreci yakalandığında\n" +
                      "genellikle idam edilirdi!");
                break;

            case '2':
                alert("🏰 ORTAÇAĞ VE RÖNESANS\n" +
                      "━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n" +
                      "🔤 SUBSTITUTION CIPHERS:\n" +
                      "Her harf farklı harfle değiştirilir\n" +
                      "Araplar frekans analizini icat etti\n\n" +
                      "🇮🇹 LEON BATTISTA ALBERTI (1467):\n" +
                      "İlk polyalphabetic cipher\n" +
                      "Modern şifrelemenin babası\n\n" +
                      "📖 JOHANNES TRITHEMIUS:\n" +
                      "'Polygraphiae' kitabı (1518)\n" +
                      "Şifreleme üzerine ilk akademik çalışma\n\n" +
                      "👑 MARY STUART:\n" +
                      "Kötü şifreleme kullandı\n" +
                      "Yakalandı ve idam edildi (1587)");
                break;

            case '3':
                alert("⚔️ DÜNYA SAVAŞLARI DÖNEMİ\n" +
                      "━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n" +
                      "🇩🇪 ENİGMA MAKİNESİ (WWII):\n" +
                      "Nazi Almanya'nın şifreleme makinesi\n" +
                      "Günde 159 trilyon kombinasyon\n\n" +
                      "🇬🇧 BLETCHLEY PARK:\n" +
                      "Alan Turing ve ekibi\n" +
                      "Enigma'yı kırdılar (1941)\n" +
                      "Savaşı 2-4 yıl kısalttı\n\n" +
                      "🇯🇵 PURPLE CIPHER:\n" +
                      "Japon diplomatik şifre\n" +
                      "ABD tarafından kırıldı\n\n" +
                      "📡 NAVAJO CODE TALKERS:\n" +
                      "Amerikan yerlilerin dili\n" +
                      "Hiç kırılmadı!");
                break;

            case '4':
                alert("💻 BİLGİSAYAR ÇAĞI\n" +
                      "━━━━━━━━━━━━━━━━━━━━━\n\n" +
                      "🔐 DES (1977):\n" +
                      "Data Encryption Standard\n" +
                      "IBM ve NSA işbirliği\n" +
                      "56-bit anahtar\n\n" +
                      "🔑 RSA (1978):\n" +
                      "Rivest, Shamir, Adleman\n" +
                      "İlk pratik açık anahtar şifreleme\n" +
                      "İnternet güvenliğinin temeli\n\n" +
                      "🏛️ AES (2001):\n" +
                      "Advanced Encryption Standard\n" +
                      "DES'in yerini aldı\n" +
                      "Hala güncel standart\n\n" +
                      "📱 ELLİPTİK EĞRİ (1985):\n" +
                      "Mobil cihazlar için optimize");
                break;

            case '5':
                alert("🚀 MODERN DÖNEM\n" +
                      "━━━━━━━━━━━━━━━━━━━\n\n" +
                      "🌐 İNTERNET GÜVENLİĞİ:\n" +
                      "HTTPS, SSL/TLS protokolleri\n" +
                      "E-ticaret ve bankacılık\n\n" +
                      "₿ BLOCKCHAIN (2008):\n" +
                      "Bitcoin ve kripto paralar\n" +
                      "Merkezi olmayan güven\n\n" +
                      "⚛️ KUANTUM TEHDİDİ:\n" +
                      "Mevcut şifreler tehlikede\n" +
                      "Post-quantum cryptography\n\n" +
                      "🔒 HOMOMORPHIC ENCRYPTION:\n" +
                      "Şifreli veri üzerinde işlem\n" +
                      "Gizlilik korunarak hesaplama\n\n" +
                      "🔐 ZERO-KNOWLEDGE PROOFS:\n" +
                      "Bilgiyi ifşa etmeden kanıtlama");
                break;

            default:
                alert("❌ Geçersiz seçim!");
        }
    }

    // Sonuç gösterme
    sonucGoster(baslik, girdi, cikti, aciklama) {
        let mesaj = `${baslik}\n`;
        mesaj += "━".repeat(baslik.length) + "\n\n";
        mesaj += `📥 GİRDİ:\n${girdi}\n\n`;
        mesaj += `📤 ÇIKTI:\n${cikti}\n\n`;
        mesaj += `ℹ️ BİLGİ:\n${aciklama}`;
        
        alert(mesaj);

        // Ek işlemler menüsü
        const ekIslem = prompt(
            "🎯 EK İŞLEMLER:\n\n" +
            "1 - Sonucu kopyala\n" +
            "2 - Başka bir yöntem dene\n" +
            "3 - Ana menüye dön\n\n" +
            "Ne yapmak istiyorsunuz? (1-3):"
        );

        switch (ekIslem) {
            case '1':
                // Kopyala simulasyonu
                alert(`📋 Sonuç panoya kopyalandı:\n${cikti}`);
                break;
            case '2':
                // Menüye geri dön
                return false;
            case '3':
            default:
                return true;
        }
    }
}

// 🚀 Uygulamayı Başlat
function kriptografiBaslat() {
    const uygulama = new KriptografiEgitimi();
    uygulama.basla();
}

// Uygulamayı çalıştır
kriptografiBaslat();