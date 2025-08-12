import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

# plt 기본 폰트 변경
fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

data = pd.read_csv("C:/moon/data/seoulDust 1.csv", names=["년", "월", "일", "시간", "권역", "구", "미세", "초미세", "상태"])
data = data[data["구"] == "종로구"]

def convert_date(d):
    # return "%s-%s-%s %s" % (d["년"], d["월"], d["일"], d["시간"])
    return d["년"]

data["날짜"] = data[["년", "월", "일", "시간"]].apply(convert_date)
print(data["날짜"])
# data = data.sort_values(by=["년", "월",])
# xdata = data[["년", "월", "일", "시간"]]
# ydata1 = pd.to_numeric(data["미세"])
# ydata2 = pd.to_numeric(data["초미세"])

# xdata = xdata.to_numpy()
# ydata1 = ydata1.to_numpy()

# print(ydata1)

# _, sub1conf = plt.subplots()
# p1 = sub1conf.plot(xdata, ydata1)

# plt.plot(xdata, ydata1)
# plt.show()