import numpy as np

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
            https://platform.worldquantbrain.com/data/data-sets/pv1/data-fields/volume?delay=1&instrumentType=EQUITY&region=USA&universe=TOP3000
      
    Doctest:
    >>> right_tail([0.1, 0.3, 0.5, 0.7, 0.9], minimum = 0.5)
    [nan, nan, 0.5, 0.7, 0.9]
    '''
    x = np.array(x)
    x[x < minimum] = np.nan
    return x.tolist()

# To run the doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()