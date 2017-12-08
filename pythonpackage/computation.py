import numpy as np

__version__ = "0.2.0"

def round_up_to_power_of_two(n):
    p = 1
    while p < n:
        p += p
    return p

def correlation(ts1, ts2=None):
    """
    Correlation function

    :param ts1: time series (scalar or vector)
    :type ts1: np.ndarray
    :param ts2: second time series (scalar or vector), if None, assume ts2=ts1
    :type ts2: np.ndarray
    :returns: the correlation function of ts1 and ts2
    :rtype: np.ndarray
    """

    n = len(ts1)
    n2 = 2*round_up_to_power_of_two(n)

    fft_ts1 = np.fft.fft(ts1, n2, axis=0)

    if ts2 is None:
        # auto-correlation
        ts2 = ts1
        fft_ts2 = fft_ts1
    else:
        # cross-correlation
        assert ts2.shape == ts1.shape
        fft_ts2 = np.fft.fft(ts2, n2, axis=0)

    product = np.conjugate(fft_ts1)*fft_ts2
    assert len(product) == n2
    fft_corr = np.fft.ifft(product, n2, axis=0)

    if len(fft_corr.shape) == 1:
        # a scalar time series
        return fft_corr.real[:n] / np.arange(n, 0, -1)
    else:
        # a vector time series - implied dot product
        return np.add.reduce(fft_corr.real[:n], axis=1) / np.arange(n, 0, -1)


def compute_msd_notoptimized(ts):
    """
    Mean square displacement (straightforward implementation - see compute_msd
    for an optimized implementation)

    :param ts: time series (scalar or vector)
    :type ts1: np.ndarray
    """
    shifts = np.arange(len(ts))
    msd = np.zeros(shifts.size)
    for i, shift in enumerate(shifts):
        diffs = ts[:-shift if shift else None] - ts[shift:]
        sqdist = np.square(diffs).sum(axis=1)
        msd[i] = sqdist.mean()
    return msd


def compute_msd(ts1, ts2=None):
    """
    Mean-square displacement
    Algorithm comes from this paper - DOI:  http://dx.doi.org/10.1051/sfn/201112010

    :param ts1: time series (scalar or vector)
    :type ts1: np.ndarray
    :param ts2: second time series (scalar or vector), if None, assume ts2=ts1
    :type ts2: np.ndarray
    :returns: the mean-square displacement of ts
    :rtype: np.ndarray
    """
    n = len(ts1)
    if ts2 is None:
        ts2 = ts1
    else:
        assert ts1.shape == ts2.shape
    dsq = ts1*ts2
    if len(ts1.shape) == 2:
        # when given a vector series, sum over the squares
        dsq = np.add.reduce(dsq, axis=1)
    sum_dsq1 = np.add.accumulate(dsq)
    sum_dsq2 = np.add.accumulate(dsq[::-1])
    sumsq = 2.*sum_dsq1[-1]
    msd  = (sumsq
            - np.concatenate(([0.], sum_dsq1[:-1]))
            - np.concatenate(([0.], sum_dsq2[:-1]))) / np.arange(n, 0, -1) \
            - 2.*correlation(ts1, ts2)
    return msd

def gaussian(ts, sigma = 1.0, mu = 0.0):
    """
    Returns a gaussian.
    """
    gauss = np.exp(-0.5*((ts - mu) / sigma)**2)
    return gauss

def window(series, window_function):
    """
    Returns a smoothed signal.

    :param series: the signal to smooth.
    :type series: np.ndarray
    :param window_function: window function
    :type window_function: np.ndarray
    :return: the smoothed signal.
    :rtype: np.ndarray
    """
    # smoothed_s is an array of length 2*len(ts)-1
    # smoothed_s is the smoothed version of ts obtained by applying
    # a window function to ts
    smoothed_signal = np.zeros((2*len(series) - 2,), dtype = np.float)

    # window function used to smooth the spectrum series
    res = series*window_function

    # The second half of smoothed_signal is filled using periodic conditions
    smoothed_signal[:len(series)] = res
    smoothed_signal[len(series):] = res[-2:0:-1]

    return smoothed_signal
