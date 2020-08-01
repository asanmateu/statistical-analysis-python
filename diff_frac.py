import numpy as np

def diff_frac(data_A, data_B):

    """ Function to compute fraction on A/B testing"""

    frac_A = np.sum(data_A) / len(data_A)
    frac_B = np.sum(data_B) / len(data_B)

    return frac_B - frac_A

