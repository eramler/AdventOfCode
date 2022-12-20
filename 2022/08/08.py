import pandas
import numpy

path = r'2022/08/08_input.txt'
raw_input = pandas.read_csv(path, header=None)[0]

# preprocessing
array = numpy.zeros((len(raw_input), len(raw_input[0])), dtype=int)

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i,j] = raw_input[i][j]

# functions
def checkView(value, view):
    if len(view) == 0 or max(view) < value:
        return True
    else:
        return False

def checkVisUp(i, j, array):
    value = array[i,j]
    view = array[:i,j]
    return checkView(value, view)

def checkVisDown(i, j, array):
    value = array[i,j]
    view = array[i+1:,j]
    return checkView(value, view)

def checkVisLeft(i, j, array):
    value = array[i,j]
    view = array[i,:j]
    return checkView(value, view)

def checkVisRight(i, j, array):
    value = array[i,j]
    view = array[i,j+1:]
    return checkView(value, view)

def checkVisibility(i, j, array):
    return checkVisUp(i, j, array) or checkVisDown(i, j, array) or checkVisLeft(i, j, array) or checkVisRight(i, j, array)

output1 = 0

for i in range(len(array)):
    for j in range(len(array[i])):
        if checkVisibility(i, j, array):
            output1 += 1

print("Output1: " + str(output1))




