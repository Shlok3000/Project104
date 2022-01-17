import csv
from collections import Counter
from heapq import heappush
with open("SOCR-HeightWeight.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

data = Counter(new_data)
mode_data_for_range = {
    "75-85": 0,
    "85-95": 0
}

for height, occurence in data.items():
    if 75 < float(height) < 85:
        mode_data_for_range["75-85"] += occurence
    elif 85 < float(height) < 95:
        mode_data_for_range["85-95"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0] + mode_range[1])/2)
print(mode)