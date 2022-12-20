import pandas

path = r'2020\Puzzle02\Puzzle02_input.xlsx'
raw_input = pandas.read_excel(path, header=None)

mylist = raw_input[0].to_list()
output1 = 0
output2 = 0

for i in range(0, len(mylist)):
    #Part1
    hyphen_index = mylist[i].find('-')
    space1_index = mylist[i].find(' ')
    colon_index = mylist[i].find(':')

    minimum = int(mylist[i][0:hyphen_index])
    maximum = int(mylist[i][hyphen_index+1:space1_index])
    letter = mylist[i][colon_index-1]
    password = mylist[i][colon_index+2:]
    
    occurences = password.count(letter)
    if occurences <= maximum and occurences >= minimum:
        output1 += 1
    
    #Part2
    index1 = minimum-1
    index2 = maximum-1

    letter1 = password[index1]
    letter2 = password[index2]

    if (letter1 == letter) ^ (letter2 == letter):
        output2 += 1

print('Output 1: ' + str(output1))
print('Output 2: ' + str(output2))
