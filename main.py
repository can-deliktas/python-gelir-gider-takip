from src.database import veri_ekle, kalan_bakiye, verileri_temizle, verileri_duzenle, dosya_kontrol
from src.hesaplama import toplam_gelir, toplam_gider
from src.tavsiyeler import tavsiye_ver

def formatli_sayi_girisi(mesaj):
    """Kullanıcının girdiği sayıyı doğru formata çevirir. Örn: '1.000.000,75' → 1000000.75"""
    while True:
        try:
            girdi = input(mesaj).strip()  # Boşlukları temizle
            girdi = girdi.replace(".", "").replace(",", ".")  # 1.000.000,75 → 1000000.75
            return float(girdi)
        except ValueError:
            print("Hatalı giriş! Lütfen yalnızca sayı girin.")

def main():
    dosya_kontrol()  # Eksik dosyalar varsa oluştur

    while True:
        print("\n=== Gelir-Gider Takip Programı ===")
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Kalan Bakiyeyi Gör")
        print("4. Tavsiye Al")
        print("5. Çıkış")
        print("6. Verileri Temizle")
        print("7. Gelirleri Düzenle")
        print("8. Giderleri Düzenle")

        secim = input("Seçiminizi yapın: ").strip()

        if secim == "1":
            miktar = formatli_sayi_girisi("Gelir miktarını girin: ")
            veri_ekle("gelirler.json", miktar)
            print(f"{miktar:,.2f} TL gelir olarak eklendi.")
        elif secim == "2":
            miktar = formatli_sayi_girisi("Gider miktarını girin: ")
            veri_ekle("giderler.json", miktar)
            print(f"{miktar:,.2f} TL gider olarak eklendi.")
        elif secim == "3":
            print(f"Kalan bakiye: {kalan_bakiye():,.2f} TL")
        elif secim == "4":
            print("Tavsiye: " + tavsiye_ver(kalan_bakiye()))
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        elif secim == "6":
            verileri_temizle()
            print("Tüm veriler temizlendi!")
        elif secim == "7":
            verileri_duzenle("gelirler.json")
        elif secim == "8":
            verileri_duzenle("giderler.json")
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
