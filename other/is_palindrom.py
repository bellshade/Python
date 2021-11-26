def is_palindrom(x: str) -> bool:
    normalized = x.lower().replace(" ", "")
    
    return normalized == normalized[::-1]

def main(args=None):
    print(is_palindrom("katak"))            # output "True"
    print(is_palindrom("label"))            # output "False"
    print(is_palindrom("Kasur ini rusak"))  # output "True"


if __name__ == '__main__':
    main()
