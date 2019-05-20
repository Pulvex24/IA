
import numpy as target  
import matplotlib.pyplot as GRF

values = target.random.uniform(0, 32000, 50000)  
print(values)
GRF.hist(values, 25)  
GRF.show() 