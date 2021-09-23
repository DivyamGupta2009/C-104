import csv
from collections import Counter
with open ("Height.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []


for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(float(n_num))

n = len(new_data)
median_list = [len(new_data)]
median_list.sort()
total = 0

for x in new_data:
    total+=x
mean = total/n

data = Counter(new_data)
mode_data_for_range = {
                        "75-85": 0,
                        "85-95": 0,
                        "95-105": 0,
                        "105-115": 0,
                        "115-125": 0,
                        "125-135": 0,
                        "135-145": 0,
                        "145-155": 0,
                        "155-165": 0,
                        "165-175": 0
                    }
for weight, occurence in data.items():
    if 105 < float(weight) < 115:
        mode_data_for_range["105-115"] += occurence
    elif 110 < float(weight) < 120:
        mode_data_for_range["115-125"] += occurence
    elif 120 < float(weight) < 130:
        mode_data_for_range["125-135"] += occurence
    elif 130 < float(weight) < 140:
        mode_data_for_range["135-145"] += occurence
    elif 140 < float(weight) < 150:
        mode_data_for_range["145-155"] += occurence
    elif 150 < float(weight) < 160:
        mode_data_for_range["155-165"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)

if median_list % 2 == 0:
    #getting the first number
	median1 = float(new_data[median_list//2])
    #getting the second number
	median2 = float(new_data[median_list//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2
else:
	median = new_data[median_list//2]

print("Median is: " + str(median))
print(f"Mode is -> {mode:2f}")
print("Mean  /  Average is : " + str(mean))
