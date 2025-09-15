/* 
    Script: Kelime Tahmin Oyunları Koleksiyonu
    Açıklama: Türkçe kelime tabanlı birden fazla tahmin oyunu
    Yazar: [Future Developer] 
    Tarih: 26.08.2025
    Sürüm: 1.0
    Satır Sayısı: ~280

    İçerilen Oyunlar:
    1. Klasik Adam Asmaca
    2. Kelime Tamamlama Oyunu
    3. Kafiye Tahmin Oyunu
    4. Kategoriye Göre Kelime Oyunu
    5. Ters Kelime Oyunu

    Not: Bu kod, StartingMagic platformu için özel olarak yazılmıştır.
*/


// ==================== KELIME VERİTABANI ====================
const kelimeler = {
    hayvanlar: ["aslan", "kaplan", "fil", "zürafa", "köpek", "kedi", "kuş", "balık", "kartal", "ayı"],
    meyveler: ["elma", "armut", "muz", "üzüm", "kiraz", "şeftali", "karpuz", "kavun", "portakal", "limon"],
    renkler: ["kırmızı", "mavi", "sarı", "yeşil", "mor", "pembe", "turuncu", "beyaz", "siyah", "gri"],
    ülkeler: ["türkiye", "almanya", "fransa", "italya", "ispanya", "ingiltere", "rusya", "çin", "japonya", "amerika"],
    meslekler: ["doktor", "öğretmen", "mühendis", "avukat", "hemşire", "polis", "itfaiyeci", "berber", "aşçı", "pilot"],
    eşyalar: ["masa", "sandalye", "kalem", "defter", "kitap", "telefon", "bilgisayar", "araba", "bisiklet", "saat"]
};

const kafiyeKelimeler = {
    "ev": ["dev", "lev", "kev"],
    "kar": ["yar", "dar", "nar"],
    "deniz": ["temiz", "henüz", "ceniz"],
    "güneş": ["büyüteç", "dürüst", "küreş"],
    "yıldız": ["hırsız", "sıkışık", "yıkış"]
};

// ==================== OYUN DEĞİŞKENLERİ ====================
let mevcutOyun = "";
let mevcutKelime = "";
let tahminEdilenHarfler = [];
let yanlisTahminler = 0;
let maksimumYanlis = 6;
let oyunBitti = false;

// ==================== YARDIMCI FONKSİYONLAR ====================
const rastgeleKelimeAl = (kategori) => {
    const kelimeListesi = kelimeler[kategori];
    return kelimeListesi[Math.floor(Math.random() * kelimeListesi.length)];
};

const kelimeGoster = () => {
    return mevcutKelime.split('').map(harf => 
        tahminEdilenHarfler.includes(harf) ? harf : '_'
    ).join(' ');
};

const oyunuSifirla = () => {
    mevcutKelime = "";
    tahminEdilenHarfler = [];
    yanlisTahminler = 0;
    oyunBitti = false;
};

const adamAsmacaCiz = (yanlisSayisi) => {
    const adamCizimleri = [
        "",
        "  +---+\n      |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n========="
    ];
    return adamCizimleri[yanlisSayisi];
};

// ==================== OYUN 1: KLASİK ADAM ASMACA ====================
const adamAsmacaOyna = () => {
    console.log("🎮 ADAM ASMACA OYUNU BAŞLADI! 🎮\n");
    
    const kategoriler = Object.keys(kelimeler);
    console.log("Kategoriler:");
    kategoriler.forEach((kat, index) => {
        console.log(`${index + 1}. ${kat.charAt(0).toUpperCase() + kat.slice(1)}`);
    });
    
    const kategoriSecimi = parseInt(prompt("Kategori seçin (1-" + kategoriler.length + "):")) - 1;
    const secilenKategori = kategoriler[kategoriSecimi];
    
    mevcutKelime = rastgeleKelimeAl(secilenKategori);
    oyunuSifirla();
    mevcutKelime = rastgeleKelimeAl(secilenKategori);
    
    console.log(`Kategori: ${secilenKategori.toUpperCase()}`);
    console.log(`Kelime: ${kelimeGoster()}`);
    
    while (!oyunBitti) {
        console.log(adamAsmacaCiz(yanlisTahminler));
        console.log(`\nKelime: ${kelimeGoster()}`);
        console.log(`Yanlış tahminler: ${yanlisTahminler}/${maksimumYanlis}`);
        console.log(`Tahmin edilen harfler: ${tahminEdilenHarfler.join(', ')}`);
        
        const tahmin = prompt("Bir harf tahmin edin:").toLowerCase();
        
        if (tahmin.length !== 1) {
            alert("Lütfen sadece bir harf girin!");
            continue;
        }
        
        if (tahminEdilenHarfler.includes(tahmin)) {
            alert("Bu harfi zaten tahmin ettiniz!");
            continue;
        }
        
        tahminEdilenHarfler.push(tahmin);
        
        if (mevcutKelime.includes(tahmin)) {
            console.log("✅ Doğru tahmin!");
            
            if (mevcutKelime.split('').every(harf => tahminEdilenHarfler.includes(harf))) {
                console.log("🎉 TEBRİKLER! Kelimeyi buldunuz: " + mevcutKelime.toUpperCase());
                oyunBitti = true;
            }
        } else {
            yanlisTahminler++;
            console.log("❌ Yanlış tahmin!");
            
            if (yanlisTahminler >= maksimumYanlis) {
                console.log(adamAsmacaCiz(yanlisTahminler));
                console.log("💀 OYUN BİTTİ! Kelime: " + mevcutKelime.toUpperCase());
                oyunBitti = true;
            }
        }
    }
};

