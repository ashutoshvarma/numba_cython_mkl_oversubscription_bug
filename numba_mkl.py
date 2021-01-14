import numpy as np
from numba import njit, prange


@njit(parallel=True)
def numba_mkl(A, B):
    for i in prange(128):
        np.dot(A, B)
