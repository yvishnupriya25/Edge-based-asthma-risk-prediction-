import tensorflow
import numpy as np
import time
import sklearn
import asthama
actual_pefr=350

age=19
height=155
gender=1
hum=60
temp=33
pm25=16
pm10=23.62
print(hum,temp,pm25,pm10)
params = np.array([age, height, gender, temp, hum, pm25, pm10])
params=params.reshape(1,7,1)
print(params)
print(params.shape)
y=asthama.model.predict(params)
predicted_pefr=y+300
print("predicted pefr:",predicted_pefr)
perpefr=(actual_pefr/predicted_pefr)*100
print(perpefr)
if perpefr>=80:
    print("safe")
elif perpefr>=50:
    print("moderate")
else:
    print("risk")
            
            
            
            
            
            
        
            
            
           
    #print(data[1])
   
   
 

