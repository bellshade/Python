import numpy as np

def standard_dev(vector:np.array) -> float:
    x_sum=np.sum([(value-np.mean(vector))**2 for value in vector])
    result=np.sqrt(x_sum/len(vector))
    return result
data=[1,2,3,1]
print(standard_dev(data))