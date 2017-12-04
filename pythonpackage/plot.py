import numpy as np
import matplotlib.pyplot as plt

__version__ = "0.1.0"

def plot_msd(*data, percentage=0.3):
    """
    Paratmeters
    -----------
    data: 1D array
    percentage: percentage of the data that will be plotted
    """
    fig, ax = plt.subplots(figsize=(10,7))

    # plot data
    for msd in data:
        msd = msd[:int(len(msd)*percentage)]
        ax.plot(np.arange(len(msd)), msd)

    # labels
    ax.set_xlabel('t', size=16)
    ax.set_title('MSD', size=16)
    ax.tick_params(labelsize=16)

    # Remove spines and ticks
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none');


def plot_coordinates(coord_pbc, coord_nopbc):
    """
    Plot coord_pbc and coord_nopbc

    Parameters
    -----------
    coord_pbc: coordinates in one dimension (x, y or z along time) of one atom
               with periodic boundary conditions
    coord_nopbc: coordinates in one dimension (x, y or z along time) of one atom
                 without the periodic boundary conditions
    """
    fig, ax = plt.subplots(figsize=(10,7))

    # plot data
    ax.plot(coord_pbc, label = 'with PBC')
    ax.plot(coord_nopbc, label = 'without PBC')

    # labels
    ax.set_xlabel('time step', size=16)
    ax.set_ylabel('coordinate', size=16)
    ax.tick_params(labelsize=16)

    # Legend
    ax.legend(['with PBC', 'without PBC'],
              loc='best',
              frameon=True,
              shadow=True,
              facecolor='#FFFFFF',
              framealpha=0.9,
              fontsize=14)

    # Remove spines and ticks
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none');
