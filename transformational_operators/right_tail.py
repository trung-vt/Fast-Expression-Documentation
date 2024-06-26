import numpy as np
import torch

def right_tail(x, minimum = 0):
    '''
    NaN everything less than minimum, minimum should be constant.
    This operator changes to NaN everything less than specified value.
    
    Example:
    x                      = [0.1, 0.3, 0.5, 0.7, 0.9]
    minimum                = 0.5
    right_tail(x, minimum) = [nan, nan, 0.5, 0.7, 0.9]
    
    Example taken from: https://platform.worldquantbrain.com/learn/data-and-operators/detailed-operator-descriptions#arc_tanx
        right_tail(rank(volume), minimum = 0.5)
            returns NaN, if rank(volume) < 0.5; else returns rank(volume).
        Note: `volume` is a field in the "Price Volume Data for Equity" dataset. Type: Matrix.
            All datasets: https://platform.worldquantbrain.com/data/data-sets?delay=1&instrumentType=EQUITY&limit=20&offset=0&region=USA&universe=TOP3000
      
    Doctest:
    >>> x = torch.tensor([0.1, 0.3, 0.5, 0.7, 0.9])
    >>> np.round(right_tail(x, minimum = 0.5), 1).tolist()
    [nan, nan, 0.5, 0.7, 0.9]
    '''
    x[x < minimum] = float('nan')
    return x.tolist()

    
# To run the doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()