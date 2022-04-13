"""
Dalam fisika dan astronomi,
simulasi gravitasi N-body adalah simulasi a
sistem dinamis partikel di bawah pengaruh gravitasi.
Sistem terdiri dari sejumlah benda, yang masing-masing
memberikan gaya gravitasi pada semua benda
tubuh lainnya. Gaya-gaya ini dihitung menggunakan hukum universal Newton
gravitasi. Metode Euler digunakan pada setiap langkah
waktu untuk menghitung perubahan
kecepatan dan posisi yang ditimbulkan oleh gaya-gaya ini.
Pelunakan digunakan untuk mencegah
divergensi numerik ketika sebuah partikel datang terlalu dekat
dengan yang lain (dan gaya
menuju tak terhingga).

informasi lebih lanjut tetang N-body
https://en.wikipedia.org/wiki/N-body_simulation
"""

from __future__ import annotations

import random

from matplotlib import animation
from matplotlib import pyplot as plt


class Body:
    def __init__(
        self,
        position_x: float,
        position_y: float,
        velocity_x: float,
        velocity_y: float,
        mass: float = 1.0,
        size: float = 1.0,
        color: str = "blue",
    ) -> None:
        """
        Parameter "size" & "color" tidak relevan untuk simulasi itu sendiri,
        mereka hanya digunakan untuk plotting.
        """
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.mass = mass
        self.size = size
        self.color = color

    @property
    def position(self) -> tuple[float, float]:
        return self.position_x, self.position_y

    @property
    def velocity(self) -> tuple[float, float]:
        return self.velocity_x, self.velocity_y

    def update_velocity(
        self, force_x: float, force_y: float, delta_time: float
    ) -> None:
        """
        algoritma euler untuk velocity
        >>> test_body_1 = Body(0.,0.,0.,0.)
        >>> test_body_1.update_velocity(1.,0.,1.)
        >>> test_body_1.velocity
        (1.0, 0.0)

        >>> test_body_1.update_velocity(1.,0.,1.)
        >>> test_body_1.velocity
        (2.0, 0.0)
        """
        self.velocity_x += force_x * delta_time
        self.velocity_y += force_y * delta_time

    def update_position(self, delta_time: float) -> None:
        """
        algoritma euler untuk update posisi

        >>> test_body1 = Body(0.,0.,1.,0.)
        >>> test_body1.update_position(1.0)
        >>> test_body1.position
        (1.0, 0.0)

        >>> test_body2 = Body(10.,10.,0.,-2)
        >>> test_body2.update_position(1.)
        >>> test_body2.position
        (10.0, 8.0)
        """
        self.position_x += self.velocity_x * delta_time
        self.position_y += self.velocity_y * delta_time


class BodySystem:
    """
    Kelas ini digunakan untuk menahan benda, konstanta gravitasi, waktu
    faktor dan faktor pelunakan.
    Faktor waktu digunakan untuk mengontrol kecepatan
    dari simulasi. Faktor pelunakan digunakan untuk pelunakan, numerik
    trik untuk simulasi N-tubuh untuk mencegah divergensi
    numerik ketika dua benda
    terlalu dekat satu sama lain.
    """

    def __init__(
        self,
        bodies: list[Body],
        gravitation_constant: float = 1.0,
        time_factor: float = 1.0,
        softening_factor: float = 0.0,
    ) -> None:
        self.bodies = bodies
        self.gravitation_constant = gravitation_constant
        self.time_factor = time_factor
        self.softening_factor = softening_factor

    def __len__(self) -> int:
        return len(self.bodies)

    def update_system(self, delta_time: float) -> None:
        """
        Untuk setiap benda, looping semua benda lain untuk menghitung total
        memaksa mereka mengerahkannya.
        Gunakan forcing untuk memperbarui kecepatan tubuh.
        """
        for body1 in self.bodies:
            force_x = 0.0
            force_y = 0.0
            for body2 in self.bodies:
                if body1 != body2:
                    dif_x = body2.position_x - body1.position_x
                    dif_y = body2.position_y - body1.position_y

                    distance = (dif_x**2 + dif_y**2 + self.softening_factor) ** (
                        1 / 2
                    )
                    force_x += (
                        self.gravitation_constant * body2.mass * dif_x / distance**3
                    )
                    force_y += (
                        self.gravitation_constant * body2.mass * dif_y / distance**3
                    )

            body1.update_velocity(force_x, force_y, delta_time * self.time_factor)

        for body in self.bodies:
            body.update_position(delta_time * self.time_factor)


