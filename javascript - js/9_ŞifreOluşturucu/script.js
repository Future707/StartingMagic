/* 
    Script: Gelişmiş Şifre Üretici ve Yöneticisi
    Açıklama: Güvenli şifreler üret ve şifre güvenliğini yönet
    Yazar: [Future Developer] 
    Tarih: 01.09.2025
    Sürüm: 1.0

    Özellikler:
    - Birden fazla şifre üretim türü
    - Şifre güç kontrolü
    - Hatırlanabilir şifre üretici
    - Şifre geçmişi ve favoriler
    - Güvenlik ipuçları ve analiz

    Not: Bu kod, StartingMagic platformu için özel olarak yazılmıştır.
*/


// Password storage and history
let passwordHistory = [];
let favoritePasswords = [];
let securityTips = [
    "Aynı şifreyi birden fazla hesapta kullanmayın",
    "Şifrelerinizi düzenli olarak değiştirin",
    "İki faktörlü kimlik doğrulamayı etkinleştirin",
    "Kişisel bilgileri şifrede kullanmaktan kaçının",
    "Güvenilir şifre yöneticisi kullanın",
    "Halka açık Wi-Fi'de hassas işlemler yapmayın",
    "Phishing e-postalarına dikkat edin",
    "Şifrelerinizi kimseyle paylaşmayın"
];

// Character sets for password generation
const charSets = {
    lowercase: "abcdefghijklmnopqrstuvwxyz",
    uppercase: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    numbers: "0123456789",
    symbols: "!@#$%^&*()_+-=[]{}|;:,.<>?",
    similar: "il1Lo0O",
    memorable: {
        adjectives: ["Güçlü", "Hızlı", "Parlak", "Gizli", "Büyük", "Küçük", "Sıcak", "Soğuk", "Yeni", "Eski"],
        nouns: ["Aslan", "Kaplan", "Kartal", "Ejder", "Şimşek", "Fırtına", "Dağ", "Deniz", "Güneş", "Ay"],
        colors: ["Kırmızı", "Mavi", "Yeşil", "Sarı", "Mor", "Turuncu", "Siyah", "Beyaz", "Pembe", "Gri"]
    }
};

// Generate random password
const generateRandomPassword = () => {
    let length = parseInt(prompt("Şifre uzunluğu girin (8-128 karakter):"));
    if (length < 8 || length > 128 || isNaN(length)) {
        alert("⚠️ Geçersiz uzunluk! 8-128 arası değer girin.");
        return;
    }

    let options = prompt(`Şifre seçenekleri (virgülle ayırın):\n1 - Küçük harfler (a-z)\n2 - Büyük harfler (A-Z)\n3 - Sayılar (0-9)\n4 - Semboller (!@#$...)\n5 - Benzer karakterleri hariç tut\n\nÖrnek: 1,2,3,4`);
    
    if (!options) {
        alert("❌ Hiçbir seçenek belirtilmedi!");
        return;
    }

    let selectedOptions = options.split(',').map(opt => parseInt(opt.trim()));
    let charset = "";

    if (selectedOptions.includes(1)) charset += charSets.lowercase;
    if (selectedOptions.includes(2)) charset += charSets.uppercase;
    if (selectedOptions.includes(3)) charset += charSets.numbers;
    if (selectedOptions.includes(4)) charset += charSets.symbols;

    if (selectedOptions.includes(5)) {
        // Remove similar looking characters
        for (let char of charSets.similar) {
            charset = charset.replace(new RegExp(char, 'g'), '');
        }
    }

    if (charset === "") {
        alert("❌ En az bir karakter türü seçmelisiniz!");
        return;
    }

    let password = "";
    for (let i = 0; i < length; i++) {
        password += charset.charAt(Math.floor(Math.random() * charset.length));
    }

    let strength = checkPasswordStrength(password);
    
    // Add to history
    passwordHistory.unshift({
        password: password,
        type: "Rastgele",
        length: length,
        strength: strength,
        date: new Date().toLocaleString("tr-TR")
    });

    if (passwordHistory.length > 20) {
        passwordHistory.pop();
    }

    let result = `🔐 YENİ ŞİFRE OLUŞTURULDU!\n\nŞifre: ${password}\nUzunluk: ${length} karakter\nGüçlülük: ${strength.level}\nSkor: ${strength.score}/100\n\n${strength.feedback}`;
    
    alert(result);
    console.log("Generated password:", { password, strength });
};

