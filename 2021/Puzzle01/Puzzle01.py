import pandas

path = r'2021\Puzzle01\Puzzle01_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

input = raw_input[0]
output1 = 0

for i in range(len(input)-1):
    if input[i+1] > input[i]:
        output1 += 1

print('Output1: ' + str(output1))

output2 = 0

for i in range(len(input)-3):
    if sum(input[i+1:i+4]) > sum(input[i:i+3]):
        output2 += 1

print('Output2: ' + str(output2))