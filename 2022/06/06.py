import pandas

path = r'2022/06/06_input.txt'
raw_input = pandas.read_csv(path, header=None)[0][0]

def findFirstUnique(length:int, string:str):
    for i in range(len(string)):
        start = max(0, i-length)
        test = string[start:i]
        if len(set(list(test))) == length:
            return str(i)

print("Output1: " + findFirstUnique(4, raw_input))
print("Output2: " + findFirstUnique(14, raw_input))