// ==================== OYUN 2: KELİME TAMAMLAMA OYUNU ====================
const kelimeTamamlamaOyna = () => {
    console.log("🧩 KELİME TAMAMLAMA OYUNU BAŞLADI! 🧩\n");
    
    const tumKelimeler = Object.values(kelimeler).flat();
    mevcutKelime = tumKelimeler[Math.floor(Math.random() * tumKelimeler.length)];
    
    // Kelimenin yarısını gizle
    const gizlenecekHarfSayisi = Math.ceil(mevcutKelime.length / 2);
    let gizlenenPozisyonlar = [];
    
    while (gizlenenPozisyonlar.length < gizlenecekHarfSayisi) {
        const rastgelePozisyon = Math.floor(Math.random() * mevcutKelime.length);
        if (!gizlenenPozisyonlar.includes(rastgelePozisyon)) {
            gizlenenPozisyonlar.push(rastgelePozisyon);
        }
    }
    
    let gosterilen = mevcutKelime.split('').map((harf, index) => 
        gizlenenPozisyonlar.includes(index) ? '_' : harf
    ).join('');
    
    console.log(`Kelimeyi tamamlayın: ${gosterilen}`);
    console.log(`İpucu: ${mevcutKelime.length} harfli kelime`);
    
    let denemeSayisi = 3;
    
    while (denemeSayisi > 0) {
        const tahmin = prompt(`Kelimeyi tahmin edin (${denemeSayisi} deneme hakkınız kaldı):`).toLowerCase();
        
        if (tahmin === mevcutKelime) {
            console.log("🎉 TEBRİKLER! Doğru cevap: " + mevcutKelime.toUpperCase());
            return;
        } else {
            denemeSayisi--;
            if (denemeSayisi > 0) {
                console.log(`❌ Yanlış! ${denemeSayisi} deneme hakkınız kaldı.`);
            }
        }
    }
    
    console.log("💔 OYUN BİTTİ! Doğru cevap: " + mevcutKelime.toUpperCase());
};

// ==================== OYUN 3: KAFİYE TAHMİN OYUNU ====================
const kafiyeTahminOyna = () => {
    console.log("🎵 KAFİYE TAHMİN OYUNU BAŞLADI! 🎵\n");
    
    const anaKelimeler = Object.keys(kafiyeKelimeler);
    const secilenAnaKelime = anaKelimeler[Math.floor(Math.random() * anaKelimeler.length)];
    const kafiyeListesi = kafiyeKelimeler[secilenAnaKelime];
    
    console.log(`Ana kelime: ${secilenAnaKelime.toUpperCase()}`);
    console.log(`Bu kelimeyle kafiyeli ${kafiyeListesi.length} kelime bulmalısınız!`);
    
    let bulunanKelimeler = [];
    let denemeSayisi = kafiyeListesi.length + 2; // Biraz ekstra şans
    
    while (denemeSayisi > 0 && bulunanKelimeler.length < kafiyeListesi.length) {
        const tahmin = prompt(`Kafiyeli kelime girin (${denemeSayisi} deneme kaldı):`).toLowerCase();
        
        if (kafiyeListesi.includes(tahmin) && !bulunanKelimeler.includes(tahmin)) {
            bulunanKelimeler.push(tahmin);
            console.log(`✅ Doğru! Bulunan kelimeler: ${bulunanKelimeler.join(', ')}`);
            console.log(`Kalan: ${kafiyeListesi.length - bulunanKelimeler.length}`);
        } else if (bulunanKelimeler.includes(tahmin)) {
            console.log("Bu kelimeyi zaten buldunuz!");
            continue;
        } else {
            console.log("❌ Yanlış veya kafiyeli değil!");
        }
        
        denemeSayisi--;
    }
    
    if (bulunanKelimeler.length === kafiyeListesi.length) {
        console.log("🎉 TEBRİKLER! Tüm kafiyeli kelimeleri buldunuz!");
    } else {
        console.log(`💔 OYUN BİTTİ! Kaçırdıklarınız: ${kafiyeListesi.filter(k => !bulunanKelimeler.includes(k)).join(', ')}`);
    }
};

