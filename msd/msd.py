import numpy as np

def compute_msd(r):
    """
    Mean square displacement

    Parameters
    ----------
    r: numpy array. dimensions: (t, 3)
       Array containing the coordinates along t
    """
    shifts = np.arange(len(r))
    msd = np.zeros(shifts.size)
    for i, shift in enumerate(shifts):
        diffs = r[:-shift if shift else None] - r[shift:]
        sqdist = np.square(diffs).sum(axis=1)
        msd[i] = sqdist.mean()
    return msd
