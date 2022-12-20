import pandas

path = r'2021\Puzzle02\Puzzle02_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

input = raw_input[0]

horizontal = 0
depth = 0

depth2 = 0
aim = 0

for i in range(len(input)):
    string = input[i].split(' ')
    command = string[0]
    amount = int(string[1])
    if command == 'forward':
        horizontal += amount
        depth2 += aim * amount
    elif command == 'down':
        depth += amount
        aim += amount
    elif command == 'up':
        depth -= amount
        aim -= amount
    else:
        print('ERROR')

output1 = horizontal * depth
output2 = horizontal * depth2
print('Output1: ' + str(output1))
print('Output2: ' + str(output2))

