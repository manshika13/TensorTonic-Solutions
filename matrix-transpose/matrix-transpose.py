import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    #get the dimension of original matrix
    A_array=np.array(A)
    m,n=A_array.shape
    # create a transpose matrix B with dimension (n,m) filled with zeros
    B=np.zeros((n,m),dtype=(np.array(A)).dtype)
    for i in range(m):
        for j in range(n):
            B[j][i]=A[i][j]
    
    return B
