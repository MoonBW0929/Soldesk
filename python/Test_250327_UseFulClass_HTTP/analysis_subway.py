# 요일별 이용객수(탄+내린) 평균

from datetime import datetime
from os import write

sub_data = open("C:\\moon\\subway.csv", "r", encoding="utf-8")
week_dict = {"Monday":[0, 0], "Tuesday":[0, 0], "Wednesday":[0, 0], "Thursday":[0, 0], "Friday":[0, 0], "Saturday":[0, 0], "Sunday":[0, 0]}

for line in sub_data.readlines():
    line = line.replace("\n", "").split(",")
    if line == ['']:
        continue

    week = datetime.strftime(datetime.strptime((line[0]+line[1]+line[2]), "%Y%m%d"), "%A")
    cnt = int(line[5]) + int(line[6])

    week_dict[week][0] += 1
    week_dict[week][1] += cnt

sub_log = open("C:\\moon\\subwayResult.csv", "a", encoding="utf-8")

week_dict = dict(sorted(week_dict.items(), key=lambda x : (x[1][0] / x[1][1])))

for w, ls in week_dict.items():
    sub_log.write("%s,%.0f\n" % (w, (ls[1] / ls[0])))

sub_data.close()
sub_log.close()