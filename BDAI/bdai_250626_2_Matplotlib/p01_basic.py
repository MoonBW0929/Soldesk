from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# plt 기본 폰트 변경
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

ydata = np.array([12, 10, 5, 22, 8])
xdata = [10, 20, 30, 40, 50]

# 기본
# plt.plot(ydata)
# plt.show()

# x, y
# plt.plot(xdata, ydata)
# plt.show()

# 축 제목
# plt.plot(xdata, ydata)
# plt.xlabel("x축")
# plt.ylabel("y축")
# plt.axis([0, 300, -10, 200])
# plt.show()

# 제목
# d = {"fontsize" : 20, "fontweight" : "bold", "color" : "#FF0000"}
# plt.plot(xdata, ydata)
# plt.title("제목", loc="left")
# plt.title("제목2")
# plt.title("제목3", loc="right", fontdict=d)
# plt.show()

# 선
# plt.plot(xdata, ydata, "b:p")
# plt.plot(xdata, ydata, color="#A3F55A", marker="$♥$", linewidth=1, linestyle=":")
# plt.show()

# 격지
# plt.plot(xdata, ydata)
# plt.grid(axis="x", color="red", linestyle=":")
# plt.show()