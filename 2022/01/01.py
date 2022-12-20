import pandas
import numpy

path = r'2022/01/01_input.txt'
raw_input = pandas.read_csv(path, header=None, skip_blank_lines=False)[0]

elves = []
calories = 0

for i in range(len(raw_input)):
    if numpy.isnan(raw_input[i]):
        elves.append(calories)
        calories = 0
    else:
        calories += raw_input[i]

output1 = max(elves)
print("Output1: " + str(output1))

elvesSorted = sorted(elves, reverse=True)
print(elvesSorted)
output2 = sum(elvesSorted[0:3])
print("Output2: " + str(output2))
