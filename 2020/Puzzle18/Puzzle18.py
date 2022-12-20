import pandas
import numpy

path = r'2020\Puzzle18\Puzzle18_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

#PART 1
values = numpy.zeros(len(raw_input[0]))

def remove_spaces(string):
    return string.replace(' ', '')

def evaluate_substring(string):
    operator_pos = min([i for i in [string.find('+'), string.find('*')] if i > 0], default=10000)
    value = int(string[:operator_pos])
    number = string.count('+') + string.count('*')
    for i in range(number):
        next_op = min([i for i in [string[operator_pos+1:].find('+'), string[operator_pos+1:].find('*')] if i > 0], default=10000)
        if string[operator_pos] == '+':
            value += int(string[operator_pos+1:operator_pos+1+next_op])
        elif string[operator_pos] == '*':
            value *= int(string[operator_pos+1:operator_pos+1+next_op])
        operator_pos += 1 + next_op
    return value

def collapse_parentheses(string, advanced=False):
    for i in range(string.count(')')):
        end = string.find(')')
        start = end - string[:end][::-1].find('(')
        if advanced:
            value = evaluate_substring_adv(string[start:end])
        else:
            value = evaluate_substring(string[start:end])
        string = string.replace('(' + string[start:end] + ')', str(value))
    return string

def evaluate(string, advanced=False):
    stripped = remove_spaces(string)
    collapsed = collapse_parentheses(stripped, advanced)
    if advanced:
        value = evaluate_substring_adv(collapsed)
    else:
        value = evaluate_substring(collapsed)
    return value

for i in range(len(values)):
    values[i] = evaluate(raw_input[0][i])

output1 = int(sum(values))
print('Output1: ' + str(output1))

#PART 2
values_adv = numpy.zeros(len(raw_input[0]))

def evaluate_substring_adv(string):
    number = string.count('+')
    for i in range(number):
        pos = string.find('+')
        if string[:pos].find('*') == -1:
            prev_op = 0
        else:
            prev_op = pos - string[:pos][::-1].find('*')
        next_op = min([i for i in [string[pos+1:].find('+'), string[pos+1:].find('*')] if i > 0], default=10000)

        value = evaluate_substring(string[prev_op:pos+1+next_op])
        string = string[:pos+1+next_op].replace(string[prev_op:pos+1+next_op], str(value)) + string[pos+1+next_op:]
    return evaluate_substring(string)

for i in range(len(values_adv)):
    values_adv[i] = evaluate(raw_input[0][i], advanced=True)

output2 = int(sum(values_adv))
print('Output2: ' + str(output2))

# test = evaluate_substring_adv('6+6*9*2296+6+5')