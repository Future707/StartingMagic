/* 
    Script: p6_sayiDonusumleriBD/script.js
    Açıklama: İkilik (binary) ve onluk (decimal) sayı sistemleri arasında dönüşüm yapan fonksiyonlar.
    Yazar: [Future Developer]
    Tarih: [26.08.2025]
    Sürüm: 1.00

    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
*/

/*
    İçerik:
    - Girilen Binary Tabanlı sayıyı Decimal Tabanlı sayıya dönüştürme.
    - Verilen Aralıkta Sayıları Binary-Decimal formda gösterme.
*/


const binarydendecimal = (sayi) => {

    let sayitext = sayi.toString().split("").reverse().join("");
    let decimalsayi = 0;

    for (let i = 0; i < sayitext.length; i++) {

        decimalsayi += Math.pow(2, i) * parseInt(sayitext[i]);

    }

    return decimalsayi;
}

const decimaldenbinary = (sayi) => {

    let binarysayi = "";
    while (sayi != 1 && sayi != 0) {
        binarysayi += (sayi % 2).toString();
        sayi = Math.floor(sayi / 2);
    }
    binarysayi += (sayi % 2).toString();

    return binarysayi.split("").reverse().join("");


}



alert("Sayı Dönüşüm Uygulamasına Hoşgeldiniz...\nSeçenekleri Görmek İçin `tamam`a Basınız...");
let secim = parseInt(prompt("[0] - Binaryden Decimal'e\n[1] - Decimalden Binary'e\n[2] - Aralık Çözümleme\n[3] - Çıkış"));
switch (secim) {

    case 0:
        let binarysayi = prompt("Binary Sayıyı Giriniz : ");
        let decimalcikti = binarydendecimal(binarysayi);
        alert("Binary " + binarysayi + " || Decimal " + decimalcikti);
        break;
    case 1:
        let decimalsayi = parseInt(prompt("Decimal Sayıyı Giriniz : "));
        let binarycikti = decimaldenbinary(decimalsayi);
        alert("Binary " + binarycikti + " || Decimal " + decimalsayi);
        break;
    case 2:
        let tip = prompt("Aralıklar Hangi Cinsten Girilecek?\n[1] - 2 tabanlı // BINARY\n[2] - 10 tabanlı // DECIMAL")
        let altaralik = prompt("Alt aralık : ");
        let ustaralik = prompt("Üst aralık : ");
        if (tip == 1) { altaralik = binarydendecimal(altaralik); ustaralik = binarydendecimal(ustaralik); }
        else { altaralik = parseInt(altaralik); ustaralik = parseInt(ustaralik); }
        let temp;
        if (altaralik > ustaralik) { temp = altaralik; altaralik = ustaralik; ustaralik = temp; }
        let out = "";
        for (let i = altaralik; i < ustaralik; i++) {
            sayidecimal = i;
            sayibinary = decimaldenbinary(i);
            out += "(" + sayibinary + ")2 || (" + sayidecimal + ")10\n";
        }
        console.log(out);
        alert(out);
        break;
    case 3:
        alert("Çıkış Yapılıyor...");
        break;
    default:
        alert("Geçersiz Giriş!");
        break;

}



