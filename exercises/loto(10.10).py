import numpy as np

def get_loto(num):
    loto = np.random.randint(1, 101, size=(num, 5, 5))
    return loto
    print(loto)
    
print((get_loto(4)))