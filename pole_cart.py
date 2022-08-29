from math import cos, sin


class PoleCart():
    def __init__(self, init_pos=None, init_angle=None):
        print("Hello World!")
        self.mass_cart = 10  # kg
        self.mass_pole = 10  # kg
        self.damping_cart = 0.1  # Ns/m
        self.damping_pole = 1  # Ns/m
        self.length_pole = 0.6  # m
        self.inertia_pole = 0.05  # m^2
        self.dt = 0.00001  # 0.00001
        self.fps = 30
        self.timespan = self.create_time_span(0, 20, self.dt)
        self.ic = [0, 0, 0, 3.14, 0, 0]
        self.swing_up = True

    def odes(self, p, dp, ddp, a, da, dda):
        m_p = self.mass_pole
        m_c = self.mass_cart
        b_c = self.damping_cart
        b_p = self.damping_pole
        l_p = self.length_pole
        i_p = self.inertia_pole
        g = 9.81

        E = g*l_p*cos(a)*m_p
        E_t = g*l_p*m_p

        if a < 0.0 or a > 3.1415*2:
            self.swing_up = False

        if self.swing_up:
            if a > 1.571 or a < 4.712:
                f = (E - E_t)*da*cos(a)*0.2
            else:
                f = 0
        else:
            f = 0
        F_m = f
        ddp = (F_m - b_c * dp + m_p * l_p * dda * cos(a) - m_p * l_p * da ** 2 * sin(a)) / (m_c + m_p)
        #ddp = F_m/(m_p + m_c)
        dda = (-b_p * da + m_p * l_p * g * sin(a) - m_p * l_p * ddp * cos(a)) / (i_p + m_p * l_p ** 2)
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

    def ode_RK4_simulation(self):
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
            states = self.RK4_step([x[i], x_dot[i], x_ddot[i], theta[i], theta_dot[i], theta_ddot[i]], t)
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

    def RK4_step(self, yk, tk):
        x = yk[0]
        dx = yk[1]
        ddx = yk[2]
        t = yk[3]
        dt = yk[4]
        ddt = yk[5]

        f1 = self.RK4_odes(x, dx, ddx, t, dt, ddt)
        ddx = f1[0]
        ddt = f1[1]
        prem = self.sum_list([[dx, dt], [(self.dt / 2) * a for a in f1]])
        f2 = self.RK4_odes(x, prem[0], ddx, t, prem[1], ddt)
        prem = self.sum_list([[dx, dt], [(self.dt / 2) * a for a in f2]])
        f3 = self.RK4_odes(x, prem[0], ddx, t, prem[1], ddt)
        prem = self.sum_list([[dx, dt], [self.dt * a for a in f3]])
        f4 = self.RK4_odes(x, prem[0], ddx, t, prem[1], ddt)
        f1 = [a * self.dt / 6 for a in f1]
        f2 = [a * self.dt / 3 for a in f2]
        f3 = [a * self.dt / 3 for a in f3]
        f4 = [a * self.dt / 6 for a in f4]
        prem = self.sum_list([[yk[1], yk[4]], f1, f2, f3, f4])
        dx = prem[0]
        dt = prem[1]

        x = x + self.dt * dx
        t = t + self.dt * dt

        #f1 = [dx, dt]
        #f2 = self.sum_list([[x, t], [(self.dt / 2) * a for a in f1]])
        #f3 = self.sum_list([[x, t], [(self.dt / 2) * a for a in f2]])
        #f4 = self.sum_list([[x, t], [self.dt * a for a in f3]])
        #f1 = [a * self.dt / 6 for a in f1]
        #f2 = [a * self.dt / 3 for a in f2]
        #f3 = [a * self.dt / 3 for a in f3]
        #f4 = [a * self.dt / 6 for a in f4]
        #prem = self.sum_list([[yk[0], yk[3]], f1, f2, f3, f4])
        #x = prem[0]
        #t = prem[1]
        return x, dx, ddx, t, dt, ddt

    def RK4_odes(self, p, dp, ddp, a, da, dda):
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
        return [ddp, dda]

    def compress(self, x, dx, ddx, t, dt, ddt, time):
        x_new = [x[0]]
        dx_new = [dx[0]]
        ddx_new = [ddx[0]]
        t_new = [t[0]]
        dt_new = [dt[0]]
        ddt_new = [ddt[0]]
        time_new = [time[0]]
        compress_value = 1 / self.fps
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
                compress_value += 1 / self.fps
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

    @staticmethod
    def sum_list(list_in):
        summed_list = len(list_in[0]) * [0]
        for a in list_in:
            for i in range(len(a)):
                summed_list[i] += a[i]
        return summed_list
