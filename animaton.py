import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def pole_cart_animate(angle, position, time):
    plt.rcParams['animation.html'] = 'html5'

    pendulum_length = 1
    x1 = position
    y1 = np.zeros(len(time))

    x2 = pendulum_length * np.sin(angle) + x1
    x2b = pendulum_length * 1.05 * np.sin(angle) + x1
    y2 = pendulum_length * np.cos(angle) - y1
    y2b = pendulum_length * 1.05 * np.cos(angle) - y1

    fig = plt.figure(figsize=(12.8, 6.4))
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2.4, 2.4), ylim=(-1.2, 1.2))
    ax.set_xlabel('position')
    ax.get_yaxis().set_visible(False)

    floor, = ax.plot([-5, 5], [-0.2, -0.2], 'k-', lw=4)
    goal, = ax.plot([], [], 'b:')
    cart, = ax.plot([], [], linestyle='None', marker='s', markersize=40, markeredgecolor='k', color='orange',
                    markeredgewidth=2)
    pendulum, = ax.plot([], [], linestyle='None', marker='o',
                        markersize=20, markeredgecolor='k',
                        color='orange', markeredgewidth=2)
    rod, = ax.plot([], [], 'o-', color='k', lw=4,
                   markersize=6, markeredgecolor='k',
                   markerfacecolor='k')
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    # start_text = ax.text(-1.06, -0.3, 'start', ha='right')
    # end_text = ax.text(0.06, -0.3, 'objective', ha='left')

    def init():
        cart.set_data([], [])
        pendulum.set_data([], [])
        rod.set_data([], [])
        goal.set_data([], [])
        time_text.set_text('')
        return rod, cart, pendulum, goal, time_text

    def animate(i):
        cart.set_data([x1[i]], [y1[i] - 0.05])
        pendulum.set_data([x2b[i]], [y2b[i]])
        rod.set_data([x1[i], x2[i]], [y1[i] + 0.01, y2[i]])
        time_text.set_text(time_template % time[i])
        if time[i] <= 13.5:
            goal.set_data([-1, -1], [-4, 4])

        else:
            goal.set_data([0, 0], [-4, 4])
        return goal, rod, cart, pendulum, time_text

    anim = animation.FuncAnimation(fig, animate, len(time), interval=40, blit=False, init_func=init)


    #anim.save('gifs/animation.gif', writer='imagemagick', fps=30)
    #anim.save('gifs/energy_swingup.gif', writer='imagemagick', fps=30)
    #anim.save('gifs/inverted_pendulum.gif', writer='imagemagick', fps=30)

    plt.show()