// ==================== OYUN 4: KATEGORİ KELİME OYUNU ====================
const kategoriKelimeOyna = () => {
    console.log("📚 KATEGORİ KELİME OYUNU BAŞLADI! 📚\n");
    
    const kategoriler = Object.keys(kelimeler);
    const secilenKategori = kategoriler[Math.floor(Math.random() * kategoriler.length)];
    const kategoriKelimeler = kelimeler[secilenKategori];
    
    console.log(`Kategori: ${secilenKategori.toUpperCase()}`);
    console.log(`Bu kategoriden 5 kelime tahmin edin!`);
    
    let bulunanKelimeler = [];
    let denemeSayisi = 8;
    
    while (denemeSayisi > 0 && bulunanKelimeler.length < 5) {
        const tahmin = prompt(`Kategori kelimesi girin (${denemeSayisi} deneme kaldı):`).toLowerCase();
        
        if (kategoriKelimeler.includes(tahmin) && !bulunanKelimeler.includes(tahmin)) {
            bulunanKelimeler.push(tahmin);
            console.log(`✅ Doğru! Bulunan: ${bulunanKelimeler.join(', ')}`);
            console.log(`Kalan: ${5 - bulunanKelimeler.length}`);
        } else if (bulunanKelimeler.includes(tahmin)) {
            console.log("Bu kelimeyi zaten buldunuz!");
            continue;
        } else {
            console.log("❌ Bu kategoride böyle bir kelime yok!");
        }
        
        denemeSayisi--;
    }
    
    if (bulunanKelimeler.length >= 5) {
        console.log("🎉 TEBRİKLER! 5 kelimeyi buldunuz!");
    } else {
        console.log(`💔 OYUN BİTTİ! Bulduğunuz: ${bulunanKelimeler.length}/5`);
        console.log(`Örnek kelimeler: ${kategoriKelimeler.slice(0, 5).join(', ')}`);
    }
};

// ==================== OYUN 5: TERS KELİME OYUNU ====================
const tersKelimeOyna = () => {
    console.log("🔄 TERS KELİME OYUNU BAŞLADI! 🔄\n");
    
    const tumKelimeler = Object.values(kelimeler).flat();
    const secilenKelimeler = [];
    
    // 5 rastgele kelime seç
    while (secilenKelimeler.length < 5) {
        const rastgeleKelime = tumKelimeler[Math.floor(Math.random() * tumKelimeler.length)];
        if (!secilenKelimeler.includes(rastgeleKelime)) {
            secilenKelimeler.push(rastgeleKelime);
        }
    }
    
    console.log("Aşağıdaki ters çevrilmiş kelimeleri doğru şekilde yazın:\n");
    
    let dogruSayisi = 0;
    
    secilenKelimeler.forEach((kelime, index) => {
        const tersKelime = kelime.split('').reverse().join('');
        console.log(`${index + 1}. ${tersKelime.toUpperCase()}`);
        
        const tahmin = prompt(`Bu kelimenin doğru hali nedir?`).toLowerCase();
        
        if (tahmin === kelime) {
            console.log("✅ Doğru!");
            dogruSayisi++;
        } else {
            console.log(`❌ Yanlış! Doğru cevap: ${kelime.toUpperCase()}`);
        }
        console.log("");
    });
    
    console.log(`🎯 SONUÇ: ${dogruSayisi}/5 doğru cevap!`);
    
    if (dogruSayisi === 5) {
        console.log("🏆 MÜKEMMEL! Tüm kelimeleri doğru bildiniz!");
    } else if (dogruSayisi >= 3) {
        console.log("👏 İyi iş çıkardınız!");
    } else {
        console.log("💪 Daha fazla pratik yapmalısınız!");
    }
};

// ==================== ANA MENÜ ====================
const anaMenu = () => {
    console.log("🎮 KELİME TAHMİN OYUNLARI KOLEKSİYONU 🎮\n");
    console.log("1. Adam Asmaca (Klasik)");
    console.log("2. Kelime Tamamlama");
    console.log("3. Kafiye Tahmin");
    console.log("4. Kategori Kelime");
    console.log("5. Ters Kelime");
    console.log("0. Çıkış\n");
    
    const secim = parseInt(prompt("Oynamak istediğiniz oyunu seçin (0-5):"));
    
    switch (secim) {
        case 1:
            adamAsmacaOyna();
            break;
        case 2:
            kelimeTamamlamaOyna();
            break;
        case 3:
            kafiyeTahminOyna();
            break;
        case 4:
            kategoriKelimeOyna();
            break;
        case 5:
            tersKelimeOyna();
            break;
        case 0:
            console.log("👋 Oynadığınız için teşekkürler!");
            return;
        default:
            console.log("❌ Geçersiz seçim!");
            break;
    }
    
    // Tekrar oynama seçeneği
    const tekrarOyna = confirm("Başka bir oyun oynamak ister misiniz?");
    if (tekrarOyna) {
        anaMenu();
    } else {
        console.log("👋 Oynadığınız için teşekkürler!");
    }
};

// ==================== OYUNU BAŞLAT ====================

anaMenu();