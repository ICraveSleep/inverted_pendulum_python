import numpy as np

from pole_cart import PoleCart
from plotter import Plotter
from animaton import pole_cart_animate

pole_cart = PoleCart()
plotter = Plotter()
x, dx, ddx, t, dt, ddt, time = pole_cart.ode_euler_simulation()
print(len(x), len(t), len(time))

velocity = np.array(dx)
position = np.array(x)
angle = np.array(t)

plotter.plot_states(x, dx, ddx, t, dt, ddt, time)
pole_cart_animate(angle, position, time)
