import numpy as np

dust_data = open("C:/moon/seoul_dust.csv", "r", encoding="utf-8")
city_dust = {}
city_dust_cnt = {}

while True:
    dust_line = dust_data.readline()
    if not dust_line: break

    dust = np.array(dust_line.replace("\n", "").split(","))
    if dust[0] == '': continue

    if dust[7] in city_dust:
        city_dust[dust[7]] += int(dust[8]) + int(dust[9])
        city_dust_cnt[dust[7]] += 1
    else:
        city_dust[dust[7]] = int(dust[8]) + int(dust[9])
        city_dust_cnt[dust[7]] = 1


city_name = []
dust = []
for i, v in enumerate(city_dust):
    city_name.append(v)
    dust.append(city_dust[v] / city_dust_cnt[v])

city_name = np.array(city_name)
dust = np.array(dust)

print(city_name)
print(dust)

print(city_name[np.argmax(dust)])
print(city_name[np.argmin(dust)])
print(city_name[dust < np.mean(dust)])