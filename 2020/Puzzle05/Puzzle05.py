import pandas
import numpy

path = r'2020\Puzzle05\Puzzle05_input.txt'
raw_input = pandas.read_csv(path, header=None)

mylist = raw_input[0].to_list()

rows = 128
columns = 8
#Part1
ids = numpy.zeros(len(mylist)).astype(int)

for i in range(0, len(mylist)):
    rows_available = numpy.arange(0, rows)
    cols_available = numpy.arange(0, columns)
    for j in range(0, 7):
        split = int(len(rows_available)/2)
        if mylist[i][j] == 'F':
            rows_available = rows_available[:split]
        elif mylist[i][j] == 'B':
            rows_available = rows_available[split:]
        else:
            print('Unexpected Character found: ' + mylist[i][j])
            break

    for k in range(7, 10):
        split = int(len(cols_available)/2)
        if mylist[i][k] == 'L':
            cols_available = cols_available[:split]
        elif mylist[i][k] == 'R':
            cols_available = cols_available[split:]
        else:
            print('Unexpected Character found: ' + mylist[i][k])
            break

    ids[i] = rows_available * 8 + cols_available

output1 = numpy.amax(ids)
print('Output1: ' + str(output1))

#Part2
all_ids = numpy.arange(0, rows*columns)

set1 = set(ids)
set2 = set(all_ids)

remaining_ids = set1 ^ set2

front = numpy.arange(0, numpy.amin(ids))
back = numpy.arange(numpy.amax(ids)+1, len(all_ids))
empty_ids = set(numpy.concatenate((front, back)))

my_id = remaining_ids ^ empty_ids
output2 = ''.join(str(x) for x in my_id)
print('Output2: ' + str(output2))
