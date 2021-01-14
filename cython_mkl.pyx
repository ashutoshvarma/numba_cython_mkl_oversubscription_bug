#distutils: extra_compile_args=-fopenmp
#distutils: extra_link_args=-fopenmp


from cython.parallel cimport prange
import numpy as np

def cython_mkl(A, B):
    cdef Py_ssize_t i
    for i in prange(128, nogil=True):
        with gil:
            np.dot(A, B)