def update_step(
    body_system: BodySystem, delta_time: float, patches: list[plt.Circle]
) -> None:
    """
    Memperbarui sistem tubuh dan menerapkan perubahan
    ke daftar yang digunakan untuk plotting
    """
    body_system.update_system(delta_time)

    for patch, body in zip(patches, body_system.bodies):
        patch.center = (body.position_x, body.position_y)


def plot(
    title: str,
    body_system: BodySystem,
    x_start: float = -1,
    x_end: float = 1,
    y_start: float = -1,
    y_end: float = 1,
) -> None:
    """
    Fungsi utilitas untuk memplot bagaimana sistem
    tubuh yang diberikan berkembang dari waktu ke waktu.
    Tidak ada doctest yang disediakan karena fungsi
    ini tidak memiliki nilai balik.
    """

    INTERVAL = 20
    DELTA_TIME = INTERVAL / 1000

    fig = plt.figure()
    fig.canvas.set_window_title(title)
    ax = plt.axes(xlim=(x_start, x_end), ylim=(y_start, y_end))
    plt.gca().set_aspect("equal")

    patches = [
        plt.Circle((body.position_x, body.position_y), body.size, fc=body.color)
        for body in body_system.bodies
    ]

    for patch in patches:
        ax.add_patch(patch)

    # Fungsi dipanggil pada setiap langkah animasi
    def update(frame: int) -> list[plt.Circle]:
        update_step(body_system, DELTA_TIME, patches)
        return patches

    anim = animation.FuncAnimation(  # noqa: F841
        fig, update, interval=INTERVAL, blit=True
    )

    plt.show()


def example_1() -> BodySystem:
    """
    http://www.artcompsci.org/vol_1/v1_web/node56.html
    >>> body_system = example_1()
    >>> len(body_system)
    3
    """

    position_x = 0.9700436
    position_y = -0.24308753
    velocity_x = 0.466203685
    velocity_y = 0.43236573

    bodies1 = [
        Body(position_x, position_y, velocity_x, velocity_y, size=0.2, color="red"),
        Body(-position_x, -position_y, velocity_x, velocity_y, size=0.2, color="green"),
        Body(0, 0, -2 * velocity_x, -2 * velocity_y, size=0.2, color="blue"),
    ]
    return BodySystem(bodies1, time_factor=3)


def example_2() -> BodySystem:
    """
    Orbit bulan mengelilingi bumi
    Contoh ini dapat dilihat sebagai ujian implementasi: diberikan hak
    kondisi awal, bulan harus mengorbit bumi seperti yang sebenarnya.

    https://en.wikipedia.org/wiki/Earth
    https://en.wikipedia.org/wiki/Moon
    """

    moon_mass = 7.3476e22
    earth_mass = 5.972e24
    velocity_dif = 1022
    earth_moon_distance = 384399000
    gravitation_constant = 6.674e-11

    # Perhitungan kecepatan masing-masing sehingga impuls total adalah nol,
    # yaitu dua tubuh bersama-sama tidak bergerak
    moon_velocity = earth_mass * velocity_dif / (earth_mass + moon_mass)
    earth_velocity = moon_velocity - velocity_dif

    moon = Body(-earth_moon_distance, 0, 0, moon_velocity, moon_mass, 10000000, "grey")
    earth = Body(0, 0, 0, earth_velocity, earth_mass, 50000000, "blue")
    return BodySystem([earth, moon], gravitation_constant, time_factor=1000000)


def example_3() -> BodySystem:
    """
    Sistem acak dengan banyak tubuh.
    Tidak ada doctest yang disediakan karena
    fungsi ini tidak memiliki nilai balik.
    """

    bodies = []
    for i in range(10):
        velocity_x = random.uniform(-0.5, 0.5)
        velocity_y = random.uniform(-0.5, 0.5)

        # Benda diciptakan berpasangan dengan kecepatan yang
        # berlawanan sehingga
        # impuls total tetap nol
        bodies.append(
            Body(
                random.uniform(-0.5, 0.5),
                random.uniform(-0.5, 0.5),
                velocity_x,
                velocity_y,
                size=0.05,
            )
        )
        bodies.append(
            Body(
                random.uniform(-0.5, 0.5),
                random.uniform(-0.5, 0.5),
                -velocity_x,
                -velocity_y,
                size=0.05,
            )
        )
    return BodySystem(bodies, 0.01, 10, 0.1)


if __name__ == "__main__":
    import doctest

    plot("solusi figure-8", example_1(), -2, 2, -2, 2)
    plot(
        "orbit bulan ke bumi",
        example_2(),
        -430000000,
        430000000,
        -430000000,
        430000000,
    )
    doctest.testmod()
