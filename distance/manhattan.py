import numpy as np

def distance(pos1: np.ndarray, pos2: np.ndarray)->float:
    cell_distance = np.abs(pos1-pos2)
    return np.add.reduce(cell_distance)

