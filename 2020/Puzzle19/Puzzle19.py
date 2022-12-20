import pandas

path = r'2020\Puzzle19\Puzzle19_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

i = 0
raw_rules = []
while raw_input[0][i].find(':') != -1:
    raw_rules.append(raw_input[0][i])
    i += 1

raw_values = []
while i < len(raw_input[0]):
    raw_values.append(raw_input[0][i])
    i += 1

rule_dict = {}
for i in range(len(raw_rules)):
    separator = raw_rules[i].find(':')
    index = raw_rules[i][:separator]
    rule = raw_rules[i][separator+2:]
    rule_dict[index] = rule

#PART 1
def find_ruleset(rule):
    i = 0
    rule_set = set()
    while i < len(rule):
        j = 0
        while not set(rule[i]).issubset({'"a"', '"b"'}) :
            if rule[i][j] in ['"a"', '"b"']:
                j+=1
                continue
            values = rule_dict[rule[i][j]].split(' ')

            if values.count('|') > 0:
                index = values.index('|')

                values1 = values[:index]
                values2 = values[index+1:]

                newsplit = rule[i].copy()
                newsplit[j:j+1] = values2
                rule[i][j:j+1] = values1
                rule.append(newsplit)
                
            else:
                rule[i][j:j+1] = values

        string = ''
        for k in range(len(rule[i])):
            string += rule[i][k].strip('"')
        rule_set.add(string)
        i += 1
    return rule_set

rule0_set = find_ruleset([['0']])

output1 = 0
for i in range(len(raw_values)):
    if raw_values[i] in rule0_set:
        output1 += 1

print('Output1: ' + str(output1))

#PART 2
rule42_set = find_ruleset([['42']])
rule31_set = find_ruleset([['31']])

output2 = 0
for i in range(len(raw_values)):
    substring = raw_values[i]
    count42 = 0
    count31 = 0
    countother = 0
    while substring[:8] in rule42_set:
        count42 += 1
        substring = substring[8:]
    while substring[:8] in rule31_set:
        count31 += 1
        substring = substring[8:]
    if len(substring) == 0 and count42 > count31 and count31 > 0:
        output2 += 1

print('Output2: ' + str(output2))