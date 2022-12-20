import pandas
import numpy

path = r'2020\Puzzle08\Puzzle08_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

op = []
arg = []
for i in range(0, len(raw_input)):
    op.append(raw_input[0][i][0:3])
    space_index = raw_input[0][i].index(' ')
    amount = int(raw_input[0][i][space_index:])
    arg.append(amount)

def run_program(operations, arguments):
    global program_fixed
    visits = numpy.zeros(len(operations), dtype=int)
    index = 0
    acc = 0

    while visits[index] == 0:
        visits[index] += 1
        if operations[index] == 'acc':
            acc += arguments[index]
            index += 1
        elif operations[index] == 'jmp':
            index += arguments[index]
        else:
            index += 1

        if index == len(operations):
            program_fixed = True
            break
    return acc

program_fixed = False

#Part1
output1 = run_program(op, arg)
print('Output1: ' + str(output1))

#Part2
for i in range(0, len(op)):
    if op[i] == 'jmp':
        new_op = op.copy()
        new_op[i] = 'nop'
    elif op[i] == 'nop':
        new_op = op.copy()
        new_op[i] = 'jmp'
    else:
        continue

    output2 = run_program(new_op, arg)
    if program_fixed:
        break

print('Output2: ' + str(output2))
