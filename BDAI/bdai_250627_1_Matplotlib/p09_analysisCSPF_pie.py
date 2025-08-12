import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd

# plt 기본 폰트 변경
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

data = pd.read_csv("C:/moon/data/cspf.csv", names=["날짜", "노선", "역명", "찍고타", "안찍고타", "찍고내려", "안찍고내려"])
data = data.groupby("노선")[["찍고타", "안찍고타", "찍고내려", "안찍고내려"]].mean()

lable = ["찍고타", "안찍고타", "찍고내려", "안찍고내려"]
value = [data["찍고타"].mean(), data["안찍고타"].mean(), data["찍고내려"].mean(), data["안찍고내려"].mean()]

plt.pie(value,labels=lable, autopct="%.1f%%", startangle=45,
        )

plt.show()