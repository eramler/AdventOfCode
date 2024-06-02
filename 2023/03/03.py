import pandas
import numpy

# Get and process input
path = r'2023/03/03_input.txt'
raw_input = pandas.read_csv(path, header=None, skip_blank_lines=False)[0]

input = []
for i in range(len(raw_input)):
    input.append([])
    for j in range(len(raw_input[i])):
        input[i].append(raw_input[i][j])

array = numpy.array(input)

# Functions
def GetSurroundingElements(array: list[str], i: int, j: int, NumLen: int) -> list[str]:
    Top = max(i-1, 0)
    Bottom = min(i+1, len(array))+1
    Left = max(j-1, 0)
    Right = min(j + NumLen, len(array[i])) + 1
    return array[Top:Bottom, Left:Right]

def isEnginePart(array: list[str]) -> bool:
    result = False
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i,j] != '.' and not array[i,j].isdigit():
                result = True
    return result

CurrentNum = ""
Output1 = 0
# Part 1
for i in range(len(array)):
    iLen = len(array[i])
    for j in range(iLen):
        here = array[i, j]
        if here.isdigit():
            CurrentNum += here
        if (j == iLen-1) or (here.isdigit() and not array[i, min(j+1, iLen-1)].isdigit()) and CurrentNum != "":
            AddOutput = True
            NumLen = len(CurrentNum)
            Surrounding = GetSurroundingElements(array, i, j-(NumLen-1), NumLen)
            EnginePart = isEnginePart(Surrounding)
            if EnginePart: Output1 += int(CurrentNum)
            CurrentNum = ""

print(Output1)


