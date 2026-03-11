import numpy as np

def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    recommended=np.array(recommended)
    relevant=np.array(relevant)

    precision_k = len(np.intersect1d(recommended[:k],relevant))/float(k)
    recall_k = len(np.intersect1d(recommended[:k],relevant))/float(len(relevant))

    return [precision_k,recall_k]