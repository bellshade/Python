from math import atan, cos, radians, sin, tan

from .haversine import haversine


def ellipsoidal_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Hitung jarak terpendek sepanjang permukaan ellipsoid antara
    dua titik di permukaan bumi diberikan garis bujur dan garis lintang

    bumi sebagai ellipsoid memungkinkan kita untuk memperkirakan jarak antara
    titik di permukaan jauh lebih baik daripada bola.
    Rumus ellipsoidal memperlakukan
    Bumi sebagai ellipsoid oblate yang berarti
    memperhitungkan perataan yang terjadi
    di kutub Utara dan Selatan. Rumus Lambert memberikan akurasi pada urutan
    10 meter lebih dari ribuan kilometer. Metode lain dapat menyediakan
    akurasi tingkat milimeter tetapi ini adalah metode yang
    lebih sederhana untuk menghitung jarak jauh
    jarak tanpa meningkatkan intensitas komputasi.

    >>> from collections import namedtuple
    >>> point_2d = namedtuple("point_2d", "lat lon")
    >>> SAN_FRANCISCO = point_2d(37.774856, -122.424227)
    >>> YOSEMITE = point_2d(37.864742, -119.537521)
    >>> NEW_YORK = point_2d(40.713019, -74.012647)
    >>> VENICE = point_2d(45.443012, 12.313071)
    >>> f"{ellipsoidal_distance(*SAN_FRANCISCO, *YOSEMITE):0,.0f} meter"
    '255,819 meter'
    >>> f"{ellipsoidal_distance(*SAN_FRANCISCO, *NEW_YORK):0,.0f} meter"
    '4,165,188 meter'
    >>> f"{ellipsoidal_distance(*SAN_FRANCISCO, *VENICE):0,.0f} meter"
    '9,819,561 meter'
    """
    AXIS_A = 6378137.0
    AXIS_B = 6356752.314245
    EQUATORIAL_RADIUS = 6378137
    flattening = (AXIS_A - AXIS_B) / AXIS_A

    b_lat1 = atan((1 - flattening) * tan(radians(lat1)))
    b_lat2 = atan((1 - flattening) * tan(radians(lat2)))

    # Hitung sudut pusat antara dua titik
    # menggunakan haversine theta. sigma = haversine_distance / radius khatulistiwa
    sigma = haversine(lat1, lon1, lat2, lon2) / EQUATORIAL_RADIUS

    P_value = (b_lat1 + b_lat2) / 2
    Q_value = (b_lat2 - b_lat1) / 2

    X_numerator = (sin(P_value) ** 2) * (cos(Q_value) ** 2)
    X_demonimator = cos(sigma / 2) ** 2
    X_value = (sigma - sin(sigma)) * (X_numerator / X_demonimator)

    Y_numerator = (cos(P_value) ** 2) * (sin(Q_value) ** 2)
    Y_denominator = sin(sigma / 2) ** 2
    Y_value = (sigma + sin(sigma)) * (Y_numerator / Y_denominator)

    return EQUATORIAL_RADIUS * (sigma - ((flattening / 2) * (X_value + Y_value)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
