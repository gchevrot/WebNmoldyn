import platform
import multiprocessing as mp
import numpy as np
import pandas as pd
import matplotlib as mpl


def sysinfo(numpy = True, pandas= True, matplotlib=True):
    print(f'Python version: {platform.python_version()}')
    if numpy:
        print(f'NumPy version: {np.__version__}')
    if pandas:
        print(f'pandas version: {pd.__version__}')
    if matplotlib:
        print(f'matplotlib version: {mpl.__version__}')

    print('\nCompiler: {platform.python_compiler}')

    print(f'\nSystem: {platform.system()}')
    print(f'Release: {platform.release()}')
    print(f'Machine: {platform.machine()}')
    print(f'Architecture: {platform.architecture()[0]}')
    print(f'Processor: {platform.processor()}')
    print(f'CPU count: {mp.cpu_count()}')
