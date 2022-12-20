import pandas
import numpy

path = r'2020\Puzzle12\Puzzle12_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

op = []
arg = []
for i in range(0, len(raw_input)):
    op.append(raw_input[0][i][0])
    arg.append(int(raw_input[0][i][1:]))
    
#Part1
north = 0
east = 0
bearing = 90

for i in range(0, len(op)):
    if op[i] == 'N':
        north += arg[i]
    if op[i] == 'S':
        north -= arg[i]
    if op[i] == 'E':
        east += arg[i]
    if op[i] == 'W':
        east -= arg[i]
    if op[i] == 'F':
        north += arg[i] * numpy.cos(numpy.deg2rad(bearing))
        east += arg[i] * numpy.sin(numpy.deg2rad(bearing))
    if op[i] == 'R':
        bearing += arg[i]
    if op[i] == 'L':
        bearing -= arg[i]

output1 = int(round(abs(north) + abs(east)))
print('Output1: ' + str(output1))

#Part2
north = 0
east = 0
w_north = 1
w_east = 10

for i in range(0, len(op)):
    if op[i] == 'N':
        w_north += arg[i]
    if op[i] == 'S':
        w_north -= arg[i]
    if op[i] == 'E':
        w_east += arg[i]
    if op[i] == 'W':
        w_east -= arg[i]
    if op[i] == 'F':
        north += arg[i] * w_north
        east += arg[i] * w_east
    if op[i] == 'R':
        w_north_new = - w_east * numpy.sin(numpy.deg2rad(arg[i])) + w_north * numpy.cos(numpy.deg2rad(arg[i]))
        w_east_new = w_east * numpy.cos(numpy.deg2rad(arg[i])) + w_north * numpy.sin(numpy.deg2rad(arg[i]))
        w_north = int(round(w_north_new))
        w_east = int(round(w_east_new))
    if op[i] == 'L':
        w_north_new = w_east * numpy.sin(numpy.deg2rad(arg[i])) + w_north * numpy.cos(numpy.deg2rad(arg[i]))
        w_east_new = w_east * numpy.cos(numpy.deg2rad(arg[i])) - w_north * numpy.sin(numpy.deg2rad(arg[i]))
        w_north = int(round(w_north_new))
        w_east = int(round(w_east_new))

output2 = abs(north) + abs(east)
print('Output2: ' + str(output2))
