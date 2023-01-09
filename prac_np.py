import numpy as np
temp =np.array([[12,13,45],
        [45,61,10],
        [1,3,80],
        [7,8,9]])
weights = np.array([0.1,2.3,4.0])
print(temp.shape)
print(weights.shape)
np.matmul(temp,weights)

import urllib.request

urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')

data_from_csv_geo = np.genfromtxt('climate.txt',delimiter=',',skip_header=1)
print(data_from_csv_geo.shape)

# in the csv file we have all the geographical things explained 

yields=np.matmul(data_from_csv_geo,weights)
print(yields)

# now yields is going to be the fourth column of the file 

results = np.concatenate((data_from_csv_geo,yields.reshape(10000,1)),axis=1)

print("new file shall look like ",results)

# Lets save it back to the file ! 

np.savetxt('climate_result.txt',results,fmt='%.2f',header='temperature,rainfall,humidity,yeild')

#--------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd 
# equation is x**2 + 2x + 1 = 0 
## x(x+2)+1 = 0 
### x**2 + x+x+1
# x (x +1 ) +(x+1)=0
# 
coeff = np.array([1,2,1])
np.roots(coeff)
print(np.roots(coeff))
a = pd.DataFrame(np.roots(coeff))
print(a)
print(a.plot(kind='line'))

#----------------------------------------------------------------------------------------------------------------

import numpy as np 
mock_ar = (np.ones((4,4)))*4
mock_ar2 = (np.ones((4,4)))*3
hypotenuse_arr=np.hypot(mock_ar2,mock_ar)
print(hypotenuse_arr)
