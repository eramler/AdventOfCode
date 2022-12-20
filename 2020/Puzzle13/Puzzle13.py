import pandas

path = r'2020\Puzzle13\Puzzle13_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

starttime = int(raw_input[0][0])
services = raw_input[0][1].split(',')

#Part1
minutes = 0
output1 = 0
while output1 == 0:
    for i in range(0, len(services)):
        if services[i] != 'x':
            if(starttime + minutes) % int(services[i]) == 0:
                output1 = minutes * int(services[i])
    minutes += 1

print('Output1: ' + str(output1))

#Part2
bus_list = []
bus_index = 0
for i in range(0, len(services)):
    if services[i] != 'x':
        bus_list.append([])
        bus_list[bus_index].append(int(services[i]))
        bus_list[bus_index].append(i)
        bus_index += 1

bus_list.sort(reverse=True)

ref_position = bus_list[0][1]
for i in range(0, len(bus_list)):
    bus_list[i][1] = bus_list[i][1] - ref_position

time = 0
increment = 1
for i in range(0, len(bus_list)):
    found_mult = False
    while found_mult == False:
        if (time + bus_list[i][1]) % (bus_list[i][0]) == 0:
            increment *= bus_list[i][0]
            found_mult = True
        else:
            time += increment

output2 = time - ref_position
print('Output2: ' + str(output2))

