/* 
    Script: p5_sayidunyasi/script.js
    Açıklama: Bazı meşhur sayıların tespiti için gerekli JavaScript kodları.
    Yazar: [Future Developer]
    Tarih: [25.08.2025]
    Sürüm: 1.00

    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
*/

/*

    İçerik:
    - Sayılara Örnekler
    - Bir sayının özel bir sayı olup olmadığını bulmak
    - Aralıkta sayı tespiti
    
*/

const asalmi=(sayi)=>{
    if(sayi < 2) return false;
    let asal=true;
    for(let i=2;(i<=sayi/2)&&asal;i++){
        asal=sayi%i!=0;
    }
    return asal;
};

const palindrommu=(sayi)=>{
    let metinsayi=sayi.toString();
    let tersmetinsayi=metinsayi.split("").reverse().join("");
    return metinsayi==tersmetinsayi?true:false;
};

const armstrongmu=(sayi)=>{
    let toplam=0;
    let basamak=sayi.toString().length;
    let ilksayi=sayi;
    let temp;
    while(sayi>0){
        temp=sayi%10;
        toplam+=Math.pow(temp,basamak);
        sayi=Math.floor(sayi/10);
    }
    return ilksayi==toplam; // DÜZELTME: sayi yerine toplam
};

const mukemmelmi=(sayi)=>{
    if(sayi <= 1) return false;
    let toplam=0;
    for(let i=1;i<=sayi/2;i++){
        toplam+=sayi%i==0?i:0;
    }
    return toplam==sayi;
};

const karesayi=(sayi)=>{
    return Math.floor(Math.sqrt(sayi))-Math.sqrt(sayi)==0&&sayi>=0;
};

const kupsayi=(sayi)=>{
    return Math.floor(Math.cbrt(sayi))-Math.cbrt(sayi)==0&&sayi>=0;
};

const tersbolunurmu=(sayi)=>{
    let tersi=parseInt(sayi.toString().split("").reverse().join(""));
    if(tersi === 0) return false;
    return sayi%tersi==0;
};

const fibonaccimi=(sayi)=>{
    if(sayi < 0) return false;
    let exp=7*sayi.toString().length;
    let explist=Array.from(fibonacciOlustur(exp));
    let fibonacci=false;
    for(let i=0;(i<explist.length)&&!fibonacci;i++){
        fibonacci=explist[i]==sayi?true:false;
    }
    return fibonacci; // DÜZELTME: return eksikliği giderildi
};

const fibonacciOlustur=(sayi)=>{
    let mylist=[];
    let temp;
    let ilk=0,son=1;
    mylist=[ilk,son];
    for(let i=0;i<sayi-2;i++){
        temp=son;
        son=ilk+son;
        ilk=temp;
        mylist.push(son);
    }
    return mylist;
};



