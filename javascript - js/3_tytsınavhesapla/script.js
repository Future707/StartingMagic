/* 
    Script: p3_tytsınavhesapla/script.js
    Açıklama: TYT sınav puanını ve detaylı istatistik hesaplar.
    Yazar: [Future Developer] 
    Tarih: 25.08.2025
    Versiyon: 1.00
    

    Not: Bu kod, StartingMagic platformu için özel olarak yazılmıştır.

*/



/* 
    TYT Sınav Puanı Hesaplama İçeriği

    - Doğru ve yanlış sayısına göre net hesaplama
    - Netlere göre puan hesaplama
    - Sonuçların kullanıcıya gösterilmesi
    - İstatistiksel veriler
*/






// -------------------------------
// TYT PUAN HESAPLAMA FORMÜLLERİ
// -------------------------------

// 1) NET HESABI
// Net = Doğru - (Yanlış / 4)

// 2) KATSAYILAR
// Türkçe katsayı: 3.3
// Sosyal Bilimler katsayı: 3.4
// Temel Matematik katsayı: 3.3
// Fen Bilimleri katsayı: 3.4
// Sabit puan: 100

// 3) HAM TYT PUANI
// Ham TYT = (Türkçe Net * 3.3) 
//         + (Sosyal Net * 3.4) 
//         + (Matematik Net * 3.3) 
//         + (Fen Net * 3.4) 
//         + 100

// 4) OBP (ORTAÖĞRETİM BAŞARI PUANI)
// OBP = Diploma Notu * 5          // (Diploma notu: 0 - 100 arası)
// OBP Katkısı = OBP * 0.12

// 5) YERLEŞTİRME PUANI
// TYT Yerleştirme Puanı = Ham TYT + OBP Katkısı

const netHesapla=(d,y)=>(d-(y/4));
const bosHesapla=(toplam,d,y)=>(toplam-(d+y));
const puanHesapla=(net,carpim)=>(Math.round((net*carpim)*10)/10);

let diplomaNotu = parseFloat(prompt("Diploma Notu : "));

let turkceD = parseInt(prompt("Türkçe Doğru Soru Sayısı : "));
let turkceY = parseInt(prompt("Türkçe Yanlış Soru Sayısı : "));
let turkceB = bosHesapla(40,turkceD,turkceY);
let turkceNet = netHesapla(turkceD,turkceY);
let turkcePuan = puanHesapla(turkceNet,3.3);

let matematikD = parseInt(prompt("Matematik Doğru Soru Sayısı : "));
let matematikY = parseInt(prompt("Matematik Yanlış Soru Sayısı : "));
let matematikB = bosHesapla(40,matematikD,matematikY);
let matematikNet = netHesapla(matematikD,matematikY);
let matematikPuan = puanHesapla(matematikNet,3.3);

let sosyalD = parseInt(prompt("Sosyal Doğru Soru Sayısı : "));
let sosyalY = parseInt(prompt("Sosyal Yanlış Soru Sayısı : "));
let sosyalB = bosHesapla(20,sosyalD,sosyalY);
let sosyalNet = netHesapla(sosyalD,sosyalY);
let sosyalPuan = puanHesapla(sosyalNet,3.4);

let fenD = parseInt(prompt("Fen Doğru Soru Sayısı : "));
let fenY = parseInt(prompt("Fen Yanlış Soru Sayısı : "));
let fenB = bosHesapla(20,fenD,fenY);
let fenNet = netHesapla(fenD,fenY);
let fenPuan = puanHesapla(fenNet,3.4);

let toplamD =turkceD+matematikD+sosyalD+fenD;
let toplamY =turkceY+matematikY+sosyalY+fenY; 
let toplamB =bosHesapla(120,toplamD,toplamY);
let toplamNet = turkceNet+matematikNet+sosyalNet+fenNet==netHesapla(toplamD,toplamY)?netHesapla(toplamD,toplamY):"ERROR";
let hamTYT = turkcePuan+matematikPuan+fenPuan+sosyalPuan+100; 
let OBPkatkı = diplomaNotu*5*0.12;
let yerlestirmePuaniTYT = hamTYT+OBPkatkı;

alert("Hesaplamalar Tamamlandı!\nSonuçlar için 'Tamam'a basınız...");

let netmetin=`Türkçe : ${turkceNet}\nMatematik : ${matematikNet}\nSosyal : ${sosyalNet}\nFen : ${fenNet}\nToplam: ${toplamNet}`;
let puanmetin=`Türkçe : ${turkcePuan}\nMatematik : ${matematikPuan}\nSosyal : ${sosyalPuan}\nFen : ${fenPuan}\nHam TYT: ${hamTYT}\nOBP katkı : ${OBPkatkı}\nTYT Yerleştirme Puanı : ${yerlestirmePuaniTYT}`;
let genelmetin = `
📌 Bilgilendirme Penceresi<br>
================================<br><br>

📖 Türkçe<br>
✅ Doğru   : ${turkceD}<br>
❌ Yanlış  : ${turkceY}<br>
➖ Boş     : ${turkceB}<br>
📊 Net     : ${turkceNet}<br>
🏆 Puan    : ${turkcePuan}<br><br>

--------------------------------<br><br>

🧮 Matematik<br>
✅ Doğru   : ${matematikD}<br>
❌ Yanlış  : ${matematikY}<br>
➖ Boş     : ${matematikB}<br>
📊 Net     : ${matematikNet}<br>
🏆 Puan    : ${matematikPuan}<br><br>

--------------------------------<br><br>

🌍 Sosyal<br>
✅ Doğru   : ${sosyalD}<br>
❌ Yanlış  : ${sosyalY}<br>
➖ Boş     : ${sosyalB}<br>
📊 Net     : ${sosyalNet}<br>
🏆 Puan    : ${sosyalPuan}<br><br>

--------------------------------<br><br>

🔬 Fen<br>
✅ Doğru   : ${fenD}<br>
❌ Yanlış  : ${fenY}<br>
➖ Boş     : ${fenB}<br>
📊 Net     : ${fenNet}<br>
🏆 Puan    : ${fenPuan}<br><br>

--------------------------------<br><br>

📌 TOPLAM<br>
✅ Doğru   : ${toplamD}<br>
❌ Yanlış  : ${toplamY}<br>
➖ Boş     : ${toplamB}<br>
📊 Net     : ${toplamNet}<br><br>

--------------------------------<br><br>

🎓 Diploma Notu : ${diplomaNotu}<br>
📘 OBP Katkı    : ${OBPkatkı}<br>
📝 Ham TYT      : ${hamTYT}<br>
💯 TYT Yerleştirme Puanı → ${yerlestirmePuaniTYT}<br><br>

================================<br>
`;


let secim;


do{
    secim = parseInt(prompt("1- Netlerim\n2- Puanlarım\n3- Tüm Bilgilendirme\n4- Çıkış"));

    switch(secim){
        case 1:
            alert(netmetin);
            break;
        case 2:
            alert(puanmetin);
    
        case 3:
            document.querySelector(".out").innerHTML = genelmetin;
            console.log(genelmetin);
            break;
                
        case 4:
                alert("Sistemden Çıkış Yapılıyor\nİyi Günler Dileriz...");break;
        default:
            alert("Geçerli bir seçim yaptığınızdan emin olunuz...");break;
            
     }   


}while(secim!=4)