// Generate memorable password
const generateMemorablePassword = () => {
    alert("🧠 Akılda Kalıcı Şifre Üreticisi\nKolay hatırlanabilir ama güvenli şifreler oluşturur");

    let type = parseInt(prompt("Memorable şifre türü:\n1 - Sıfat + İsim + Sayı (örn: GüçlüAslan47)\n2 - Renk + Hayvan + Yıl (örn: MaviKartal2023)\n3 - Üç Kelime + Sayılar (örn: Hızlı-Şimşek-95)\n4 - Kısa Cümle (örn: Benim3Kedim!Var)"));

    let password = "";
    let description = "";

    switch(type) {
        case 1:
            let adj1 = charSets.memorable.adjectives[Math.floor(Math.random() * charSets.memorable.adjectives.length)];
            let noun1 = charSets.memorable.nouns[Math.floor(Math.random() * charSets.memorable.nouns.length)];
            let num1 = Math.floor(Math.random() * 100);
            password = adj1 + noun1 + num1;
            description = "Sıfat + İsim + Sayı";
            break;
            
        case 2:
            let color = charSets.memorable.colors[Math.floor(Math.random() * charSets.memorable.colors.length)];
            let animal = charSets.memorable.nouns[Math.floor(Math.random() * charSets.memorable.nouns.length)];
            let year = Math.floor(Math.random() * 50) + 1980;
            password = color + animal + year;
            description = "Renk + Hayvan + Yıl";
            break;
            
        case 3:
            let word1 = charSets.memorable.adjectives[Math.floor(Math.random() * charSets.memorable.adjectives.length)];
            let word2 = charSets.memorable.nouns[Math.floor(Math.random() * charSets.memorable.nouns.length)];
            let num2 = Math.floor(Math.random() * 100);
            password = word1 + "-" + word2 + "-" + num2;
            description = "Üç Parçalı";
            break;
            
        case 4:
            let subject = Math.floor(Math.random() * 5) + 1;
            let object = charSets.memorable.nouns[Math.floor(Math.random() * charSets.memorable.nouns.length)];
            let verb = ["Var", "Yok", "Güzel", "Hızlı"][Math.floor(Math.random() * 4)];
            password = `Benim${subject}${object}${verb}!`;
            description = "Cümle Yapısı";
            break;
            
        default:
            alert("❌ Geçersiz seçim!");
            return;
    }

    let strength = checkPasswordStrength(password);
    
    // Add to history
    passwordHistory.unshift({
        password: password,
        type: "Memorable (" + description + ")",
        length: password.length,
        strength: strength,
        date: new Date().toLocaleString("tr-TR")
    });

    let result = `🧠 MEMORABLE ŞİFRE OLUŞTURULDU!\n\nŞifre: ${password}\nTür: ${description}\nUzunluk: ${password.length} karakter\nGüçlülük: ${strength.level}\n\n💡 Bu şifre kolay hatırlanabilir ama yine de güvenlidir!`;
    
    alert(result);
    console.log("Memorable password:", { password, type: description, strength });
};

// Check password strength
const checkPasswordStrength = (password) => {
    let score = 0;
    let feedback = [];

    // Length check
    if (password.length >= 12) {
        score += 25;
    } else if (password.length >= 8) {
        score += 15;
        feedback.push("• Daha uzun şifre kullanmayı deneyin");
    } else {
        score += 5;
        feedback.push("• Şifre çok kısa, en az 8 karakter olmalı");
    }

    // Character variety checks
    if (/[a-z]/.test(password)) score += 15;
    else feedback.push("• Küçük harf ekleyin");

    if (/[A-Z]/.test(password)) score += 15;
    else feedback.push("• Büyük harf ekleyin");

    if (/[0-9]/.test(password)) score += 15;
    else feedback.push("• Sayı ekleyin");

    if (/[^a-zA-Z0-9]/.test(password)) score += 20;
    else feedback.push("• Özel karakter ekleyin");

    // Pattern checks
    if (!/(.)\1{2,}/.test(password)) score += 10;
    else feedback.push("• Ard arda aynı karakterleri azaltın");

    // Common patterns
    let commonPatterns = ["123", "abc", "password", "qwerty"];
    let hasCommonPattern = commonPatterns.some(pattern => 
        password.toLowerCase().includes(pattern)
    );
    
    if (!hasCommonPattern) score += 5;
    else feedback.push("• Yaygın kalıplardan kaçının");

    // Determine level
    let level = "";
    if (score >= 90) level = "🟢 Çok Güçlü";
    else if (score >= 70) level = "🟡 Güçlü";
    else if (score >= 50) level = "🟠 Orta";
    else if (score >= 30) level = "🔴 Zayıf";
    else level = "💀 Çok Zayıf";

    return {
        score: score,
        level: level,
        feedback: feedback.length > 0 ? "İyileştirme önerileri:\n" + feedback.join("\n") : "✅ Mükemmel şifre!"
    };
};

// Analyze existing password
const analyzePassword = () => {
    let password = prompt("Analiz edilecek şifreyi girin:");
    if (!password) {
        alert("❌ Şifre girilmedi!");
        return;
    }

    let strength = checkPasswordStrength(password);
    let crackTime = estimateCrackTime(password);
    
    let analysis = `🔍 ŞİFRE ANALİZİ\n\n`;
    analysis += `Şifre: ${"*".repeat(password.length)}\n`;
    analysis += `Uzunluk: ${password.length} karakter\n`;
    analysis += `Güçlülük: ${strength.level}\n`;
    analysis += `Skor: ${strength.score}/100\n`;
    analysis += `Kırılma süresi: ${crackTime}\n\n`;
    analysis += `${strength.feedback}`;

    alert(analysis);
    console.log("Password analysis:", { length: password.length, strength, crackTime });
};

