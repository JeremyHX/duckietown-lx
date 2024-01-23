from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # DONE: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    res[250:, :340] = 1
    #res[220:, 360:] = -1
    for i in range(200, 480):
        for j in range(360, min(260+i, 640)):
            res[i, j] = -1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # DONE: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    #res[220:, :320] = -1
    for i in range(200, 480):
        for j in range(max(400-i, 0), 320):
            res[i, j] = -1

    res[250:, 341:] = 1
    # ---
    return res
