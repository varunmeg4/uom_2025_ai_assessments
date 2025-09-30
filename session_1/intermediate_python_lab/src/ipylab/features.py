import numpy as np
from typing import Sequence

def feature_vector(x: np.ndarray) -> list[float]:
    """
    Compute basic features for 1D signal x:
      - RMS
      - zero-crossings (count)
      - peak-to-peak (max - min)
      - mean absolute diff (MAD)
    Use NumPy vectorized ops only.
    Return as [rms, zc, p2p, mad].
    TODO: implement.
    """
    # TODO: implement
    rms = np.sqrt(np.mean(np.square(x)))

    # Zero-crossings: sign change between consecutive samples
    signs = np.sign(x)
    zero_crossings = np.sum(signs[:-1] * signs[1:] < 0)

    # Peak-to-peak
    p2p = np.ptp(x)  # max - min

    # Mean absolute difference (MAD)
    mad = np.mean(np.abs(np.diff(x)))

    return [rms, float(zero_crossings), p2p, mad]
    #return [0.0, 0.0, 0.0, 0.0]
