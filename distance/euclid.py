import numpy as np


def distance(pos1: np.ndarray, pos2: np.ndarray)->float:
    difference = pos1-pos2
    difference_pow = np.square(difference)
    distance_base = np.add.reduce(difference_pow)
    return np.sqrt(distance_base)

