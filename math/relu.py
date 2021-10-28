"""
Activation Function ReLU

ReLU (Rectified Linear Unit) merupakan salah satu fungsi aktivasi
yang biasa digunakan pada projek Machine Learning dan Deep Learning
khususnya yang menggunakan Artificial Neural Network.

Cara kerja ReLU sederhana, fungsi akan mengembalikan nilai 0 jika
nilai input kurang dari 0. Jika fungsi diberi input nilai
lebih dari 0 maka nilai yang dikembalikan adalah nilai input itu.

>>> relu(1.0)
1.0

>>> relu(0.0)
0.0
"""


def relu(x: float):
    if x > 0.0:
        return x
    else:
        return 0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Nilai input lebih dari 0
    print(relu(30.0))

    # Nilai input kurang dari 0
    print(relu(-30.0))

    # Nilai input sama dengan 0
    print(relu(0.0))

    # Nilai banyak sekali
    print(relu(193279812837917298371927.0))
