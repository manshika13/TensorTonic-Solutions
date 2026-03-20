import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    """Reminder: input are given as np.array([1,2,3]) that does mean code convert the list into array,
    we need to mention it explicitely in the code ,otherwise it create the problem like n.dim is not a part of list """
    x=np.array(x)
    axis=0 if x.ndim==1 else 1
    max_x=np.max(x,axis=axis,keepdims=True)
    e_x=np.exp(x-max_x)

    sum_e_x=np.sum(e_x,axis=axis,keepdims=True)
    return e_x/sum_e_x
   