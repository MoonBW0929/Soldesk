import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np

# plt 기본 폰트 변경
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False


data = pd.read_csv("C:/moon/data/titanic.csv")
data = data[data["Survived"] == 0]


pclass = data["Pclass"].unique()
team = data["Pclass"].value_counts().to_numpy()
w = {"width" : 0.7, "edgecolor" : "black", "linewidth" : 1}

plt.pie(team,labels=pclass, autopct="%.1f%%",
        wedgeprops=w)

plt.show()