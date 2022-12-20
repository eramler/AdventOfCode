import pandas

path = r'2020\Puzzle07\Puzzle07_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

mylist = []

for i in range(0, len(raw_input)):
    mylist.append([])
    mylist[i] = raw_input[0][i].replace(' contain', ',')
    mylist[i] = mylist[i].split(', ')

def bagsearch(bagtype):
    for i in range(0, len(mylist)):
        if bagtype in mylist[i][0]:
            return mylist[i]

def bagcheck(bagtype, multiplier=1):
    global is_gold
    global bag_sum
    bag_def = bagsearch(bagtype)
    for k in range(1, len(bag_def)):
        firstspace = bag_def[k].find(' ')
        bagindex = bag_def[k].find('bag')
        sub_bag = bag_def[k][firstspace:bagindex].strip()
        sub_bag_num = bag_def[k][:firstspace].strip()
        if sub_bag != 'other':
            if sub_bag == 'shiny gold':
                is_gold = True
            bag_sum += multiplier * int(sub_bag_num)
            bagcheck(sub_bag, multiplier * int(sub_bag_num))
    

#Part1
output1 = 0
branch_numbers = [[]]
branch = 0
level = 0
bag_sum = 0
for i in range(0, len(mylist)):
    is_gold = False
    bagcheck(mylist[i][0])
    if is_gold == True:
        output1 += 1
print('Output1: ' + str(output1))

# Part2
bag_sum = 0
bagcheck('shiny gold')
print('Output2: ' + str(bag_sum))
