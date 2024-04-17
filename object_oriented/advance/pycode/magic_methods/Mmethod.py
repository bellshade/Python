class Pastikom:

    def __init__(self, yourname: str, email: str) -> None:
        """Magic Method
        Kelas Pastikom memiliki 2 parameter dan/atau argumen
        :param yourname: tuliskan nama mu di parameter pertama
        :param email: tuliskan email mu di parameter ke dua
        nama = 'Bellshade'
        email = bellshade@pastikom.id
        >>> Pastikom(nama, email)
        Nama: Bellshade
        Email: bellshade@pastikom.id
        """
        self.name = yourname
        self.email = email

    def __repr__(self) -> str:
        """Fungsi representasi nilai parameter dan/atau argumen"""
        return f"Nama: { self.name }\nEmail: { self.email }"

    def __del__(self) -> str:
        """Fungsi informasi jika ada nilai parameter dan/atau argumen yang terhapus"""
        return "Oh tidaaaak! Data sudah terhapus :'("


nama: str = "Bellshade"
email: str = "bellshade@pastikom.id"
if __name__ == "__main__":
    Pastikom(nama, email)
