import pandas as pd 
import numpy as np

dic = {
    "nome":["a","b"],
    "nota":[1,2],
    "aprovado":["sim","nao"]
}
df = pd.DataFrame(dic)  
print(df)

ff = pd.Series(dic)
print (ff)

a = [1,2,3,4,5]
ar = np.array(a)
rr = np.array([(1,2,3,4,5),(1,2,3,4,5)])
print(ar)
print(rr)