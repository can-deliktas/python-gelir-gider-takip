import json
import os

data_path = "data/"

def toplam_gelir():
    dosya_yolu = os.path.join(data_path, "gelirler.json")
    with open(dosya_yolu, "r") as f:
        gelirler = json.load(f)
    return sum(gelirler)

def toplam_gider():
    dosya_yolu = os.path.join(data_path, "giderler.json")
    with open(dosya_yolu, "r") as f:
        giderler = json.load(f)
    return sum(giderler)
