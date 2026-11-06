import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    x_array = np.asarray(x,dtype=float)
    y_array = np.asarray(y,dtype=float)
    L1_distance = np.abs(x_array-y_array).sum()
    return L1_distance