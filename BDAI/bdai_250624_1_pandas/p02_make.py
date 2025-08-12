import pandas as pd
import numpy as np

a = pd.DataFrame()
a["이름"] = np.array(["홍", "김"])
a["나이"] = np.array([20, 30])
print(a)
print("-------------------------------")

c = [["홍", 20], ["김", 30]]
c = pd.DataFrame(c, columns=["이름", "나이"])
print(c)
print("-------------------------------")

d = {"이름" : ["홍", "김"], "나이" : [20, 30]}
d = pd.DataFrame(d)
print(d)
print("-------------------------------")

e = [{"이름" : "홍", "나이" : 20},
     {"이름" : "김", "나이" : 30}]
e = pd.DataFrame(e)
print(e)
print("-------------------------------")