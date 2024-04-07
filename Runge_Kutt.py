import numpy as np
from Functions import dif_func

def R_K (time_limits, points0, h):
    time = np.arange(time_limits[0], time_limits[1], h)
    points = np.zeros((len(time), len(points0)))
    points[0] = points0
    for i in range(1, len(time)):
        t = time[i]
        k1 = h * dif_func(t, points[i - 1])
        k2 = h * dif_func(t + h / 2, points[i - 1] + 2 * k1 / 3)
        k3 = h * dif_func(t + h, points[i - 1] - k1 / 3 + k2)
        points[i] = points[i - 1] + (k1 + 2 * k2 + k3) / 4
    return points