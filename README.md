# Inverted Pendulum

<p align="center">
    <img src="gifs/animation.gif"/>
</p>

Swing-up using energy pumping method

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

## State space model
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

Adding state feedback where the gain matrix is calulated
using LQR

<p align="center">
    <img src="gifs/inverted_pendulum.gif"/>
</p>