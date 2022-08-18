import numpy as np
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
import sys
import time
dt = 0.01
t = np.arange(0, 180+dt, dt)
g = 9.81
l = 2.5
m1 = 50
m2 = 20
x = np.zeros(len(t))
xd = np.zeros(len(t))
xdd = np.zeros(len(t))

p = np.zeros(len(t))
pd = np.zeros(len(t))
pdd = np.zeros(len(t))


for i in range(len(t)):
    if i == 0:
        p[i] = np.pi/2  # initial condition
        pd[i] = 0  # initial condition

        x[i] = 0
        xd[i] = 0

        # pdd[i] = (g*np.sin(p[i])-xdd[i]*np.cos(p[i]))/l
        pdd[i] = 0
        # xdd[i] = (m2*l*pdd[i]*np.cos(p[i])-m2*l*pd[i]**2*np.sin(p[i]))
        xdd[i] = 0
    else:
        # pdd[i] = (-g * np.sin(p[i-1]) + xdd[i-1] * np.cos(p[i-1])) / l
        pdd[i] = (-g * np.sin(p[i-1])) / l
        xdd[i] = (-m2 * l * pdd[i-1] * np.cos(p[i-1]) + m2 * l * pd[i-1] ** 2 * np.sin(p[i-1]))/(m1+m2)

        pd[i] = pd[i-1] + dt*pdd[i]
        xd[i] = xd[i-1] + dt*xdd[i]
        p[i] = p[i-1] + dt*pd[i]
        x[i] = x[i-1] + dt*xd[i]


figure, axis = plt.subplots(2)
axis[0].plot(t, x)
axis[1].plot(t, p)
plt.show()

w, h = 1100, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)

screen = pygame.display.set_mode((w, h))
screen.fill(WHITE)
pygame.display.update()
clock = pygame.time.Clock()


def update(a1_sim, a2_sim):
    scale = 100
    x1 = scale * a1_sim + 400
    y1 = 300

    x2 = x1 + l * scale * np.sin(a2_sim) + 150/2
    y2 = y1 + l * scale * np.cos(a2_sim) + 100/2
    return (x1, y1), (x2, y2)


def render(point_sim1, point_sim2, m1, m2):
    x1 = point_sim1[0]
    y1 = point_sim1[1]

    x2 = point_sim2[0]
    y2 = point_sim2[1]

    scale = 2.5

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, (0, 300 + 100+20), (1100, 300 + 100+20), 4)
    pygame.draw.rect(screen, BLUE, (x1, y1, 150, 100), 0)
    pygame.draw.circle(screen, (128, 128, 128), (int(x1 + 25), int(y1 + 100)), 20)
    pygame.draw.circle(screen, (0, 0, 0), (int(x1 + 25), int(y1 + 100)), 7)
    pygame.draw.circle(screen, (128, 128, 128), (int(x1 + 125), int(y1 + 100)), 20)
    pygame.draw.circle(screen, (0, 0, 0), (int(x1 + 125), int(y1 + 100)), 7)
    pygame.draw.line(screen, BLACK, (x1+150/2, y1+100/2), (x2, y2), 5)
    pygame.draw.circle(screen, RED, (int(x2), int(y2)), int(m2*scale))
    pygame.draw.circle(screen, (128, 128, 128), (int(x1+150/2), int(y1+100/2)), 10)


    return


a1 = x[0]
a2 = p[0]

tStart = time.time()
tAccumulated = 0
for i in range(len(t)):
    tStep_start = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Update step
    point1, point2 = update(a1, a2)

    # Render step
    render(point1, point2, m1=m1, m2=m2)

    a1 = x[i]
    a2 = p[i]

    # clock.tick(60)
    pygame.display.update()
    tStep = time.time() - tStep_start
    if tStep < dt:
        time.sleep(dt-tStep)
    else:
        tAccumulated += tStep-dt
        print("Accumulated over pass time:", tAccumulated, "[s]")
tEnd = time.time()

print("Simulation time", (tEnd-tStart))