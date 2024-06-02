import pandas
import numpy

path = r'2023/01/01_input.txt'
raw_input = pandas.read_csv(path, header=None, skip_blank_lines=False)[0]

calibration1 = []
calibration2 = []
DigitLookup = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
DictKeys = list(DigitLookup.keys())

for i in range(len(raw_input)):
    s = raw_input[i]
    stringLen = len(s)
    firstDigit = ""
    lastDigit = ""
    for j in range(len(s)):
        if s[j].isdigit() and firstDigit == "":
            firstDigit = s[j]
            firstDigitPos = j
        rpos = stringLen - 1 - j
        if s[rpos].isdigit() and lastDigit == "":
            lastDigit = s[rpos]
            lastDigitPos = rpos

    calibration1.append(int(firstDigit + lastDigit))

    # Check for string digits for Part 2
    for k in range(len(DictKeys)):
        thisStrDigit = DictKeys[k]
        if thisStrDigit in s:
            strDigitLPos = s.index(thisStrDigit)
            strDigitRPos = s.rindex(thisStrDigit)
            if strDigitLPos < firstDigitPos:
                firstDigit = DigitLookup[thisStrDigit]
                firstDigitPos = strDigitLPos
            if strDigitRPos > lastDigitPos:
                lastDigit = DigitLookup[thisStrDigit]
                lastDigitPos = strDigitRPos
    
    calibration2.append(int(firstDigit + lastDigit))

TotalCalibration1 = sum(calibration1)
TotalCalibration2 = sum(calibration2)
print("Part 1: " + str(TotalCalibration1))
print("Part 2: " + str(TotalCalibration2))
