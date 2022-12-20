import pandas

path = r'2020\Puzzle10\Puzzle10_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

mylist = raw_input[0].to_list()

device_joltage = max(mylist) + 3

bag = mylist.copy()
bag.append(0)
bag.append(device_joltage)
bag.sort()

min_diffs = [0, 0, 0]
diffs = []

#Part1
for i in range(0, len(bag)-1):
    this_diff = bag[1] - bag[0]
    min_diffs[this_diff-1] += 1
    diffs.append(this_diff)
    bag.remove(bag[0])

output1 = min_diffs[0] * min_diffs[2]
print('Output1: ' + str(output1))

#Part2
output2 = 1

while len(diffs) > 0:
    three_index = diffs.index(3)
    if len(diffs[:three_index]) > 4:
        output2 = ('ERROR - Need to upgrade function to deal with larger lengths of 1s')
        break
    elif len(diffs[:three_index]) == 4:
        output2 *= 7
    elif len(diffs[:three_index]) == 3:
        output2 *= 4
    elif len(diffs[:three_index]) == 2:
        output2 *= 2
    for i in range(0, three_index + 1):
        diffs.remove(diffs[0])

print('Output2: ' + str(output2))
