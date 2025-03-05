if __name__ == "__main__":
    import socket

    sock = socket.socket()
    host = socket.gethostname()
    port = 4412

    sock.connect((host, port))
    sock.send(b"hellotesting!")

    with open("Received_file", "wb") as out_file:
        print("file terbuka")
        print("menerima data")
        while True:
            data = sock.recv(1024)
            print(f"{data}")
            if not data:
                break
            out_file.write(data)

    print("data didapatkan")
    sock.close()
    print("tutup koneksi")
