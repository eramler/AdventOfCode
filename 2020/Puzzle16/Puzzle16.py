import pandas
import numpy

path = r'2020\Puzzle16\Puzzle16_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

i = 0
raw_rules = []
while raw_input[0][i] != 'your ticket:':
    raw_rules.append(raw_input[0][i])
    i += 1

i += 1
myticket = raw_input[0][i].split(',')

i += 2
tickets = []
for j in range(i, len(raw_input[0])):
    tickets.append(raw_input[0][j].split(','))

rule_class = []
rule_mins = []
rule_maxs = []
for j in range(0, len(raw_rules)):
    class_ind = raw_rules[j].find(':')
    rule_class.append(raw_rules[j][:class_ind])

    r_ind1 = class_ind + 2
    r_ind2 = raw_rules[j].find('-')
    r_ind3 = raw_rules[j].find(' or ') + 4
    r_ind4 = raw_rules[j].find('-', r_ind3)

    rule_mins.append([])
    rule_maxs.append([])
    rule_mins[j].append(int(raw_rules[j][r_ind1:r_ind2]))
    rule_maxs[j].append(int(raw_rules[j][r_ind2+1:r_ind3-4]))
    rule_mins[j].append(int(raw_rules[j][r_ind3:r_ind4]))
    rule_maxs[j].append(int(raw_rules[j][r_ind4+1:]))

#Part1
invalid_tickets = []
output1 = 0
for k in range(0, len(tickets)):
    for l in range(0, len(tickets[k])):
        valid = False
        value = int(tickets[k][l])
        for m in range(0, len(rule_mins)):
            if value >= rule_mins[m][0] and value <= rule_maxs[m][0]:
                valid = True
                break
            elif value >= rule_mins[m][1] and value <= rule_maxs[m][1]:
                valid = True
                break
        if valid == False:
            output1 += value
            invalid_tickets.append(k)

print('Output1: ' + str(output1))

#Part2
invalid_tickets.sort(reverse=True)
for i in range(0, len(invalid_tickets)):
    del tickets[invalid_tickets[i]]

def check_column(field_index, col_index):
    valid = True
    for i in range(0, len(tickets)):
        value = int(tickets[i][col_index])
        if (value >= rule_mins[field_index][0] and value <= rule_maxs[field_index][0]) or (value >= rule_mins[field_index][1] and value <= rule_maxs[field_index][1]):
            pass
        else:
            valid = False
            break
    return valid

matrix = numpy.zeros((len(tickets[0]), len(rule_class)))
for i in range(0, len(rule_class)):
    for j in range(0, len(tickets[0])):
        a = check_column(i, j)
        matrix[i][j] = a

columns = numpy.zeros(len(rule_class), dtype=int)
for i in range(0, len(rule_class)):
    for j in range(0, len(matrix)):
        if sum(matrix[j]) == 1:
            col = numpy.where(matrix[j] == 1)[0][0]
            columns[j] = col
            for k in range(0 ,len(matrix)):
                matrix[k][col] = 0
            break

output2 = 1
for i in range(0, len(rule_class)):
    if rule_class[i][:9] == 'departure':
        output2 *= int(myticket[columns[i]])

print('Output2: ' + str(output2))
