import pandas

path = r'2020\Puzzle04\Puzzle04_input.txt'
raw_input = pandas.read_csv(path, sep='\n', header=None, skip_blank_lines=False)
mylist = ['']
entry = 0

for i in range(0, len(raw_input)):
    if str(raw_input[0][i]) != 'nan':
        mylist[entry] = mylist[entry] + ' ' + str(raw_input[0][i])
    else:
        entry += 1
        mylist.append('')

#Part1
validcount1 = 0
validcount2 = 0
keys = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

for j in range(0, len(mylist)):
    if all(x in mylist[j] for x in keys):
        validcount1 +=1

        #Part2
        byr_index_i = mylist[j].index(keys[0])
        byr_index_f = mylist[j][byr_index_i:].find(' ')
        if byr_index_f == -1:
            byr = int(mylist[j][byr_index_i+4:])
        else:
            byr = int(mylist[j][byr_index_i+4:byr_index_i+byr_index_f])
        if byr >=1920 and byr <=2002:
            pass
        else:
            continue

        iyr_index_i = mylist[j].index(keys[1])
        iyr_index_f = mylist[j][iyr_index_i:].find(' ')
        if iyr_index_f == -1:
            iyr = int(mylist[j][iyr_index_i+4:])
        else:
            iyr = int(mylist[j][iyr_index_i+4:iyr_index_i+iyr_index_f])
        if iyr >=2010 and iyr <=2020:
            pass
        else:
            continue

        eyr_index_i = mylist[j].index(keys[2])
        eyr_index_f = mylist[j][eyr_index_i:].find(' ')
        if eyr_index_f == -1:
            eyr = int(mylist[j][eyr_index_i+4:])
        else:
            eyr = int(mylist[j][eyr_index_i+4:eyr_index_i+eyr_index_f])
        if eyr >=2020 and eyr <=2030:
            pass
        else:
            continue

        hgt_index_i = mylist[j].index(keys[3])
        hgt_index_f = mylist[j][hgt_index_i:].find(' ')
        if hgt_index_f == -1:
            hgt = mylist[j][hgt_index_i+4:]
        else:
            hgt = mylist[j][hgt_index_i+4:hgt_index_i+hgt_index_f]
        hgt_num = int(hgt[:len(hgt)-2])
        if 'cm' in hgt and hgt_num >=150 and hgt_num <=193:
            pass
        elif 'in' in hgt and hgt_num >=59 and hgt_num <=76:
            pass
        else:
            continue

        hcl_index_i = mylist[j].index(keys[4])
        hcl_index_f = mylist[j][hcl_index_i:].find(' ')
        if hcl_index_f == -1:
            hcl = mylist[j][hcl_index_i+4:]
        else:
            hcl = mylist[j][hcl_index_i+4:hcl_index_i+hcl_index_f]
        allowed_chars = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if len(hcl) == 7 and hcl[0] == '#' and all(char in allowed_chars for char in hcl[1:]):
            pass
        else:
            continue

        ecl_index_i = mylist[j].index(keys[5])
        ecl_index_f = mylist[j][ecl_index_i:].find(' ')
        if ecl_index_f == -1:
            ecl = mylist[j][ecl_index_i+4:]
        else:
            ecl = mylist[j][ecl_index_i+4:ecl_index_i+ecl_index_f]
        allowed_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if any(colour in ecl for colour in allowed_values):
            pass
        else:
            continue

        pid_index_i = mylist[j].index(keys[6])
        pid_index_f = mylist[j][pid_index_i:].find(' ')
        if pid_index_f == -1:
            pid = mylist[j][pid_index_i+4:]
        else:
            pid = mylist[j][pid_index_i+4:pid_index_i+pid_index_f]
        if len(pid) == 9:
            pass
        else:
            continue

        validcount2 +=1

print('Output1: ' + str(validcount1))
print('Output2: ' + str(validcount2))
