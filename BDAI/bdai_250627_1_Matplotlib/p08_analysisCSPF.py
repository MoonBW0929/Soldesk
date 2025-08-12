import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np

# plt 기본 폰트 변경
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False


data = pd.read_csv("C:/moon/data/cspf.csv", names=["날짜", "노선", "역명", "찍고타", "안찍고타", "찍고내려", "안찍고내려"])
data = data.groupby("노선")[["찍고타", "안찍고타", "찍고내려", "안찍고내려"]].mean()
print(data)

# y축 값을 여러개, 가로
ydata1 = data["찍고타"].to_numpy()
ydata2 = data["안찍고타"].to_numpy()
ydata3 = data["찍고내려"].to_numpy()
ydata4 = data["안찍고내려"].to_numpy()
xLabel = data.index.to_numpy()
xdata = np.arange(len(xLabel))

plt.bar(xdata-0.3, ydata1, width=0.3, color="green", align="edge")
plt.bar(xdata-0.3, ydata2, width=0.3, color="red", align="edge", bottom=ydata1)
plt.bar(xdata, ydata4, width=0.3, color="yellow", align="edge", bottom=ydata3)
plt.bar(xdata, ydata3, width=0.3, color="blue", align="edge")
plt.xticks(xdata, xLabel)

plt.show()