import pandas

path = r'2020\Puzzle03\Puzzle03_input.xlsx'
raw_input = pandas.read_excel(path, header=None)

mylist = raw_input[0].to_list()

def count_trees(rightstep, downstep=1):
    path_index = 0
    trees = 0

    for i in range(0, len(mylist), downstep):
        path = mylist[i][path_index]
        
        if path == '#':
            trees += 1

        path_index += rightstep
        if path_index >= 31:
            path_index -= 31
    
    return(trees)

#Part1
output1 = count_trees(rightstep=3)
print('Output1: ' + str(output1))

#Part2
slope1 = count_trees(rightstep=1)
slope2 = output1
slope3 = count_trees(rightstep=5)
slope4 = count_trees(rightstep=7)
slope5 = count_trees(rightstep=1, downstep=2)

output2 = slope1 * slope2 * slope3 * slope4 * slope5

print('Output2: ' + str(output2))
