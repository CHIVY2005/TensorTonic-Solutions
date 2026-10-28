import math
import numpy as np
def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    arr = []
    for i in range(len(x)):
        if x[i] > 0:
            res = x[i]
        else:
            res = alpha * (math.exp(x[i]) -1)

        arr.append(res)
    return arr
    pass