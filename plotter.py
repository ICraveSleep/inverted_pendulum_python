import matplotlib.pyplot as plt


class Plotter:

    def __init__(self):
        pass

    @staticmethod
    def plot_states(pos, d_pos, dd_pos, angle, d_angle, dd_angle, time):
        fig, axs = plt.subplots(3, 2)
        axs[0, 0].plot(time, pos)
        axs[0, 0].set_title("x")
        axs[1, 0].plot(time, d_pos)
        axs[1, 0].set_title("xd")
        axs[2, 0].plot(time, dd_pos)
        axs[2, 0].set_title("xdd")
        axs[0, 1].plot(time, angle)
        axs[0, 1].set_title("theta")
        axs[1, 1].plot(time, d_angle)
        axs[1, 1].set_title("theta d")
        axs[2, 1].plot(time, dd_angle)
        axs[2, 1].set_title("theta dd")
        fig.tight_layout()

    def show_plot(self):
        plt.show()
