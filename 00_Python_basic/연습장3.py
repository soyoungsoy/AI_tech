import numpy as np
import pandas as pd

dic1 = []

for 변수 in [1, 2, 3]:
  aa = print(" {'userid' : ", 변수, '}')
  dic1.append(aa)


print(type(dic1))

df = pd.DataFrame(dic1)
df