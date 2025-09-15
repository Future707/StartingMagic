/* 
    Script: p7_urunArama/script.js
    Açıklama: Siteden Urun Arama için gerekli JavaScript kodları.
    Yazar: [Future Developer]
    Tarih: [25.08.2025]
    Sürüm: 1.00

    Not: Bu dosya, StartingMagic platformunda yer alan eğitim amaçlı bir örnektir.
*/

/*
    İçerik:
    - Kullanıcı Paneli(Kullanıcı - 123) / Admin Paneli (Admin - 123)
    - Ürün Ekleme, Güncelleme, Silme [ADMİN İŞLEMLERİ] 
    - Ürün Arama, Sepete Ekleme, Ürün Filtreleme Mekanizması [KULLANICI İŞLEMLERİ]
    - Peşinat ve Taksit Seçenekleri
    - Çıkış
*/


// ---------------- KOZMETİK ----------------
let kozmetik = [
  { isim: "Parfüm", marka: "Dior", model: "Sauvage", yil: 2023, fiyat: 2500 },
  { isim: "Ruj", marka: "MAC", model: "Ruby Woo", yil: 2022, fiyat: 750 },
  { isim: "Fondöten", marka: "Maybelline", model: "Fit Me", yil: 2021, fiyat: 350 },
  { isim: "Maskara", marka: "L’Oreal", model: "Voluminous Lash", yil: 2022, fiyat: 280 },
  { isim: "Allık", marka: "Nars", model: "Orgasm", yil: 2023, fiyat: 600 },
  { isim: "Oje", marka: "Essie", model: "Classic Red", yil: 2023, fiyat: 120 },
  { isim: "Şampuan", marka: "Pantene", model: "Keratin", yil: 2022, fiyat: 90 },
  { isim: "Krem", marka: "Clinique", model: "Moisture Surge", yil: 2023, fiyat: 950 },
  { isim: "Deodorant", marka: "Rexona", model: "Active", yil: 2022, fiyat: 80 },
  { isim: "Saç Spreyi", marka: "Taft", model: "Power Hold", yil: 2021, fiyat: 150 }
];

// ---------------- GİYİM ----------------
let giyim = [
  { isim: "Tişört", marka: "Nike", model: "Sportswear", yil: 2023, fiyat: 450 },
  { isim: "Pantolon", marka: "Levis", model: "501 Original", yil: 2022, fiyat: 1200 },
  { isim: "Gömlek", marka: "Zara", model: "Slim Fit", yil: 2023, fiyat: 650 },
  { isim: "Etek", marka: "Mango", model: "Mini Skirt", yil: 2023, fiyat: 500 },
  { isim: "Elbise", marka: "H&M", model: "Casual Dress", yil: 2022, fiyat: 800 },
  { isim: "Mont", marka: "Columbia", model: "Winter Jacket", yil: 2023, fiyat: 3200 },
  { isim: "Spor Ayakkabı", marka: "Adidas", model: "Ultraboost", yil: 2023, fiyat: 2800 },
  { isim: "Şort", marka: "Puma", model: "Training Shorts", yil: 2022, fiyat: 400 },
  { isim: "Kazak", marka: "LC Waikiki", model: "Classic Knit", yil: 2023, fiyat: 350 },
  { isim: "Takım Elbise", marka: "Damat", model: "Slim Fit", yil: 2023, fiyat: 4500 }
];

// ---------------- ELEKTRONİK ----------------
let elektronik = [
  { isim: "Telefon", marka: "Apple", model: "iPhone 15", yil: 2023, fiyat: 48000 },
  { isim: "Laptop", marka: "Dell", model: "XPS 13", yil: 2023, fiyat: 35000 },
  { isim: "Tablet", marka: "Samsung", model: "Galaxy Tab S9", yil: 2023, fiyat: 18000 },
  { isim: "Televizyon", marka: "LG", model: "OLED55", yil: 2022, fiyat: 25000 },
  { isim: "Kulaklık", marka: "Sony", model: "WH-1000XM5", yil: 2023, fiyat: 12500 },
  { isim: "Konsol", marka: "Sony", model: "PlayStation 5", yil: 2023, fiyat: 21000 },
  { isim: "Monitör", marka: "Asus", model: "ROG Swift", yil: 2023, fiyat: 15000 },
  { isim: "Akıllı Saat", marka: "Apple", model: "Watch Series 9", yil: 2023, fiyat: 12000 },
  { isim: "Fotoğraf Makinesi", marka: "Canon", model: "EOS R7", yil: 2023, fiyat: 30000 },
  { isim: "Hoparlör", marka: "JBL", model: "Charge 5", yil: 2023, fiyat: 5000 }
];

// ---------------- KIRTASİYE ----------------
let kirtasiye = [
  { isim: "Defter", marka: "Moleskine", model: "Classic Notebook", yil: 2023, fiyat: 250 },
  { isim: "Kalem", marka: "Parker", model: "Jotter", yil: 2023, fiyat: 400 },
  { isim: "Silgi", marka: "Faber-Castell", model: "Dust-Free", yil: 2022, fiyat: 20 },
  { isim: "Çanta", marka: "Eastpak", model: "Padded Pak’r", yil: 2023, fiyat: 1500 },
  { isim: "Kalem Kutusu", marka: "Deli", model: "Pencil Case", yil: 2023, fiyat: 150 },
  { isim: "Çizim Defteri", marka: "Canson", model: "Sketchbook", yil: 2023, fiyat: 300 },
  { isim: "Boya Seti", marka: "Faber-Castell", model: "12’li Kuru Boya", yil: 2023, fiyat: 90 },
  { isim: "Çöp Defteri", marka: "Oxford", model: "A4 Spiralli", yil: 2022, fiyat: 60 },
  { isim: "Çizim Kalemi", marka: "Rotring", model: "Tikky 0.5", yil: 2023, fiyat: 250 },
  { isim: "Post-it", marka: "3M", model: "Post-it", yil: 2023, fiyat: 70 }
];

