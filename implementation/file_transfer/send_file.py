import socket


def send_file(filename: str = "textfile.txt", testing: bool = False) -> None:
    port = 4412
    sock = socket.socket()
    host = socket.gethostname()
    sock.bind((host, port))
    sock.listen(5)

    print("server jalan..!")

    while True:
        conn, addr = sock.accept()
        print(f"terkoneksi.. ke {addr}")
        data = conn.recv(1024)
        print(f"diterima .. {data}")

        with open(filename, "rb") as in_file:
            data = in_file.read(1024)
            while data:
                conn.send(data)
                data = in_file.read(1024)

        print("terkirim")

        conn.close()
        if testing:
            break

        sock.shutdown(1)
        sock.close()


if __name__ == "__main__":
    send_file()
