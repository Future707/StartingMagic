/* 
    Script: p2_atmuygulaması/script.js
    Açıklama: Atm uygulaması için gerekli JavaScript kodları.
    Yazar: [Future Developer]
    Tarih: [25.08.2025]
    Sürüm: 1.00

    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.


*/


/*  
    ATM uygulaması içerik
    1- Bakiye Sorgulama
    2- Para Çekme
    3- Para Yatırma
    4- Tarihçeyi Görüntüleme
    5- Çıkış

*/


let bakiye = 10000;
let tarihce = [];
let islem;
do {
    islem = window.prompt("[1]Bakiye Sorgulama\n[2]Para Çekme\n[3]Para Yatırma\n[4]Tarihçeyi Görüntüleme\n[5]Çıkış\nLütfen yapmak istediğiniz işlemi seçiniz:");
    switch (islem) {
        case "1":
            alert(`Güncel Bakiyeniz: ${bakiye} TL`);
            tarihce.push(`Bakiye Sorgulama: ${bakiye} TL`);
            break;
        case "2":
            let cekilecekTutar = parseFloat(window.prompt("Çekmek istediğiniz tutarı giriniz:"));
            if (cekilecekTutar > bakiye) {
                alert("Yetersiz bakiye!");
            } else {
                bakiye -= cekilecekTutar;
                alert(`İşlem başarılı! Yeni bakiyeniz: ${bakiye} TL`);
                tarihce.push(`Para Çekme: -${cekilecekTutar} TL, Yeni Bakiye: ${bakiye} TL`);
            }
            break;
        case "3":
            let yatirilacakTutar = parseFloat(window.prompt("Yatırmak istediğiniz tutarı giriniz:"));
            bakiye += yatirilacakTutar;
            alert(`İşlem başarılı! Yeni bakiyeniz: ${bakiye} TL`);
            tarihce.push(`Para Yatırma: +${yatirilacakTutar} TL, Yeni Bakiye: ${bakiye} TL`);
            break;
        case "4":
            if (tarihce.length === 0) {
                alert("Henüz işlem yapılmadı.");
            } else {
                alert("İşlem Tarihçesi:\n" + tarihce.join("\n"));
            }
            break;
        case "5":
            alert("Çıkış yapılıyor. İyi günler dileriz!");
            break;
        default:
            alert("Geçersiz işlem seçimi. Lütfen tekrar deneyiniz.");
    }
}while (islem !== "5"&&(islem=="1"||islem!="2"||islem!="3"||islem!="4"));


document.querySelector(".out").innerHTML = "ATM uygulamasını kullandığınız için teşekkür ederiz. İyi günler dileriz!";