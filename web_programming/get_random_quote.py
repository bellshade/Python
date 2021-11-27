import requests
import json


def get_random_quote():
    url = "https://api.quotable.io/random"
    r = requests.get(url)
    quote = json.loads(r.text)
    return quote


def main():
    quote = get_random_quote()

    print(f"\n\n{quote['content']} - {quote['author']}")


if __name__ == '__main__':
    main()
