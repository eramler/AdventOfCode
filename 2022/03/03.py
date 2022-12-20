import pandas
import string

path = r'2022/03/03_input.txt'
raw_input = pandas.read_csv(path, header=None)[0]

def SplitCompartments(string):
    halfint = int(len(string) / 2)
    Comp1 = string[:halfint]
    Comp2 = string[halfint:]
    return [Comp1, Comp2]

def FindCommonItems(string1, string2):
    set1 = set(list(string1))
    set2 = set(list(string2))
    (shared,) = set1.intersection(set2)
    return shared

def ScoreFromPosition(item, list:list):
    score = list.index(item) + 1
    return score

ItemsList = list(string.ascii_letters)

output1 = 0
for i in range(len(raw_input)):
    ItemsInCompartments = SplitCompartments(raw_input[i])
    SharedItem = FindCommonItems(ItemsInCompartments[0], ItemsInCompartments[1])
    output1 += ScoreFromPosition(SharedItem, ItemsList)

print("Output1: " + str(output1))

def FindCommonItemGroup(elf1, elf2, elf3):
    set1 = set(elf1)
    set2 = set(elf2)
    set3 = set(elf3)
    (CommonItem,) = set1.intersection(set2).intersection(set3)
    return CommonItem

output2 = 0
for i in range(int(len(raw_input)/3)):
    badge = FindCommonItemGroup(raw_input[3*i], raw_input[3*i+1], raw_input[3*i+2])
    output2 += ScoreFromPosition(badge, ItemsList)

print("Output2: " + str(output2))
