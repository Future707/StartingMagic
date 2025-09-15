/* 
    Script: p1_yakitalmauygulama/script.js
    Açıklama: Yakıt alma için gerekli JavaScript kodları.
    Yazar: [Future Developer]
    Tarih: [25.08.2025]
    Sürüm: 1.00

    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
*/


let yakit = window.prompt("[1]Benzin (95 Oktan): 42,50 TL / Litre\n[2]Benzin (98 Oktan): 44,20 TL / Litre\n[3]Motorin (Dizel): 40,10 TL / Litre\n[4]LPG: 21,80 TL / Litre\nYakıt Türü Seçiniz");
let litre = window.prompt("Kaç Litre Almak İstiyorsunuz?");

let litrefiyat = yakit==1?42.5:yakit==2?44.2:yakit==3?40.1:yakit==4?21.8:alert("Geçersiz Yakıt Türü Seçtiniz!");

alert(`Toplam Tutar: ${litrefiyat*litre} TL`);

alert("Teşekkür Ederiz, İyi Günler Dileriz!");

document.querySelector(".out").innerHTML = `Toplam Tutar: ${litrefiyat*litre} TL<br>Teşekkür Ederiz, İyi Günler Dileriz!`;