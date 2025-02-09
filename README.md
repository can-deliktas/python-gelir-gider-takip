# **Gelir-Gider Takip Programı**

Bu Python programı, kullanıcıların aylık gelirlerini ve giderlerini kaydetmesine, kalan bakiyeyi hesaplamasına ve **akıllı finansal öneriler almasına** yardımcı olur.

## 🚀 **Özellikler**
✔ Gelir ve gider ekleme  
✔ Kalan bakiyeyi anlık görüntüleme  
✔ Kişisel finans durumuna göre **akıllı tavsiyeler**  
✔ Verileri düzenleme ve temizleme seçeneği  
✔ Kullanıcı dostu arayüz  
✔ JSON dosyalarıyla veri kaydetme  

---

## 📥 **Kurulum**  

### **1️⃣ Depoyu Klonlayın**  
Aşağıdaki komutu kullanarak projeyi bilgisayarınıza indirin:  
```bash
git clone https://github.com/kullaniciadi/gelir-gider-takip.git
cd gelir-gider-takip
```

### **2️⃣ Gerekli Bağımlılıkları Yükleyin**  
Bu proje Python 3+ gerektirir. Bağımlılıkları yüklemek için:  
```bash
pip install -r requirements.txt
```

### **3️⃣ Programı Çalıştırın**  
```bash
python main.py
```

---

## 🎯 **Kullanım**  
Programı başlattığınızda aşağıdaki menü görüntülenecektir:  
```
=== Gelir-Gider Takip Programı ===
1. Gelir Ekle
2. Gider Ekle
3. Kalan Bakiyeyi Gör
4. Tavsiye Al
5. Verileri Temizle
6. Verileri Düzenle
7. Çıkış
```

### 📌 **İşlevler:**
✅ **Gelir Ekle:** `1` seçeneğini seçerek gelir miktarınızı ekleyin.  
✅ **Gider Ekle:** `2` seçeneğini seçerek giderlerinizi kaydedin.  
✅ **Kalan Bakiyeyi Gör:** `3` seçeneği ile güncel mali durumunuzu öğrenin.  
✅ **Tavsiye Al:** `4` seçeneği, **finansal durumunuza göre akıllı öneriler sunar**.  
✅ **Verileri Temizle:** `5` seçeneği, tüm kayıtları sıfırlar.  
✅ **Verileri Düzenle:** `6` seçeneği ile yanlış girilen verileri değiştirebilirsiniz.  
✅ **Çıkış:** `7` ile programdan güvenli bir şekilde çıkabilirsiniz.  

---

## 📂 **Proje Dosya Yapısı**  
```
gelir_gider_takip/
│── README.md                 # Proje dökümantasyonu
│── main.py                   # Ana program
│── requirements.txt           # Gerekli bağımlılıklar
│── data/                      # JSON veri dosyaları
│   ├── gelirler.json          # Kayıtlı gelirler
│   ├── giderler.json          # Kayıtlı giderler
│── src/                       # Programın ana işlevlerini içeren modüller
│   ├── database.py            # Veri okuma/yazma işlemleri
│   ├── hesaplama.py           # Gelir-gider hesaplamaları
│   ├── tavsiyeler.py          # Finansal öneriler
│── ui/                        # Arayüz modülleri
│   ├── giris_ekrani.py        # (Geliştirme aşamasında) Grafiksel UI
│── tests/                     # Test dosyaları
│   ├── test_hesaplama.py      # Otomatik testler
```

---

## 🤖 **Akıllı Tavsiye Sistemi**  
Bu program, **gelir ve giderlerinizi analiz ederek** size finansal durumunuza uygun öneriler sunar:  

💰 **Kalan Bakiye < 0** → Acil tasarruf yapmalısınız, gereksiz harcamaları azaltın!  
💳 **0 TL bakiye** → Harcamalarınızı dikkatlice yönetin, acil durum fonu oluşturun.  
📈 **5.000 TL < Bakiye < 20.000 TL** → Yatırım yapmaya başlamalısınız.  
🏦 **50.000 TL+ Bakiye** → Profesyonel yatırım seçeneklerini değerlendirebilirsiniz.  

---

## 🛠 **Önerilen Geliştirmeler**  
Bu proje **açık kaynak** olup, geliştirmeye açıktır! 🎉 Aşağıdaki özellikler eklenebilir:  

✅ **Grafiksel Arayüz (GUI)** → Kullanıcı dostu bir pencere uygulaması  
✅ **Grafik & İstatistikler** → Gelir-gider değişimlerini gösteren görseller  
✅ **Mobil Uygulama Desteği** → Android/iOS için bir versiyon  
✅ **Yapay Zeka Destekli Finansal Öneriler**  

---

## 📢 **Katkıda Bulunma (Pull Request Rehberi)**  
Projeye katkıda bulunmak için şu adımları izleyebilirsiniz:  

### **1️⃣ Depoyu Fork Edin**  
GitHub'da "Fork" butonuna tıklayarak projeyi kendi hesabınıza kopyalayın.  

### **2️⃣ Yeni Bir Branch Açın**  
```bash
git checkout -b yeni-ozellik
```

### **3️⃣ Değişiklikleri Yapın ve Commit Edin**  
```bash
git add .
git commit -m "Yeni özellik eklendi"
```

### **4️⃣ Değişiklikleri Fork’unuza Gönderin**  
```bash
git push origin yeni-ozellik
```

### **5️⃣ Pull Request Gönderin**  
GitHub’a gidin, projenin orijinal deposunu açın ve "New Pull Request" seçeneğiyle kodunuzu incelemeye gönderin.  

---

## 📜 **Lisans**  
Bu proje **MIT Lisansı** ile lisanslanmıştır. Özgürce kullanabilir ve geliştirebilirsiniz.
