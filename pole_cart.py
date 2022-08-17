from math import cos, sin


class PoleCart():
    def __init__(self, init_pos=None, init_angle=None):
        print("Hello World!")
        self.mass_cart = 10  # kg
        self.mass_pole = 10  # kg
        self.damping_cart = 0  # Ns/m
        self.damping_pole = 0  # Ns/m
        self.length_pole = 0.6  # m
        self.inertia_pole = 0.05  # m^2
        self.dt = 0.00001
        self.fps = 30
        self.timespan = self.create_time_span(0, 30, self.dt)
        self.ic = [0, 0, 0, 0.15, 0, 0]

    def odes(self, p, dp, ddp, a, da, dda):
        m_p = self.mass_pole
        m_c = self.mass_cart
        b_c = self.damping_cart
        b_p = self.damping_pole
        l_p = self.length_pole
        i_p = self.inertia_pole
        F_m = 0
        g = 9.81
        ddp = (F_m - b_c * dp + m_p * l_p * dda * cos(a) - m_p * l_p * da ** 2 * sin(a)) / (m_c + m_p)
        dda = (m_p * l_p * g * sin(a) + m_p * l_p * ddp * cos(a)) / (i_p + m_p * l_p ** 2)
        dp = dp + ddp * self.dt
        da = da + dda * self.dt
        p = p + dp * self.dt
        a = a + da * self.dt
        return [p, dp, ddp, a, da, dda]

    def ode_euler_simulation(self):
        x = [self.ic[0]]
        x_dot = [self.ic[1]]
        x_ddot = [self.ic[2]]
        theta = [self.ic[3]]
        theta_dot = [self.ic[4]]
        theta_ddot = [self.ic[5]]
        time = []
        for i in range(len(self.timespan) - 1):
            t = i * self.dt
            time.append(t)
            states = self.odes(x[i], x_dot[i], x_ddot[i],
                               theta[i], theta_dot[i], theta_ddot[i])
            x.append(states[0])
            x_dot.append(states[1])
            x_ddot.append(states[2])
            theta.append(states[3])
            theta_dot.append(states[4])
            theta_ddot.append(states[5])
        time.append(self.dt * len(self.timespan))
        x, x_dot, x_ddot, theta, theta_dot, theta_ddot, time = self.compress(x, x_dot, x_ddot,
                                                                             theta, theta_dot, theta_ddot, time)
        return x, x_dot, x_ddot, theta, theta_dot, theta_ddot, time

    def compress(self, x, dx, ddx, t, dt, ddt, time):
        x_new = [x[0]]
        dx_new = [dx[0]]
        ddx_new = [ddx[0]]
        t_new = [t[0]]
        dt_new = [dt[0]]
        ddt_new = [ddt[0]]
        time_new = [time[0]]
        compress_value = 1/self.fps
        counter = 0
        for i in time:
            if i > compress_value:
                x_new.append(x[counter])
                dx_new.append(dx[counter])
                ddx_new.append(ddx[counter])
                t_new.append(t[counter])
                dt_new.append(dt[counter])
                ddt_new.append(ddt[counter])
                time_new.append(time[counter])
                compress_value += 1/self.fps
            counter += 1

        return x_new, dx_new, ddx_new, t_new, dt_new, ddt_new, time_new

    @staticmethod
    def create_time_span(t_start, t_end, step_size):
        time_span = []
        time = t_start
        while time <= t_end:
            time_span.append(time)
            time += step_size
        time_span.append(time)
        return time_span
