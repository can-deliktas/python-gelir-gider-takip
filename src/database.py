import json
import os
from src.hesaplama import toplam_gelir, toplam_gider  

data_path = "data/"

def dosya_kontrol():
    """Gerekli JSON dosyalarının olup olmadığını kontrol eder, yoksa oluşturur."""
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    for dosya in ["gelirler.json", "giderler.json"]:
        dosya_yolu = os.path.join(data_path, dosya)
        if not os.path.exists(dosya_yolu):
            with open(dosya_yolu, "w") as f:
                json.dump([], f)

def formatli_sayi_girisi(mesaj):
    """Kullanıcının girdiği Türkçe formatlı sayıyı float'a çevirir."""
    while True:
        try:
            girdi = input(mesaj).strip()  # Boşlukları temizle
            girdi = girdi.replace(".", "").replace(",", ".")  # 1.000.000,75 → 1000000.75
            return float(girdi)
        except ValueError:
            print("Hata: Geçersiz sayı formatı! Lütfen yalnızca sayı girin.")

def veri_ekle(dosya_adi, miktar):
    """Belirtilen JSON dosyasına yeni bir miktar ekler."""
    dosya_yolu = os.path.join(data_path, dosya_adi)

    try:
        with open(dosya_yolu, "r") as f:
            mevcut_veri = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        mevcut_veri = []

    mevcut_veri.append(miktar)  # Miktarı doğrudan ekliyoruz, tekrar dönüştürme yapmıyoruz!
    
    with open(dosya_yolu, "w") as f:
        json.dump(mevcut_veri, f, indent=4)

def verileri_temizle():
    """Tüm gelir ve gider verilerini sıfırlar."""
    for dosya in ["gelirler.json", "giderler.json"]:
        dosya_yolu = os.path.join(data_path, dosya)
        with open(dosya_yolu, "w") as f:
            json.dump([], f)
    print("Tüm veriler temizlendi.")

def verileri_duzenle(dosya_adi):
    """Belirtilen dosyadaki verileri düzenleme imkanı sunar."""
    dosya_yolu = os.path.join(data_path, dosya_adi)

    try:
        with open(dosya_yolu, "r") as f:
            veriler = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Dosya bulunamadı veya bozuk.")
        return

    if not veriler:
        print("Bu dosyada düzenlenecek veri bulunmuyor.")
        return

    print("\nMevcut veriler:")
    for i, miktar in enumerate(veriler):
        print(f"{i + 1}. {miktar:,.2f} TL")

    try:
        secim = int(input("Düzenlemek istediğiniz kaydın numarasını girin: ")) - 1
        if 0 <= secim < len(veriler):
            yeni_miktar = formatli_sayi_girisi("Yeni değeri girin: ")
            veriler[secim] = yeni_miktar
            with open(dosya_yolu, "w") as f:
                json.dump(veriler, f, indent=4)
            print("Veri başarıyla güncellendi.")
        else:
            print("Geçersiz seçim.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def kalan_bakiye():
    """Toplam geliri ve gideri hesaplayarak kalan bakiyeyi döndürür."""
    return toplam_gelir() - toplam_gider()
