
import numpy as np 

def cor_co(array1,array2):

    mean1 = array1.mean()
    mean2 = array2.mean()

    std1 = array1.std()
    std2 = array2.std()

    mean3 = (array1*array2).mean()

    covarience = mean3 - mean1*mean2

    correlation_coeffienct = covarience/(std1*std2)

    return correlation_coeffienct


