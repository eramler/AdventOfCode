import pandas
import numpy

path = r'2020\Puzzle11\Puzzle11_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

myarray = numpy.full((len(raw_input[0]), len(raw_input[0][0])), [''], dtype=str)

for i in range(0, len(myarray)):
    for j in range(0, len(myarray[i])):
        myarray[i][j] = raw_input[0][i][j]

#Part1
def check_seat(array, i, j, direction=[0,0]):
    global neighbours
    check_i = i + direction[0]
    check_j = j + direction[1]
    if check_i >= 0 and check_i < len(array) and check_j >= 0 and check_j < len(array[check_i]):
        if array[check_i][check_j] == '#':
            neighbours += 1

def update_seats1(array):
    global neighbours
    updated_array = array.copy()
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if array[i][j] != '.':
                neighbours = 0
                check_seat(array, i, j, direction=[-1,0])
                check_seat(array, i, j, direction=[-1,1])
                check_seat(array, i, j, direction=[0,1])
                check_seat(array, i, j, direction=[1,1])
                check_seat(array, i, j, direction=[1,0])
                check_seat(array, i, j, direction=[1,-1])
                check_seat(array, i, j, direction=[0,-1])
                check_seat(array, i, j, direction=[-1,-1])
                if array[i][j] == 'L' and neighbours == 0:
                    updated_array[i][j] = '#'
                elif array[i][j] == '#' and neighbours >= 4:
                    updated_array[i][j] = 'L'
    return updated_array

oldarray1 = myarray.copy()
newarray1 = update_seats1(oldarray1)

while numpy.array_equal(oldarray1, newarray1) == False:
    oldarray1 = newarray1.copy()
    newarray1 = update_seats1(oldarray1)

output1 = numpy.count_nonzero(oldarray1 == '#')
print('Output1: ' + str(output1))

#Part2
def check_floor(array, i, j):
    global visible
    if array[i][j] == '.':
        return True
    elif array[i][j] == '#':
        visible += 1
        return False
    elif array[i][j] == 'L':
        return False

def look_seats(array, i, j, direction=[0,0]):
    dist = 1
    check_i = i + direction[0]*dist
    check_j = j + direction[1]*dist
    if check_i >= 0 and check_i < len(array) and check_j >= 0 and check_j < len(array[check_i]):
        is_floor = check_floor(array, check_i, check_j)
        while is_floor:
            dist += 1
            check_i = i + direction[0]*dist
            check_j = j + direction[1]*dist
            if check_i >= 0 and check_i < len(array) and check_j >= 0 and check_j < len(array[check_i]):
                is_floor = check_floor(array, check_i, check_j)
            else:
                break

def update_seats2(array):
    global visible
    updated_array = array.copy()
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if array[i][j] != '.':
                visible = 0
                look_seats(array, i, j, direction=[-1,0])
                look_seats(array, i, j, direction=[-1,1])
                look_seats(array, i, j, direction=[0,1])
                look_seats(array, i, j, direction=[1,1])
                look_seats(array, i, j, direction=[1,0])
                look_seats(array, i, j, direction=[1,-1])
                look_seats(array, i, j, direction=[0,-1])
                look_seats(array, i, j, direction=[-1,-1])
                if array[i][j] == 'L' and visible == 0:
                    updated_array[i][j] = '#'
                elif array[i][j] == '#' and visible >= 5:
                    updated_array[i][j] = 'L'
    return updated_array

oldarray2 = myarray.copy()
newarray2 = update_seats2(oldarray2)

while numpy.array_equal(oldarray2, newarray2) == False:
    oldarray2 = newarray2.copy()
    newarray2 = update_seats2(oldarray2)

output2 = numpy.count_nonzero(oldarray2 == '#')
print('Output2: ' + str(output2))
