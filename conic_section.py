import os
import pickle

filename = '/Users/lukin/kNN_model.sav'
neigh = pickle.load(open(filename, 'rb'))

print('a=')
a=input()
print('b=')
b=input()
print('c=')
c=input()
import pandas as pd
if ((a==0) & (b==0)) or ((a==0) & (c==0)) or ((b==0) & (c==0)):
    print('a, b and c cannot be both zero')
else:
    d = {'A' : [a], 'B': [b], 'C': [c]}
    inp = pd.DataFrame(data=d)
    out=neigh.predict(inp) 
    print(out)
