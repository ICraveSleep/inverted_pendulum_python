# Inverted Pendulum
In order to run the simulation, simply run `main.py`

In order to save animations ImageMagick is required. It can be installed from here: https://imagemagick.org/script/download.php

## Simulation of the pole cart system ##
The equations of motion that are presented below. Here the pendulum and cart viscous damping is set to zero. I.e. $b_c = b_p = 0$


Cart equation

$$
    \ddot{x}_{cx} = \frac{F_m - b_c\Dot{x} + m_pL_p\ddot{\theta} \cos (\theta) - m_pL_p\dot{\theta}^2 \sin (\theta)}{m_c + m_p}
$$

Pendulum equation

$$
    \ddot{\theta} = \frac{-b_p\dot\theta + m_pL_pg\sin(\theta) + m_pL_p\ddot{x}_{cx}\cos(\theta)}{ I_p +m_pL_p^2}
$$


<p align="center">
    <img src="gifs/animation.gif"/>
</p>

## Swing-up ##
In order to swing the pendulum up, an energy pumping method is used. It only considers the potential energy of the pendulum. 

$$
    f(t) = (E_p(t) - E_t)\dot\theta\cos(\theta)
$$

Where

$$
    E_p(t) = m_pgl_p\cos(\theta) ~~ and ~~ E_t = m_pgl_p
$$

<p align="center">
    <img src="gifs/energy_swingup.gif"/>
</p>

## State feedback ##
The linearized equations of motion, in state space representation, is presented below. The model is applied
when calculating the state feedback gain matrix.

$$
    \begin{bmatrix}
        \dot x_{cx} \\
        \ddot x_{cx}\\
        \dot \theta \\
        \ddot \theta
    \end{bmatrix}
     = 
    \begin{bmatrix}
        0 & 1 & 0 & 0 \\
        0 & \frac{-b_c(m_pL_p^2+I_p)}{(L_p^2m_c+I_p)m_p+I_pm_c} & \frac{L_p^2gm_p^2}{(L_p^2m_c+I_p)m_p+I_pm_c} & \frac{-b_pL_pm_p}{(L_p^2m_c+I_p)m_p+I_pm_c} & \\
        0 & 0 & 0 & 1 \\
        0 & \frac{-bm_pL_p}{(L_p^2m_c+I_p)m_p+I_pm_c} & \frac{m_pgL_p(m_c+m_p)}{(L_p^2m_c+I_p)m_p+I_pm_c} & \frac{-b_p(m_c+m_p)}{(L_p^2m_c+I_p)m_p+I_pm_c}
    \end{bmatrix}
    \begin{bmatrix}
        x_{cx} \\
        \dot x_{cx}\\
        \theta \\
        \dot \theta
    \end{bmatrix}
    + 
    \begin{bmatrix}
        0 \\
        \frac{m_pL_p^2+I_p}{(L_p^2m_c+I_p)m_p+I_pm_c}\\
        0 \\
        \frac{m_pL_p}{(L_p^2m_c+I_p)m_p+I_pm_c}
    \end{bmatrix}
    u(t)
$$

<p align="center">
    <img src="gifs/inverted_pendulum_correct.gif"/>
</p>