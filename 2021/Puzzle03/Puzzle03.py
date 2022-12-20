import pandas
import numpy

path = r'2021\Puzzle03\Puzzle03_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n', dtype=str)

input = []
for i in range(len(raw_input[0])):
    input.append(list(raw_input[0][i]))

numlength = len(input[0])
array = numpy.array(input)

gamma = ''
epsilon = ''

for i in range(numlength):
    zeros = numpy.count_nonzero(array[:, i] == '0')
    ones = numpy.count_nonzero(array[:, i] == '1')
    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

output1 = gamma_int * epsilon_int
print('Output1: ' + str(output1))

O2_rating = ''
CO2_rating = ''
O2array = array.copy()
CO2array = array.copy()

for i in range(numlength):
    newO2array = []
    zeros = numpy.count_nonzero(O2array[:, i] == '0')
    ones = numpy.count_nonzero(O2array[:, i] == '1')
    if zeros > ones:
        char = '0'
    else:
        char = '1'
    
    O2_rating += char

    for j in range(len(O2array)):
        if O2array[j, i] == char:
            newO2array.append(O2array[j])
    
    O2array = numpy.array(newO2array)

for i in range(numlength):
    if len(CO2array) == 1:
        for k in range(i, numlength):
            CO2_rating += CO2array[0, k]
        break
    newCO2array = []
    zeros = numpy.count_nonzero(CO2array[:, i] == '0')
    ones = numpy.count_nonzero(CO2array[:, i] == '1')
    if zeros <= ones:
        char = '0'
    else:
        char = '1'
    
    CO2_rating += char

    for j in range(len(CO2array)):
        if CO2array[j, i] == char:
            newCO2array.append(CO2array[j])
    
    CO2array = numpy.array(newCO2array)

O2_rating_int = int(O2_rating, 2)
CO2_rating_int = int(CO2_rating, 2)

output2 = O2_rating_int * CO2_rating_int
print('Output2: ' + str(output2))
