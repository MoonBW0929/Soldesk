import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# plt 기본 폰트 변경
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

ydata = np.array([12, 10, 5, 22, 8])
xdata = [10, 20, 30, 40, 50]

# # 꺾은선 그래프
# # xdata 변화 대비 ydata의 변화 추이
# plt.plot(xdata, ydata)

# # 눈금 표현 변경
# plt.xticks(xdata, ["ㅋ", "ㅎ", "ㅐ", "ㅇ", "ㄹ"])
# # plt.yticks(ydata, ["a", "q", "w", "r", "s"])

# # 그래프 표현은 ydata를 사용하나, 눈금 표현을 다른 값으로 사용
# plt.yticks(np.arange(0, 23, 5), ["a", "q", "w", "r", "s"])

# # 눈금 디자인
# plt.tick_params("x", direction="inout", length=10, pad=10)
# plt.tick_params("y", color="green", labelcolor="brown", labelsize="20")

# plt.show()


# # 다중 선
# ydata2 = [55, 10, 50, 12, 6]

# plt.plot(xdata, ydata)
# plt.plot(xdata, ydata2, "r-*")
# plt.legend(["after", "before"])

# plt.show()


# 다중 선2 (y축을 각각)
ydata2 = [10000, 9090, 6054, 4238, 7860]

_, sub1conf = plt.subplots()
p1 = sub1conf.plot(xdata, ydata)
sub1conf.set_xlabel("x축")
sub1conf.set_ylabel("After")

sub2conf = sub1conf.twinx()
p2 = sub2conf.plot(xdata, ydata2, color="green")
sub2conf.set_ylabel("Before")

sub1conf.legend(p1 + p2, ["after", "before"])

plt.show()