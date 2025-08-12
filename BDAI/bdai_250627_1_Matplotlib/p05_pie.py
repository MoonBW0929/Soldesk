import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# plt 기본 폰트 변경
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

# 파이 차트 : 점유율 표현
s_class = np.array(["902", "510", "기타"])
team = np.array([8, 10, 4])
e = [0.03, 0.03, 0.2]
w = {"width" : 0.7, "edgecolor" : "black", "linewidth" : 1}

plt.pie(team,labels=s_class, autopct="%.1f%%", startangle=45,
        explode=e, wedgeprops=w)

plt.show()