import math
import numpy as np

def Function(t) -> float:
     return  math.exp(t)
def dif_func(t: float, point_coordinates: tuple) -> np.ndarray:
    return np.array([Function(t) * point_coordinates[0], Function(t) * point_coordinates[1]])