// ---------------- VASITALAR ----------------
let vasitalar = [
  { isim: "Araba", marka: "BMW", model: "320i", yil: 2023, fiyat: 1850000 },
  { isim: "Motosiklet", marka: "Yamaha", model: "MT-07", yil: 2023, fiyat: 400000 },
  { isim: "Bisiklet", marka: "Giant", model: "Escape 3", yil: 2022, fiyat: 15000 },
  { isim: "Kamyon", marka: "Mercedes-Benz", model: "Actros", yil: 2023, fiyat: 3500000 },
  { isim: "Otobüs", marka: "MAN", model: "Lion’s Coach", yil: 2023, fiyat: 4500000 },
  { isim: "Scooter", marka: "Xiaomi", model: "Mi Electric Scooter 4", yil: 2023, fiyat: 18000 },
  { isim: "Uçak", marka: "Cessna", model: "172 Skyhawk", yil: 2023, fiyat: 12000000 },
  { isim: "Gemi", marka: "Princess", model: "Yacht 60", yil: 2023, fiyat: 75000000 },
  { isim: "Traktör", marka: "John Deere", model: "6M", yil: 2023, fiyat: 1800000 },
  { isim: "ATV", marka: "Can-Am", model: "Outlander 450", yil: 2023, fiyat: 250000 }
];

let kategoriler=[kozmetik,giyim,elektronik,kirtasiye,vasitalar];
let filtresec=["isim","marka","model","yil","fiyat"];


const urun_ekle=()=>
{
  alert("Kategori seçin ve içerikleri doldurun...");
  let kategori = parseInt(prompt("Kategori seçin\n1-Kozmetik\n2-Giyim\n3-Elektronik\n4-Kırtasiye\n5-Vasıtalar"));
  let yeniurun={isim:"",marka:"",model:"",yil:0,fiyat:0};
  for(let ind in yeniurun){
    yeniurun[filtresec[ind]] = prompt("Ürünün "+filtresec[ind]+" değerini giriniz : ");
  }
  kategoriler[kategori-1].push(yeniurun);

  let out="Eklenen Ürün ve Yeni Liste\n---------------\nÜrün\n"+yeniurun.isim+"\n---------------\nYeni Liste:\n"+kategoriler[kategori-1];
  console.log(out);
}


const urun_sil=(urunadi)=>{
  let kategoriSilinen;
  let silinenUrun;

  for(let urunler of kategoriler){
  for(let urun of urunler){
    for(let icerik of Object.values(urun)){
        if(icerik.toString().toLowerCase().includes(urunadi)){urunler.splice(urunler.indexOf(urun),1);silinenUrun=urun;kategoriSilinen=urunler;}

    }
  }
}

  let out="Silinme İşlemi Başarılı...("+silinenUrun+")\n"+kategoriSilinen;
  alert(out);
};



const urunfiltre=(girdi)=>{
  let istenenler =new Array();
  for(let urunler of kategoriler){
    for(let urun of urunler){
      for(let icerik of Object.values(urun)){
          if(icerik.toString().toLowerCase().includes(girdi.toLowerCase())){istenenler.push(urun);}

      }
    }
  }

  return istenenler;

    
}


const urun_sorgu = () => {
    let kategori = parseInt(prompt("Kategori seçin\n1-Kozmetik\n2-Giyim\n3-Elektronik\n4-Kırtasiye\n5-Vasıtalar"));
    let filtre = parseInt(prompt("Filtre seçin\n1-İsim\n2-Marka\n3-Model\n4-Yıl\n5-Fiyat"));
    
    let secilenKategori = kategoriler[kategori - 1];
    let secilenFiltre = filtresec[filtre - 1];
    
    let say = 0;
    let out="";
    for (let urun of secilenKategori) {
        out+=((++say)+"-"+ urun[secilenFiltre]+"\n");
    }
    alert("İLGİLİ EŞYALAR\n"+out);
};





alert("Alışveriş Sitesinden Ürün İşlemleri Simülasyonu Uygulaması...");
let kullanıcıtip=prompt("ADMIN >> 0\nKULLANICI >> 1");
if(kullanıcıtip==0){
  let islem = parseInt(prompt("ADMIN işlemleri\n| 1 ürün ekleme\n| 2 ürün silme\n| 3 çıkış"));
  switch(islem){
    case 1:
      urun_ekle();
      break;
    case 2:
      let ara=prompt("Silinecek Ürün :");
      urun_sil(ara);
      break;
    case 3:
      alert("Çıkış Yapılır..");
      break;
    default:
      alert("Geçersiz Giriş..");
      break;
  }
}else{
  let islem = parseInt(prompt("KULLANICI işlemleri\n| 1 Kategorilere Bakmak\n| 2 Filtreli Ürün Bulmak\n| 3 çıkış"));
  switch(islem){
    case 1:
      urun_sorgu();
      break;
    case 2:
      let ara=prompt("Aranacak Ürün :");
      debugger;
      console.log(urunfiltre(ara));
      break;
    case 3:
      alert("Çıkış Yapılıyor...");
      break;
    default:
      alert("Geçersiz Giriş...");
      break;
    
  }
}
