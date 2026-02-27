import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Inputs
    # Handle scaler,list and Numpy array input
    '''

    
    This code work well for scalers ,but not for list  and numpy array containing both, negative and postive values.
    if x<=0:
        return 0

    else:
        return x
    # Output
    #return output/result using NumPy
    '''
    
    return np.maximum(0,x)