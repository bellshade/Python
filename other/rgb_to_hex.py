def rgb_to_hex(r: int, g: int, b: int) -> str:
    result = ""

    for x in (r, g, b):
        if x < 0:
            x = 0
        elif x > 255:
            x = 255

        result += f"{x:02X}"

    return result


def rgb_to_hex_v2(r: int, g: int, b: int) -> str:
    return "".join([
        "00" if x <= 0
        else "FF" if x >= 255
        else f"{x:02X}"
        for x in (r, g, b)
    ])


def main(args=None):
    print(rgb_to_hex(0, 0, 0))        # returns 000000
    print(rgb_to_hex(1, 2, 3))        # returns 010203
    print(rgb_to_hex(255, 255, 255))  # returns FFFFFF
    print(rgb_to_hex(-10, 255, 300))  # returns 00FFFF
    print(rgb_to_hex(150, 0, 180))    # returns 9600B4


if __name__ == '__main__':
    main()
