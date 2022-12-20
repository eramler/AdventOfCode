import pandas
import numpy

path = r'2020\Puzzle17\Puzzle17_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

#PART 1
input_array = numpy.full((1, len(raw_input[0]), len(raw_input[0][0])), [0], dtype=int)

for i in range(0, len(input_array[0])):
    for j in range(0, len(input_array[0, i])):
        if raw_input[0][i][j] == '#':
            input_array[0, i, j] = 1

def expand_array(array):
    updown = numpy.full((len(array), 1, len(array[0, 0])), 0)
    widened_updown = numpy.concatenate((updown, array, updown), axis=1)
    leftright = numpy.full((len(widened_updown), len(widened_updown[0]), 1), 0)
    widened = numpy.concatenate((leftright, widened_updown, leftright), axis=2)
    newlayer = numpy.full((1, len(widened[0]), len(widened[0, 0])), 0)
    expanded_array = numpy.concatenate((newlayer, widened, newlayer), axis=0)
    return expanded_array

def check_neighbours(array, i,j,k):
    region = array[max(0, i-1):i+2, max(0, j-1):j+2, max(0, k-1):k+2]
    neighbours = numpy.sum(region) - array[i, j, k]
    return neighbours

def update_values(array):
    updated = numpy.zeros_like(array)
    for i in range(len(array)):
        for j in range(len(array[0])):
            for k in range(len(array[0, 0])):
                neighbours = check_neighbours(array, i, j, k)
                if neighbours == 3 or (array[i, j, k] == 1 and neighbours == 2):
                    updated[i, j, k] = 1
    return updated

def run_simulation(input_array, steps):
    for iteration in range(0, steps):
        expanded_space = expand_array(input_array)
        updated_values = update_values(expanded_space)
        input_array = updated_values
    return updated_values

simulated = run_simulation(input_array, 6)

output1 = numpy.sum(simulated)
print('Output 1: ' + str(output1))

#PART 2
input_array4d = numpy.full((1, 1, len(raw_input[0]), len(raw_input[0][0])), [0], dtype=int)

for i in range(len(input_array4d[0, 0])):
    for j in range(len(input_array4d[0, 0, i])):
        if raw_input[0][i][j] == '#':
            input_array4d[0, 0, i, j] = 1

def expand_array4d(array):

    inout = numpy.full((1, len(array[0]), len(array[0, 0]), len(array[0, 0, 0])), 0)
    widened_inout = numpy.concatenate((inout, array, inout), axis=0)

    updown = numpy.full((len(widened_inout), len(widened_inout[0]), 1, len(widened_inout[0, 0, 0])), 0)
    widened_updown = numpy.concatenate((updown, widened_inout, updown), axis=2)

    leftright = numpy.full((len(widened_updown), len(widened_updown[0]), len(widened_updown[0, 0]), 1), 0)
    widened = numpy.concatenate((leftright, widened_updown, leftright), axis=3)

    newlayer = numpy.full((len(widened), 1, len(widened[0, 0]), len(widened[0, 0, 0])), 0)
    expanded_array = numpy.concatenate((newlayer, widened, newlayer), axis=1)

    return expanded_array

def check_neighbours4d(array, w,i,j,k):
    region = array[max(0, w-1):w+2, max(0, i-1):i+2, max(0, j-1):j+2, max(0, k-1):k+2]
    neighbours = numpy.sum(region) - array[w, i, j, k]
    return neighbours

def update_values4d(array):
    updated = numpy.zeros_like(array)
    for w in range(len(array)):
        for i in range(len(array[0])):
            for j in range(len(array[0, 0])):
                for k in range(len(array[0, 0, 0])):
                    neighbours = check_neighbours4d(array, w, i, j, k)
                    if neighbours == 3 or (array[w, i, j, k] == 1 and neighbours == 2):
                        updated[w, i, j, k] = 1
    return updated

def run_simulation4d(input_array, steps):
    for iteration in range(0, steps):
        expanded_space = expand_array4d(input_array)
        updated_values = update_values4d(expanded_space)
        input_array = updated_values
    return updated_values

simulated4d = run_simulation4d(input_array4d, 6)

output2 = numpy.sum(simulated4d)
print('Output 2: ' + str(output2))