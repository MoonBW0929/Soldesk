import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# plt 기본 폰트 변경
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

# 막대 그래프 : 항목 간의 절대적인 크기 비교, x축이 숫자일 필요는 없음
# ydata = [12, 10, 5, 22, 8]
# xdata = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"]

# plt.bar(xdata, ydata, color=["g", "r", "b", "yellow", "black"], width=0.2, edgecolor="yellow", linewidth=1)

# plt.show()

# y축 값을 여러개, 가로
# ydata1 = [12, 10, 5, 22, 8]
# ydata2 = [22, 33, 11, 7, 3]
# xLabel = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"]
# xdata = np.arange(len(xLabel))

# plt.bar(xdata, ydata1, width=0.3, color="green", align="edge")
# plt.bar(xdata-0.3, ydata2, width=0.3, color="blue", align="edge")
# plt.show()

# y축 값을 여러개, 세로
ydata1 = [12, 10, 5, 22, 8]
ydata2 = [22, 33, 11, 7, 3]
xLabel = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"]
xdata = np.arange(len(xLabel))

plt.bar(xdata, ydata1, color="green")
plt.bar(xdata, ydata2, color="blue", bottom=ydata1)
plt.show()