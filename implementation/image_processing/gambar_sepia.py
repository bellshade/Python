import numpy as np
from cv2 import destroyAllWindows, imread, imshow, waitKey


def gambar_sepia(img, skala: int) -> np.ndarray:
    """
    sepia adalah nuansa warna tua yang terbentuk dari campuran warna coklat dan
    abu-abu. nama "Sepia" berasal dari tinta berwarna coklat yang ditemukan
    dalam cumi-cumi jenis sepia

    Args:
        img (np.ndarray): gambar masukkan, representasi dari numpy array
        skala (int): skala sepia yang diterapkan. skala lebih tinggi akan
                     menghasilkan efek sepia yang lebih kuat.

    Return:
        (np.ndarray) : gambar dengan efek sepia yang dihasilkan dalam bentuk
                       array numpy
    """
    piksel_h, piksel_v = img.shape[0], img.shape[1]

    def ke_grayscale(biru: int, hijau: int, merah: int) -> float:
        """
        fungsi untuk menciptkan representasi grayscale dari piksel

        Args:
            biru (int): nilai warna dari biru 0 - 255
            hijau (int): nilai warna dari hijau 0 - 255
            merah (int): nilai warna dari merah 0 - 255

        Return:
            (float): representasi grayscale dari piksel
        """
        return 0.2126 * merah + 0.587 * hijau + 0.114 * biru

    def normalisasi_nilai_warna(nilai: int) -> int:
        """
        fungsi untuk normalisasi nilai warna dari merah hijau biru
        jika nilai tersebut lebih dari 255

        Args:
            nilai (int): nilai yang diberikan

        Return:
            (int): mengembalikan nilai minimal dari 255
        """
        return min(nilai, 255)

    for i in range(piksel_h):
        for j in range(piksel_v):
            grayscale = int(ke_grayscale(*img[i][j]))
            img[i][j] = [
                normalisasi_nilai_warna(grayscale),
                normalisasi_nilai_warna(grayscale + skala),
                normalisasi_nilai_warna(grayscale + 2 * skala),
            ]

    return img


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    gambar = {
        presentasi: imread("data_image/example_image.jpg", 1)
        for presentasi in (10, 20, 30, 40)
    }

    for presentasi, img in gambar.items():
        gambar_sepia(img, presentasi)

    for presentasi, img in gambar.items():
        imshow(f"gambar asli dari sepia (skala: {presentasi})", img)

    waitKey(0)
    destroyAllWindows()
