import pandas

path = r'2020\Puzzle14\Puzzle14_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

mylist = raw_input[0].tolist()

#Part1
mem1 = {}

for i in range(0, len(mylist)):
    if mylist[i][:4] == 'mask':
        mask = str(mylist[i][7:])
    else:
        mem_i = mylist[i].find('[') + 1
        mem_f = mylist[i].find(']')
        mem_index = mylist[i][mem_i:mem_f]

        value_i = mylist[i].find('=') + 2
        value = int(mylist[i][value_i:])

        bin_value = str('{0:036b}'.format(value))
        masked_value = ''
        for j in range(0, len(mask)):
            if mask[j] == 'X':
                masked_value += bin_value[j]
            elif mask[j] != 'X':
                masked_value += mask[j]
            
        new_value = int(masked_value, 2)
        mem1[mem_index] = new_value

output1 = sum(mem1.values())
print('Output1: ' + str(output1))

#Part2
mem2 = {}

for i in range(0, len(mylist)):
    if mylist[i][:4] == 'mask':
        mask = str(mylist[i][7:])
        # print(mask)
    else:
        mem_i = mylist[i].find('[') + 1
        mem_f = mylist[i].find(']')
        mem_index = int(mylist[i][mem_i:mem_f])

        value_i = mylist[i].find('=') + 2
        value = int(mylist[i][value_i:])

        bin_mem = str('{0:036b}'.format(mem_index))
        masked_mems = []
        float_vals = []
        float_ind = 0
        for k in range(0, 2 ** mask.count('X')):
            masked_mems.append('')
            float_vals.append(str('{0:0{num_floats}b}'.format(k, num_floats=mask.count('X'))))
        for j in range(0, len(mask)):
            for l in range(0, len(masked_mems)):
                if mask[j] == 'X':
                    masked_mems[l] += float_vals[l][float_ind]
                elif mask[j] == '1':
                    masked_mems[l] += mask[j]
                elif mask[j] == '0':
                    masked_mems[l] += bin_mem[j]
            if mask[j] == 'X':
                float_ind += 1
        
        for m in range(0, len(masked_mems)):
            new_mem = int(masked_mems[m], 2)
            mem2[new_mem] = value

output2 = sum(mem2.values())
print('Output2: ' + str(output2))
