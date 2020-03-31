import pandas as pd 

dic = {
    "nome":["a","b"],
    "nota":[1,2],
    "aprovado":["sim","nao"]
}
df = pd.DataFrame(dic)
print(df)