import numpy as np

def midpoint(func, a: float, b: float, eps: float = 0.0001, *args, **kwargs) -> float:
    """
    Aturan titik tengah berfungsi mengoptimasi metode segiempat
    Dengan aturan ini, metode segiempat membagi domain integrasi
    sebanyak n buah dan menjumlahkan seluruh luas segi empat dengan dimensi
    (a + b)/n * f(x), dimana x adalah titik tengah segiempat

    Parameter:
    f   = fungsi input
    a   = batas bawah integrasi
    b   = batas atas integrasi
    eps = error relatif maksimal
    """
    try:
        n = 100
        x = np.linspace(a, b, n)
        dx = x[1] - x[0]
        L0 = sum([dx * func(i+dx/2, *args, **kwargs) for i in x])
        err = 1
        while err > eps:
            n += 1
            x = np.linspace(a, b, n)
            dx = x[1] - x[0]
            L1 = sum([dx * func(i + dx/2, *args, **kwargs) for i in x])
            err = np.abs(L1 - L0)/np.abs(L1)
            L0 = L1
    except Exception:
        raise RuntimeError('Integrasi gagal, pastikan fungsi anda benar!')
    return L1  

if __name__ == "__main__":
    def f(x: float) -> float: x**3
    print(midpoint(f, 0, 1))

