
import numpy as target  
import matplotlib.pyplot as GRF

aleatorio = target.random.uniform(0, 32000, 50000)  
print(aleatorio)
GRF.hist(aleatorio, 25)  
GRF.title('DISTRIBUCION UNIFORME')
GRF.xlabel('VALORES')
GRF.show() 
