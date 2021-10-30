# menampilkan informasi dari corona


import requests
from bs4 import BeautifulSoup


def status_covid(url: str = "https://www.worldometers.info/coronavirus") -> dict:
    """
    menampilkan informasi covid 19 statistiknya
    """
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    find_data = soup.findAll("h1")
    values = soup.findAll("div", {"class": "maincounter-number"})
    find_data += soup.findAll("span", {"class": "panel-title"})
    values += soup.findAll("div", {"class": "number-table-main"})

    return {
        key.text.strip(): value.text.strip() for key, value in zip(find_data, values)
    }


if __name__ == "__main__":
    print("status corona")
    for find_data, values in status_covid().items():
        print(f"{find_data} : {values}")