// Estimate crack time
const estimateCrackTime = (password) => {
    let charset = 0;
    if (/[a-z]/.test(password)) charset += 26;
    if (/[A-Z]/.test(password)) charset += 26;
    if (/[0-9]/.test(password)) charset += 10;
    if (/[^a-zA-Z0-9]/.test(password)) charset += 32;

    let combinations = Math.pow(charset, password.length);
    let guessesPerSecond = 1000000000; // 1 billion guesses per second
    let secondsToCrack = combinations / (2 * guessesPerSecond);

    if (secondsToCrack < 60) return "Saniyeler içinde";
    if (secondsToCrack < 3600) return `${Math.round(secondsToCrack / 60)} dakika`;
    if (secondsToCrack < 86400) return `${Math.round(secondsToCrack / 3600)} saat`;
    if (secondsToCrack < 31536000) return `${Math.round(secondsToCrack / 86400)} gün`;
    if (secondsToCrack < 3153600000) return `${Math.round(secondsToCrack / 31536000)} yıl`;
    return "Milyonlarca yıl";
};

// Show password history
const showHistory = () => {
    if (passwordHistory.length === 0) {
        alert("📝 Henüz şifre oluşturulmadı!");
        return;
    }

    let history = "📝 ŞİFRE GEÇMİŞİ\n\n";
    passwordHistory.forEach((entry, index) => {
        history += `${index + 1}. ${entry.type}\n`;
        history += `   Şifre: ${entry.password}\n`;
        history += `   Güçlülük: ${entry.strength.level}\n`;
        history += `   Tarih: ${entry.date}\n`;
        history += `${"=".repeat(30)}\n\n`;
    });

    alert(history);
};

// Generate passphrase
const generatePassphrase = () => {
    let words = ["elma", "kitap", "güneş", "deniz", "dağ", "çiçek", "kuş", "rüzgar", "yıldız", "nehir",
                 "orman", "köprü", "bahçe", "pencere", "kapı", "masa", "kalem", "resim", "müzik", "dans"];
    
    let wordCount = parseInt(prompt("Kaç kelime kullanılsın? (3-8 arası):"));
    if (wordCount < 3 || wordCount > 8 || isNaN(wordCount)) {
        alert("⚠️ 3-8 arası sayı girin!");
        return;
    }

    let separator = prompt("Kelimeler arası ayırıcı (-, _, boşluk):") || "-";
    let addNumbers = confirm("Sonuna sayı eklensin mi?");
    let capitalizeFirst = confirm("İlk harfler büyük olsun mu?");

    let passphrase = [];
    for (let i = 0; i < wordCount; i++) {
        let word = words[Math.floor(Math.random() * words.length)];
        if (capitalizeFirst) {
            word = word.charAt(0).toUpperCase() + word.slice(1);
        }
        passphrase.push(word);
    }

    let result = passphrase.join(separator);
    if (addNumbers) {
        result += Math.floor(Math.random() * 1000);
    }

    let strength = checkPasswordStrength(result);
    
    passwordHistory.unshift({
        password: result,
        type: "Passphrase",
        length: result.length,
        strength: strength,
        date: new Date().toLocaleString("tr-TR")
    });

    alert(`🔤 PASSPHRASE OLUŞTURULDU!\n\nPassphrase: ${result}\nUzunluk: ${result.length} karakter\nGüçlülük: ${strength.level}\n\n💡 Passphraselar uzun ama hatırlaması kolaydır!`);
};

// Show security tips
const showSecurityTips = () => {
    let randomTip = securityTips[Math.floor(Math.random() * securityTips.length)];
    
    let tips = `🛡️ GÜVENLİK İPUÇLARI\n\n`;
    tips += `💡 Günün İpucu:\n"${randomTip}"\n\n`;
    tips += `📚 Diğer önemli ipuçları:\n\n`;
    
    securityTips.forEach((tip, index) => {
        if (tip !== randomTip) {
            tips += `• ${tip}\n`;
        }
    });

    alert(tips);
};

// Main menu
const main = () => {
    alert("🔐 Gelişmiş Şifre Üretici ve Yöneticisine Hoş Geldiniz!");
    
    let choice = parseInt(prompt(`Ana Menü - Ne yapmak istiyorsunuz?\n\n1 - Rastgele Şifre Oluştur\n2 - Akılda Kalıcı Şifre Oluştur\n3 - Passphrase Oluştur\n4 - Mevcut Şifreyi Analiz Et\n5 - Şifre Geçmişini Görüntüle\n6 - Güvenlik İpuçları\n7 - Çıkış\n\nSeçiminiz:`));

    switch(choice) {
        case 1:
            generateRandomPassword();
            break;
        case 2:
            generateMemorablePassword();
            break;
        case 3:
            generatePassphrase();
            break;
        case 4:
            analyzePassword();
            break;
        case 5:
            showHistory();
            break;
        case 6:
            showSecurityTips();
            break;
        case 7:
            alert("🔐 Güvenli şifreler kullanmayı unutmayın! Hoşçakalın!");
            return;
        default:
            alert("❌ Geçersiz seçim!");
            break;
    }
};

// Start the application
main();