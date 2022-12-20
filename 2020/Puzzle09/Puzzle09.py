import pandas

path = r'2020\Puzzle09\Puzzle09_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

mylist = raw_input[0].to_list()

#Part1
def find_invalid():
    for i in range(25, len(mylist)):
        valid = False
        for j in range(-25, 0):
            for k in range(j+1, 0):
                if mylist[i] == mylist[i+j] + mylist[i+k]:
                    valid = True
                    break
            if valid == True:
                break
        if valid == False:
            return mylist[i]

output1 = find_invalid()
print('Output1: ' + str(output1))

#Part2
def find_weakness(invalid_num):
    for i in range(0, len(mylist)):
        terms = []
        index = 0
        while sum(terms) < invalid_num:
            terms.append(mylist[i+index])
            index += 1
        if sum(terms) == invalid_num and len(terms) > 1:
            return min(terms) + max(terms)

output2 = find_weakness(output1)
print('Output2: ' + str(output2))
