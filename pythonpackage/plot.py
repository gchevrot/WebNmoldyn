import numpy as np
import matplotlib.pyplot as plt

__version__ = "0.1.0"

def plot_msd(*data, percentage=1, legend=None, fit=None):
    """
    Plot the mean square displacement

    :param data: time series
    :type data: np.ndarray
    :param percentage: percentage of the data that will be plotted,
                       value between 0 and 1.
    :type percentage: float
    :param legend: data legend
    :type legend: list of string
    :param fit: fitting coefficients
    :type fit: list of 2 floats
    """
    fig, ax = plt.subplots(figsize=(10,7))

    # plot data
    if len(data[0].shape) == 1:
        for msd in data:
            msd = msd[:int(len(msd)*percentage)]
            ax.plot(np.arange(len(msd)), msd)
            ax.set_xlabel('t', size=16)
            ax.set_title('MSD', size=16)
    if len(data[0].shape) == 2:
        for msd in data:
            ax.plot(msd[0, :int(len(msd[0])*percentage)],
                    msd[1, :int(len(msd[1])*percentage)])
            ax.set_xlabel('time [ps]', size=16)
            ax.set_ylabel('MSD [nm]', size=16)
            ax.set_xlim([0, msd[0, int(len(msd[0])*percentage)-1]])
            ax.set_ylim([0, msd[1, int(len(msd[1])*percentage)-1]])
        if fit:
            ax_sub = fig.add_axes([0.20, 0.65, 0.2, 0.2],
                         xlim=(0, msd[0, int(len(msd[0])*percentage)-1]*0.1),
                         ylim=(0, msd[1, int(len(msd[1])*percentage)-1]*0.15))
            # Remove spines and ticks
            ax_sub.spines['right'].set_color('none')
            ax_sub.spines['top'].set_color('none');
            for msd in data:
                ax_sub.plot(msd[0, :int(len(msd[0])*percentage)],
                            msd[1, :int(len(msd[1])*percentage)])
            # Adding text
            ax.text(x = 5, y = 0.08, s = "Fit: 6 D t + a",
                    fontsize = 18, color='#FF8000', alpha = 1)
            ax.text(x = 5.6, y = 0.06, s = f"D = {fit[0]/6:.4f}",
                    fontsize = 16, color='#FF8000', alpha = 1)
            ax.text(x = 5.6, y = 0.04, s = f"a = {fit[1]:.4f}",
                    fontsize = 16, color='#FF8000', alpha = 1)


    # labels
    ax.tick_params(labelsize=16)

    # Legend
    if legend:
        ax.legend(legend,
                  loc='best',
                  frameon=True,
                  shadow=True,
                  facecolor='#FFFFFF',
                  framealpha=0.9,
                  fontsize=14)

    # Remove spines and ticks
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none');


def plot_coordinates(coord_pbc, coord_nopbc):
    """
    Plot coord_pbc and coord_nopbc

    :param coord_pbc: coordinates in one dimension (x, y or z along time) of
                      one atom with periodic boundary conditions
    :type coord_pbc: np.ndarray
    :param coord_nopbc: coordinates in one dimension (x, y or z along time) of
                        one atom without the periodic boundary conditions
    :type coord_nopbc: np.ndarray
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
