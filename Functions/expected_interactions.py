import numpy as np

def expected_interactions(array_of_interactions):
    mean = array_of_interactions.mean()
    std = array_of_interactions.std()

    altered_array = []
    for i in array_of_interactions:
        if i < mean + 2*std:
            altered_array.append(i)

    return (np.array(altered_array).mean())