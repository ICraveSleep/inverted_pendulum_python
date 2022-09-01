from numpy import matrix
import control
mass_cart = 10  # kg
mass_pole = 10  # kg
damping_cart = 0.1  # Ns/m
damping_pole = 1.17  # Ns/m
length_pole = 0.6  # m
inertia_pole = 0.05  # m^2
m_p = mass_pole
m_c = mass_cart
b_c = damping_cart
b_p = damping_pole
l_p = length_pole
i_p = inertia_pole
g = 9.81
num = (l_p ** 2 + i_p) * m_p + i_p * m_c
a_22 = (-b_c * (m_p * l_p ** 2)) / num
a_23 = (l_p ** 2 * g * m_p ** 2) / num
a_24 = (-b_p * (m_c + m_p)) / num
a_42 = (-b_c * m_p * l_p) / num
a_43 = (m_p * g * l_p * (m_c + m_p)) / num
a_44 = (-b_p * (m_c + m_p)) / num
A = matrix([
    [0, 0, 1, 0],
    [0, a_22, a_23, a_24],
    [0, 0, 0, 1],
    [0, a_42, a_43, a_44]
])
b_2 = (m_p * l_p ** 2 + i_p) / num
b_4 = m_p * l_p / num
B = matrix([
    [0],
    [b_2],
    [0],
    [b_4]
])
Q = matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 10, 0],
    [0, 0, 0, 1]
])
R = 1

K, S, E = control.lqr(A, B, Q, R)

print(K)
print(S)
print(E)
print()
X = matrix([
    [1],
    [2],
    [3],
    [4]
])

ref = matrix([
    [25],
    [12],
    [3],
    [4]
])
u_t = -K*(ref - X)

print(u_t[0,0])