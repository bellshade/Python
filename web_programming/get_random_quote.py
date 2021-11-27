import requests
import json


def get_random_quote():
    url = "https://api.quotable.io/random"
    r = requests.get(url)
    quote = json.loads(r.text)
    return quote


def main():
    import os

    quote = get_random_quote()

    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\n{quote['content']} - {quote['author']}")

    if input("\n\nKetik 'y' untuk coba lagi: ") == 'y':
        main()


if __name__ == '__main__':
    main()
