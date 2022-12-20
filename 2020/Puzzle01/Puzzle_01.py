import pandas

path = r'2020\Puzzle01\Puzzle01_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

mylist = raw_input[0].to_list()

#Part1
for i in range(0, len(mylist)):
    for j in range(i, len(mylist)):
        sum = mylist[i] + mylist[j]
        if sum == 2020:
            output1 = mylist[i] * mylist[j]
            print('Output1: ' + str(output1))

#Part2
for i in range(0, len(mylist)):
    for j in range(i, len(mylist)):
        for k in range(j, len(mylist)):
            sum = mylist[i] + mylist[j] + mylist[k]
            if sum == 2020:
                output2 = mylist[i] * mylist[j] * mylist[k]
                print('Output2: ' + str(output2))
