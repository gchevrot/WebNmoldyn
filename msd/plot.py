import numpy as np
import matplotlib.pyplot as plt

def plot_msd(data, percentage=0.3):
    """
    Paratmeters
    -----------
    data: 1D array
    percentage: percentage of plot data
    """
    fig, ax = plt.subplots(figsize=(7,7))

    for msd in data:
        msd = msd[:int(len(msd)*percentage)]
        ax.plot(np.arange(len(msd)), msd)
    ax.set_xlabel('t')
    ax.set_title('MSD');
