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

