import pandas

path = r'2022/05/05_input.txt'
raw_input = pandas.read_csv(path, header=None, skip_blank_lines=False)[0]

# separate starting position and instructions
ProcessingInstructions = False
setup = []
instructions = []

for i in range(len(raw_input)):
    if str(raw_input[i]) == "nan":
        ProcessingInstructions = True
    elif ProcessingInstructions == True:
        instructions.append(raw_input[i])
    else:
        setup.append(raw_input[i])

# remove pile indices from setup and reverse so that bottom boxes are first in list
pileNames = setup.pop(-1).split()
setup.reverse()

# create lists that correspond to each stack instead of each layer
setup_transposed = []
for i in range(len(pileNames)):
    pile = []
    base_r = setup[0].index("]")
    for j in range(len(setup)):
        if setup[j][:base_r+1] != "   ":
            pile.append(setup[j][:base_r+1])
        setup[j] = setup[j][base_r+2:]
    setup_transposed.append(pile)

# add stacks to dataframe column with pilenames as row index 
df = pandas.DataFrame({"Boxes":setup_transposed})["Boxes"]
df.index = pileNames

df2 = pandas.DataFrame({"Boxes":setup_transposed})["Boxes"]
df2.index = pileNames

# functions for manipulating and reading boxes
def moveTopBox(fromStack:str, toStack:str):
    box = df[fromStack].pop(-1)
    df[toStack].append(box)

def moveBoxes(quantity:int, fromStack:str, toStack:str):
    for i in range(quantity):
        moveTopBox(fromStack, toStack)

def uncodeInstructions(string:str):
    list = string.split()
    list.remove("move")
    list.remove("from")
    list.remove("to")
    return list

def readTopBoxes():
    list = []
    for i in range(len(df)):
        list.append(df[i][-1])
    print(list)

# output1
# for i in range(len(instructions)):
#     params = uncodeInstructions(instructions[i])
#     moveBoxes(int(params[0]), params[1], params[2])

# additional function needed for output2
def moveBoxesGroup(quantity:int, fromStack:str, toStack:str):
    for i in range(-quantity,0):
        box = df2[fromStack].pop(i)
        df2[toStack].append(box)

# output2
for i in range(len(instructions)):
    params = uncodeInstructions(instructions[i])
    moveBoxesGroup(int(params[0]), params[1], params[2])

readTopBoxes()
