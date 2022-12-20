import pandas

path = r'2022/07/07_input.txt'
raw_input = pandas.read_csv(path, header=None)[0]
print(raw_input)