const uret=()=>{
    let sayitipleri=["`asal`","`palindrom`","`armstrong`","`mükemmel`","`kare`","`küp`","`ters-bölünür`","`fibonacci`"];
    let secim=parseInt(prompt("Üretim için seçin : Rastgele[0] - Belirli Aralıktan[1] : "));
    let altaralik;
    let ustaralik;
    let listem=[];
    
    if(secim==1){
        altaralik=parseInt(prompt("Alt aralık : "));
        ustaralik=parseInt(prompt("Üst aralık : "));
        if(altaralik>ustaralik){
            let temp=ustaralik;
            ustaralik=altaralik;
            altaralik=temp;
        }
    }else{
        altaralik=Math.floor(Math.random()*100);
        ustaralik=altaralik+100;
    }
    
    let adet=parseInt(prompt("Kaç adet üretim yapalım : "));
    let tur=parseInt(prompt("Hangi Türden üretim yapılacak:\n[0] ASAL\t[1] PALİNDROM\n[2] ARMSTRONG\t[3] MÜKEMMEL\n[4] KARE\t[5] KÜP\t[6] TERS BÖLÜNÜR\n[7] FİBONACCİ"));
    
    console.log("Üretim Başladı...");
    
    if(secim==0){
        // Rastgele üretim için aralığı genişletme mantığı
        for(let j=altaralik;(j<ustaralik)&&(listem.length<adet);j++)
        {
            switch(tur){
                case 0: // DÜZELTME: string yerine number
                    asalmi(j)?listem.push(j):false;
                    break;
                case 1:
                    palindrommu(j)?listem.push(j):false;
                    break;
                case 2:
                    armstrongmu(j)?listem.push(j):false;
                    break;
                case 3:
                    mukemmelmi(j)?listem.push(j):false;
                    break;
                case 4:
                    karesayi(j)?listem.push(j):false;
                    break;
                case 5:
                    kupsayi(j)?listem.push(j):false;
                    break;
                case 6:
                    tersbolunurmu(j)?listem.push(j):false;
                    break;
                case 7:
                    fibonaccimi(j)?listem.push(j):false;
                    break;
                default:
                    break;
            }
            // Aralık sonuna gelindi ama yeterli sayı bulunamadıysa aralığı genişlet
            if(listem.length<adet&&j==ustaralik-1){
                ustaralik+=ustaralik*5;
            }
        }
        console.log("---------------\n↓ Üretilen "+sayitipleri[tur]+" Sayılar ↓\n["+altaralik+"-"+ustaralik+"]");
        console.log(listem);
        for(let sayim=0; sayim<listem.length; sayim++){ // DÜZELTME: for-in yerine for loop
            console.log(listem[sayim]);
        }
    }
    else
    {
        for(let j=altaralik;(j<=ustaralik)&&(listem.length<adet);j++) // DÜZELTME: <= kullanıldı
        {
            switch(tur){
                case 0: // DÜZELTME: consistent number kullanımı
                    console.log("BURADA");
                    asalmi(j)?listem.push(j):false;
                    break;
                case 1:
                    palindrommu(j)?listem.push(j):false;
                    break;
                case 2:
                    armstrongmu(j)?listem.push(j):false;
                    break;
                case 3:
                    mukemmelmi(j)?listem.push(j):false;
                    break;
                case 4:
                    karesayi(j)?listem.push(j):false;
                    break;
                case 5:
                    kupsayi(j)?listem.push(j):false;
                    break;
                case 6:
                    tersbolunurmu(j)?listem.push(j):false;
                    break;
                case 7:
                    fibonaccimi(j)?listem.push(j):false;
                    break;
                default:
                    break;
            }
        }
        console.log("Belirtilen aralıkta "+listem.length+" adet "+sayitipleri[tur]+" sayı üretimi yapılabildi...");
        console.log("---------------\n↓ Üretilen "+sayitipleri[tur]+" Sayılar ↓\n["+altaralik+"-"+ustaralik+"]");
        console.log(listem);
        for(let sayim=0; sayim<listem.length; sayim++){ // DÜZELTME: for-in yerine for loop
            console.log(listem[sayim]);
        }
    }
    
    console.log("Üretim Tamamlandı");
};


const sorgu=(sayi)=>{
return sayi+"<-\n-----------\n"+
        "ASAL "+(asalmi(sayi)?"[YES]\n":"[NO]\n")+
        "PALİNDROM "+(palindrommu(sayi)?"[YES]\n":"[NO]\n")+
        "ARMSTRONG "+(armstrongmu(sayi)?"[YES]\n":"[NO]\n")+
        "MÜKEMMEL "+(mukemmelmi(sayi)?"[YES]\n":"[NO]\n")+
        "KARE "+(karesayi(sayi)?"[YES]\n":"[NO]\n")+
        "KÜP "+(kupsayi(sayi)?"[YES]\n":"[NO]\n")+
        "TERS-BÖLÜNÜR "+(tersbolunurmu(sayi)?"[YES]\n":"[NO]\n")+
        "FİBONACCİ "+(fibonaccimi(sayi)?"[YES]\n":"[NO]\n-----------------\n")            
        ;

}

const incele=()=>{
    alert("İnceleme Programı Girilen Sayının veya Aralığın\nNe Olduğunu Anlamak Üzere Oluşturulmuştur...");
    let sayi=prompt("[0] Belirli Sayı\n[1] Belirli Aralık");
    let out;
    switch(sayi){
        case "0":
            let arastirilsin=prompt("Sayı : ");
            alert("↓ Soruşturma Tamamlandı ↓");
            out=sorgu(arastirilsin);
            alert(out);
            console.log(out);
            break;
        case "1":
            let alt=prompt("Alt aralık : ");
            let ust=prompt("Üst aralık : ");
            let temp;
            if(alt>ust){temp=alt;alt=ust;ust=temp}
            for(let i =alt;i<=ust;i++){
                console.log(sorgu(i));
            }
            break;
        default:
            alert("Geçersiz Giriş...");
            break;
        
    }
}

alert("Sayıların Dünyasına Hoşgeldiniz...\n(Devam etmek için `tamam`a basınız...)");
let secim=prompt("İşlemi Seçiniz\n\n1-Üretmek\n2-İncelemek\n3-Çıkmak");
switch(secim){
    case "1":
        uret();
        break;
    case "2":
        incele();
        break;
    case "3":
        alert("Çıkış Yapılıyor...");
        break;
    default:
        alert("Geçersiz Giriş...");
        break;
}