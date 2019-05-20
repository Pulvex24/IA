import numpy as target  
aleatorio = target.random.normal(0, 32000, 8000) 
print(aleatorio)
import matplotlib.pyplot as GRF  
GRF.hist(aleatorio, 100)  
GRF.title('DISTRIBUCION GAUSSIANA')
GRF.xlabel('VALORES')
GRF.show() 
