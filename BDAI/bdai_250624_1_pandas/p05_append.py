import pandas as pd

a = pd.DataFrame()
a["이름"] = ["새우깡", "양파링"]
a["가격"] = [5000, 4000]
print(a)
print("-----------------------------")

s = pd.Series(["빼빼로", 2000], index=["이름", "가격"])
# a = a.append(s)
s = pd.DataFrame([s])
a = pd.concat([a, s])
print(a)
print("-----------------------------")

s = {"이름" : "포카칩", "가격" : 6000}
s = pd.DataFrame([s])
a = pd.concat([a, s])
print(a)
print("-----------------------------")