import numpy as np

def shuffle_seed(array):
    seed = np.random.randint(2 ** 32)
    np.random.seed(seed)
    result = np.random.permutation(array)
    return result, seed
 