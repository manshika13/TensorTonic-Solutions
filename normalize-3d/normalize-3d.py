import numpy as np
import math

def normalize_3d(vectors):
    """
    Normalize 3D vector(s) to unit length.
    """
    if isinstance(vectors[0],(int,float)):
        vectors=[vectors]
        single_input=True
    else:
        single_input=False

    normalized = []
    for vec in vectors:
        x, y, z = vec
        mag = math.sqrt(x**2 + y**2 + z**2)
        if mag == 0:
            normalized.append([0.0, 0.0, 0.0])
        else:
            normalized.append([x/mag, y/mag, z/mag])
    return np.array(normalized[0]) if single_input else np.array(normalized)