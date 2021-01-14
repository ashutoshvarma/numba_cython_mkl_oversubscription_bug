from IPython import get_ipython
ipython = get_ipython()

import sys
import numpy as np


A = np.random.random((10**3, 10**3))
B = np.random.random((10**3, 10**3))

if "cython" in sys.argv:
    print("only cython_mkl")
    from cython_mkl import cython_mkl
    print("cython : %s" % ipython.magic("timeit -o -q cython_mkl(A, B)").best)
elif "cython-first" in sys.argv:
    print("cython then numba")
    from cython_mkl import cython_mkl

    from numba_mkl import numba_mkl
    print("cython : %s" % ipython.magic("timeit -o -q cython_mkl(A, B)").best)
    print("numba : %s" % ipython.magic("timeit -o -q numba_mkl(A, B)").best)
else:
    print("numba then cython")
    from cython_mkl import cython_mkl

    from numba_mkl import numba_mkl
    print("numba : %s" % ipython.magic("timeit -o -q numba_mkl(A, B)").best)
    print("cython : %s" % ipython.magic("timeit -o -q cython_mkl(A, B)").best)
