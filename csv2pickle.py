import pandas as pd
import pickle

df = pd.read_csv('FilePath',encoding="utf-8", engine='python',header=None)
a=set(df.values.ravel())        #Firstly,converting csv file into set 

with open('Pickle FilePath', 'wb') as f:
    pickle.dump(a, f)
with open('Pickle FilePath', 'rb') as f:
    dest_object_name = pickle.load(f) 
