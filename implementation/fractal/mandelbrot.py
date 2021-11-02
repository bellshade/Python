# Himpunan Mandelbrot adalah himpunan bilangan kompleks "c" yang deretnya
# "z_(n+1) = z_n * z_n + c" tidak divergen, yaitu tetap dibatasi. Jadi,
# bilangan kompleks "c"
# adalah anggota himpunan Mandelbrot jika, ketika dimulai dengan
# "z_0 = 0" dan menerapkan iterasi berulang kali, nilai absolut dari
# "z_n" tetap dibatasi untuk semua "n > 0".
# Bilangan kompleks dapat ditulis sebagai
# "a + b*i": "a" adalah komponen real, biasanya digambarkan
# pada sumbu x, dan "b*i"
# adalah komponen imajiner, biasanya digambar pada sumbu y.
# Kebanyakan visualisasi
# dari himpunan Mandelbrot menggunakan kode warna
# untuk menunjukkan setelah berapa banyak langkah dalam
# deret bilangan di luar himpunan divergen. Gambar set Mandelbrot
# menunjukkan batas yang rumit dan sangat rumit yang mengungkapkan
# detail rekursif yang semakin halus pada peningkatan perbesaran, membuat
# batas Mandelbrot menetapkan kurva fraktal.

import colorsys

from PIL import Image  # type: ignore


def get_distance(x: float, y: float, max_step: int) -> float:
    """
    Return jarak relatif (= step/max_step) setelah itu bilangan kompleks
    dibentuk oleh pasangan xy ini divergen.
    Anggota himpunan Mandelbrot tidak
    divergen sehingga jaraknya adalah 1.
    """
    a = x
    b = y
    for step in range(max_step):
        a_new = a * a - b * b + x
        b = 2 * b + y
        a = a_new

        # divergensi terjadi untuk semua
        # bilangan kompleks dengan nilai absolut
        # lebih besar dari 4
        if a * a + b * b > 4:
            break
    return step / (max_step - 1)


def get_black_and_white_rgb(distance: float) -> tuple:
    """
    Kode warna hitam putih yang mengabaikan jarak relatif.
    Mandelbrot set berwarna hitam, yang lainnya putih.
    >>> get_black_and_white_rgb(0)
    (255, 255, 255)
    >>> get_black_and_white_rgb(0.5)
    (255, 255, 255)
    >>> get_black_and_white_rgb(1)
    (0, 0, 0)
    """
    if distance == 1:
        return (0, 0, 0)
    else:
        return (255, 255, 255)


def get_color_coded_rgb(distance: float) -> tuple:
    """
    >>> get_color_coded_rgb(0)
    (255, 0, 0)
    >>> get_color_coded_rgb(0.5)
    (0, 255, 255)
    >>> get_color_coded_rgb(1)
    (0, 0, 0)
    """
    if distance == 1:
        return (0, 0, 0)
    else:
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(distance, 1, 1))


def get_image(
    image_width: int = 800,
    image_height: int = 600,
    figure_center_x: float = -0.6,
    figure_center_y: float = 0,
    figure_width: float = 3.2,
    max_step: int = 50,
    use_distance_color_coding: bool = True,
) -> Image.Image:
    """
    Menggambar himpunan Mandelbrot dalam bentuk
    image.
    >>> get_image().load()[0,0]
    (255, 0, 0)
    >>> get_image(use_distance_color_coding = False).load()[0,0]
    (255, 255, 255)
    """
    img = Image.new("RGB", (image_width, image_height))
    pixels = img.load()

    for image_x in range(image_width):
        for image_y in range(image_height):
            figure_height = figure_width / image_width * image_height
            figure_x = figure_center_x + (image_x / image_width - 0.5) * figure_width
            figure_y = figure_center_y + (image_y / image_height - 0.5) * figure_height

            distance = get_distance(figure_x, figure_y, max_step)
            if use_distance_color_coding:
                pixels[image_x, image_y] = get_color_coded_rgb(distance)
            else:
                pixels[image_x, image_y] = get_black_and_white_rgb(distance)
    return img


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # img = get_image()
    # img.save("testing.png")
    # img.show()
