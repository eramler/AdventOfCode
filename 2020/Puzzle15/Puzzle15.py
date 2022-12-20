import pandas

path = r'2020\Puzzle15\Puzzle15_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

mylist = str(raw_input[0][0]).split(',')
mylist = list(map(int, mylist))

def elf_counter(input, count):
    mydict = {}
    for i in range(0, len(input)):
        mydict[input[i]] = i

    next_num = 0
    for i in range(len(input), count):
        num = next_num
        if num in mydict:
            next_num = i - mydict[num]
            mydict[num] = i
        else:
            next_num = 0
            mydict[num] = i
    
    return num
        
output1 = elf_counter(mylist, 2020)
print('Output1: ' + str(output1))

output2 = elf_counter(mylist, 30000000)
print('Output2: ' + str(output2))
