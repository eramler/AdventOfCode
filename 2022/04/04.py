import pandas

colnames = ["set1", "set2"]
path = r'2022/04/04_input.txt'
raw_input = pandas.read_csv(path, header=None, sep=",", names=colnames)

def get_areas(min:int, max:int):
    areas = set(range(min, max+1))
    return areas

def preprocess(string:str):
    bounds = string.split("-")
    areas = get_areas(int(bounds[0]), int(bounds[1]))
    return areas

def check_either_contains(set1:set, set2:set):
    output = set1.issubset(set2) | set1.issuperset(set2)
    return output

def check_overlap(set1:set, set2:set):
    output = len(set1.intersection(set2)) > 0
    return output

output1, output2 = 0, 0

for i in range(len(raw_input["set1"])):
    areas1 = preprocess(raw_input["set1"][i])
    areas2 = preprocess(raw_input["set2"][i])
    if check_either_contains(areas1, areas2):
        output1 += 1
    if check_overlap(areas1, areas2):
        output2 += 1

print("Output1: " + str(output1))
print("Output2: " + str(output2))
