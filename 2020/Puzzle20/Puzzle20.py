import pandas
import numpy

path = r'2020\Puzzle20\Puzzle20_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n')

#print(raw_input[0][1])

ids = []
pieces = []

i = 0
while i < len(raw_input[0]):
    if 'Tile' in raw_input[0][i]:
        id = raw_input[0][i].strip('Tile :')
        ids.append(int(id))
        piece = numpy.empty((10, 10), dtype='str')
        i+=1
    else:
        for j in range(len(piece)):
            for k in range(len(piece[j])):
                piece[j][k] = raw_input[0][i][k]
            i+=1
        pieces.append(piece)

tops = []
tops_back = []
bottoms = []
bottoms_back = []
lefts = []
lefts_back = []
rights = []
rights_back = []

width = len(pieces[0])
for i in range(len(ids)):
    top = ''
    bottom = ''
    left = ''
    right = ''
    for j in range(width):
        top += pieces[i][0][j]
        bottom += pieces[i][width-1][j]
        left += pieces[i][j][0]
        right += pieces[i][j][width-1]
    tops.append(top)
    tops_back.append(top[::-1])
    bottoms.append(bottom)
    bottoms_back.append(bottom[::-1])
    lefts.append(left)
    lefts_back.append(lefts[::-1])
    rights.append(right)
    rights_back.append(right[::-1])

output1 = 1
for i in range(1):
    top = ''
    bottom = ''
    left = ''
    right = ''
    matched_edges = 0
    for j in range(width):
        top += pieces[i][0][j]
        bottom += pieces[i][width-1][j]
        left += pieces[i][j][0]
        right += pieces[i][j][width-1]

    # print(top)
    # print(any(top in list for list in [tops_back, bottoms, bottoms_back, rights, rights_back, lefts, lefts_back]))

    if (any(top in list for list in [tops_back, bottoms, bottoms_back, rights, rights_back, lefts, lefts_back])):
        matched_edges +=1
    if (any(bottom in list for list in [tops, tops_back, bottoms_back, rights, rights_back, lefts, lefts_back])):
        matched_edges +=1
    if (any(right in list for list in [tops, tops_back, bottoms, bottoms_back, rights_back, lefts, lefts_back])):
        matched_edges +=1
    if (any(left in list for list in [tops, tops_back, bottoms_back, rights, rights_back, lefts_back])):
        matched_edges +=1
    print(matched_edges)

A = [1, 2, 3, 4, 5]
B = A.remove(2)
print(A)
