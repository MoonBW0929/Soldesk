import numpy as np

subway = open("C:/moon/subway.csv", "r", encoding="utf-8")
subway_dict = {}
cnt = 0

while True:

    subway_line = subway.readline()
    if not subway_line: break

    line = np.array(subway_line.replace("\n", "").split(","))
    if line[0] == '': continue

    if not subway_dict.get(line[4], [False, False])[0]:
        subway_dict[line[4]] = np.array([int(line[5]), int(line[6])])
    else:
        subway_dict[line[4]] = subway_dict[line[4]] + np.array([int(line[5]), int(line[6])])


for sub in subway_dict:
    if subway_dict[sub][0] < subway_dict[sub][1]:
        print(sub)
        print(subway_dict[sub])