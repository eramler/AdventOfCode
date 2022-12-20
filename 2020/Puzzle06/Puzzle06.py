import pandas

path = r'2020\Puzzle06\Puzzle06_input.txt'
raw_input = pandas.read_csv(path, sep='\n', header=None, skip_blank_lines=False)

mylist = [[]]
entry = 0

for i in range(0, len(raw_input)):
    if str(raw_input[0][i]) != 'nan':
        mylist[entry].append(str(raw_input[0][i]))
    else:
        entry += 1
        mylist.append([])

#Part1 and Part2
output1 = 0
output2 = 0

for j in range(0, len(mylist)):
    anyone = set('')
    everyone = set('abcdefghijklmnopqrstuvwxyz')
    for k in range(0, len(mylist[j])):
        ans = set(mylist[j][k])
        anyone = anyone.union(ans)
        everyone = everyone.intersection(ans)
    output1 += len(anyone)
    output2 += len(everyone)

print('Output1: ' + str(output1))
print('Output2: ' + str(output2))
