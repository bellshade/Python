# https://en.wikipedia.org/wiki/Pendulum
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def full_pendulum(g, L, theta, theta_velocity, time_step):
    """
    fungsi untuk menghitung persamaan pendulum.
    """
    theta_acceleration = -(g / L) * np.sin(theta)
    theta_velocity += time_step * theta_acceleration
    theta += time_step * theta_velocity
    return theta, theta_velocity


g = 9.8  # konstanta gravitasi
L = 1.0  # panjang tali


theta = [np.radians(90)]
theta_velocity = 0
time_step = 20 / 300


time_stap = np.linspace(0, 20, 300)
"""
Looping untuk memasukkan setiap angka.
"""
for t in time_stap:
    theta_new, theta_velocity = full_pendulum(g, L, theta[-1],
                                              theta_velocity, time_step)
    theta.append(theta_new)

# persamaan proyeksi panjang tali
x = L * np.sin(theta)
y = -L * np.cos(theta)

fig, axis = plt.subplots()

# batas sumbu x dan y
axis.set_xlim(-L - 0.2 , L + 0.2)
axis.set_ylim(-L - 0.2 , L)

plt.grid()

# benda yang akan bergerak
rod_line, = axis.plot([], [], lw=2)
mass_point, = axis.plot([], [], marker='o', markersize=10)
trace, = axis.plot([], [], '-', lw=1, alpha=0.6)


def animate(frame):
    """
    Fungsi ini berguna untuk mengambil setiap hasil hitungan
    dan menjadikan setiap hitungan frame.
    """
    rod_line.set_data([0, x[frame]], [0, y[frame]])
    mass_point.set_data([x[frame]], [y[frame]])
    trace.set_data(x[:frame], y[:frame])

    return rod_line, mass_point, trace


animation = FuncAnimation(
    fig=fig,
    func=animate,
    frames=len(time_stap),
    interval=25,
    blit=True
)

plt.show()
