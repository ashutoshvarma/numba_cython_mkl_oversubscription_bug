## Setup Environment
- ## Install deps
    ```
    conda install numpy numba cython ipython
    ```

- ## Build cython extension
    ```
    cythonize -i *pyx
    ```

## Run test.py
- ### numba first then cython
    ```
    ./check_thread ipython test.py
    ```
- ### cython first then numba
    ```
    ./check_thread ipython test.py cython-first
    ```
