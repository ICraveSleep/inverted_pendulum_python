# Plotting the results
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from pole_cart import PoleCart

pole_cart = PoleCart()
x, dx, ddx, t, dt, ddt, time = pole_cart.ode_euler_simulation()
print(len(x), len(t), len(time))
fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(time, x)
axs[0, 0].set_title("x")
axs[1, 0].plot(time, dx)
axs[1, 0].set_title("xd")
axs[2, 0].plot(time, ddx)
axs[2, 0].set_title("xdd")
axs[0, 1].plot(time, t)
axs[0, 1].set_title("theta")
axs[1, 1].plot(time, dt)
axs[1, 1].set_title("theta d")
axs[2, 1].plot(time, ddt)
axs[2, 1].set_title("theta dd")
fig.tight_layout()

plt.show()

velocity = np.array(dx)
position = np.array(x)
angle = np.array(t)


plt.rcParams['animation.html'] = 'html5'
x1 = position
y1 = np.zeros(len(time))

# suppose that l = 1
l = 0.6
x2 = 1 * np.sin(angle) + x1
x2b = 1.05 * np.sin(angle) + x1
y2 = 1 * np.cos(angle) - y1
y2b = 1.05 * np.cos(angle) - y1

fig = plt.figure(figsize=(12.8, 6.4))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2.4, 2.4), ylim=(-1.2, 1.2))
ax.set_xlabel('position')
ax.get_yaxis().set_visible(False)

floor, = ax.plot([-5, 5], [-0.2, -0.2], 'k-', lw=4)
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
    time_text.set_text('')
    return rod, cart, pendulum, time_text


def animate(i):
    cart.set_data([x1[i]], [y1[i] - 0.05])
    pendulum.set_data([x2b[i]], [y2b[i]])
    rod.set_data([x1[i], x2[i]], [y1[i]+0.01, y2[i]])
    time_text.set_text(time_template % time[i])
    return rod, cart, pendulum, time_text


ani_a = animation.FuncAnimation(fig, animate,
                                np.arange(1, len(time)),
                                interval=40, blit=False, init_func=init)

# requires ffmpeg to save mp4 file
#  available from https://ffmpeg.zeranoe.com/builds/
#  add ffmpeg.exe to path such as C:\ffmpeg\bin\ in
#  environment variables

# ani_a.save('Pendulum_Control.mp4',fps=30)

plt.show()
