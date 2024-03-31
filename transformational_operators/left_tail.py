import numpy as np
import torch

def left_tail(x, maximum = 0):

    '''
    NaN everything greater than maximum, maximum should be constant.
    This operator changes to NaN everything greater than a specified value.
    
    Example:
    x                      = [0.1, 0.3, 0.5, 0.7, 0.9]
    maximum                = 0.5
    left_tail(x, maximum)  = [0.1, 0.3, 0.5, nan, nan]
    
    Example taken from: https://platform.worldquantbrain.com/learn/data-and-operators/detailed-operator-descriptions#arc_tanx
        left_tail(rank(close), maximum = 0.02)
            returns NaN, if rank(close)> 0.02; else returns rank(close).
        Note: `close` is a field in the "Price Volume Data for Equity" dataset. Type: Matrix.
            All datasets: https://platform.worldquantbrain.com/data/data-sets?delay=1&instrumentType=EQUITY&limit=20&offset=0&region=USA&universe=TOP3000
      
    Doctest:
    >>> x = torch.tensor([0.1, 0.3, 0.5, 0.7, 0.9])
    >>> np.round(left_tail(x, maximum = 0.5), 1).tolist()
    [0.1, 0.3, 0.5, nan, nan]
    '''
    x[x > maximum] = float('nan')
    return x.tolist()

    
# To run the doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()