# contoh sederhana emisi CO2 dari sebuah negara inggris
# yang menggunakan API dari https://api.carbonintensity.org.uk

from datetime import date

import requests

BASE_URL = "https://api.carbonintensity.org.uk/intensity"


# emisi dalam setengah jam terakhir
def emisi_stngh_jam() -> str:
    setengah_jam = requests.get(BASE_URL).json()["data"][0]
    return setengah_jam["intensity"]["actual"]


# emisi dalam waktu spesifik
def emisi(start, end) -> list:
    return requests.get(f"{BASE_URL}/{start}/{end}").json()["data"]


if __name__ == "__main__":
    for entry in emisi(start=date(2020, 10, 1), end=date(2020, 10, 3)):
        print("dari {from} ke {to}: {intensity[actual]}".format(**entry))
    print(f"{emisi_stngh_jam()}")
