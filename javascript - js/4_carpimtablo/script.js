/* 
    Script: p4_carpimtablo/script.js
    Açıklama: Çarpı tablosu için gerekli JavaScript kodları.
    Yazar: [Future Developer]
    Tarih: [25.08.2025]
    Sürüm: 1.00

    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
*/


/*
    Çarpım Tablosu İçeriği
    -Çarpım tablosu oluşturma istenen şekilde(1-10//onluklar beşlikler....)
    -Çarpım Quizi(5 soruluk,10 soruluk)

*/ 


alert("Merhaba çarpım tablosuna hoşgeldin...\nLütfen `tamam`a bas ve ardından istediğin işlemi seç..")


let secim;
let kullaniciPuan=0;


const carpimtablosuolustur=(limitof,miktar)=>{ //limit of 
    for (let index = 1; index <= limitof; index++) {
        console.log("part #"+index+"s")
        for (let index2 = 1; index2 <= miktar; index2++) {
            console.log(index+"x"+index2+"="+(index*index2)+"\n");
            
        }
        console.log("--------------\n")

        
    }
}

do
{
    secim = parseInt(prompt("1-Çarpım Tablosu Oluşturucu\n2-Çarpım Tablosu quiz\n3-Mevcut Puanım\n4-Çıkış"));
    switch(secim){
        case 1:
            let sinir = parseInt(prompt("Hangi sayıya kadar olsun : "));
            let kacar = parseInt(prompt("Kaçar kaçar yazdıralım :  "));
            carpimtablosuolustur(sinir,kacar);
            break;
        case 2:
            let soruadedi=parseInt(prompt("Kaç adet soru istersin?"));
            let zorluk= parseInt(prompt("Zorluk seçin \n1-Beşe kadar\n2-Ona kadar\n3-On beşe kadar\n4-Yirmiye kadar\n5-Yirmi beşe kadar"));
            let puan=zorluk*50;
            for(let i=0;i<soruadedi;i++){                
                let sayı1=Math.floor(Math.random()*((zorluk*5)+1));
                let sayı2=Math.floor(Math.random()*((zorluk*5)+1));
                let tahmin=parseInt(prompt(sayı1+"x"+sayı2+"= `?`"));
                kullaniciPuan= tahmin==sayı1*sayı2?kullaniciPuan+(puan):kullaniciPuan-(puan);
                alert(tahmin==sayı1*sayı2?"BAŞARILI (+"+puan+")":"BAŞARISIZ(-"+puan+")")
            }
            break;
        case 3:
            alert(`Mevcut Puanınız : ${kullaniciPuan}Pts..`);
            break;
        case 4:
            alert("Çıkış yapılıyor görüşmek üzere")
            break;
        default:
            alert("Geçerli bir seçim yapınız...")
            break;
    }


}while(secim!=4)