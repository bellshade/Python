# https://en.wikipedia.org/wiki/Pendulum
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parameter(g=9.8, L=1.0, a=float, b=float) -> float:
    time_step = a / b
    time_stap = np.linspace(0, a, b)
    return g, L, time_step, time_stap


def full_pendulum(g, L, theta, theta_velocity, time_step):
    """
    fungsi untuk menghitung persamaan pendulum.
    """
    theta_acceleration = -(g / L) * np.sin(theta)
    theta_velocity += time_step * theta_acceleration
    theta += time_step * theta_velocity
    return theta, theta_velocity


def calculate_pendulum() -> float:
    """
    Melakukan kalkulasi pendulum
    """
    theta = [np.radians(90)]
    theta_velocity = 0

    for _ in time_stap:
        theta_new, theta_velocity = full_pendulum(
            g, L, theta[-1], theta_velocity, time_step
        )
        theta.append(theta_new)

    # persamaan proyeksi panjang tali
    x = L * np.sin(theta)
    y = -L * np.cos(theta)
    return x, y


def setup_axis(axis) -> None:
    """
    Setup sumbu x dan y.
    """
    axis.set_xlim(-L - 0.2, L + 0.2)
    axis.set_ylim(-L - 0.2, L)
    axis.grid()
    return axis


def create_plot_elements(axis) -> None:
    """
    Membuat elemen plot yang akan dianimasu.
    """
    (rod_line,) = axis.plot([], [], lw=2)
    (mass_point,) = axis.plot([], [], marker="o", markersize=10)
    (trace,) = axis.plot([], [], "-", lw=1, alpha=0.6)
    return rod_line, mass_point, trace


def animate(frame, x, y, rod_line, mass_point, trace) -> None:
    """
    Fungsi ini berguna untuk mengambil setiap hasil hitungan
    dan menjadikan setiap hitungan frame.
    """
    rod_line.set_data([0, x[frame]], [0, y[frame]])
    mass_point.set_data([x[frame]], [y[frame]])
    trace.set_data(x[:frame], y[:frame])
    return rod_line, mass_point, trace


if __name__ == "__main__":
    g, L, time_step, time_stap = parameter(a=20, b=300)
    x, y = calculate_pendulum()
    fig, axis = plt.subplots()
    axis = setup_axis(axis)
    rod_line, mass_point, trace = create_plot_elements(axis)

    def init():
        """
        Parameter awal.
        """
        rod_line.set_data([], [])
        mass_point.set_data([], [])
        trace.set_data([], [])
        return rod_line, mass_point, trace

    animation = FuncAnimation(
        fig=fig,
        func=animate,
        fargs=(x, y, rod_line, mass_point, trace),
        init_func=init,
        frames=len(time_stap),
        interval=25,
        blit=True,
    )

    print(animation)
    plt.show()
