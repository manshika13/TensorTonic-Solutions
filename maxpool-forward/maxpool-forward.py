def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    #1. Measure our board
    No_of_rows=len(X)
    Elements_in_first_row=len(X[0])

    #2. Prepare the empty list for our answer
    final_result=[]

    #3. The MOVERS Loop
    #we move our window accross the grid
    # we jump by 'stride' each time
    # range(start,stop,step)-> range(0,rows,stride) handles the jmping for us

    for i in range(0,No_of_rows-pool_size+1,stride):
        new_row=[]
        for j in range(0,Elements_in_first_row-pool_size+1,stride):
            # INSIDE THE FLASHLIGHT
            # Now our window is sitting at position (i,j).
            # We need to find the max value inside the small box.
            max_value=float('-inf') # Start with a small number
            # THE COLLOCTORS LOOPs
            # Look at the small box starting at i,j
            for window_row in range(i,i+ pool_size):
                for window_col in range(j,j+pool_size):
                    current_val=X[window_row][window_col]
                    if current_val>max_value:
                        max_value=current_val
            # We found the winner for this window
            new_row.append(max_value)
        # We finished a whole row of windowa.Add the row to the final_result
        final_result.append(new_row)
    return final_result
