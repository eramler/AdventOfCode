import pandas
import numpy

path = r'2021\Puzzle04\Puzzle04_input.txt'
raw_input = pandas.read_csv(path, header=None, sep='\n', dtype=str)

x = 0
guesses = raw_input[0][x].split(',')
x += 1

size = 5
cards = []

while x < len(raw_input[0]):
    newcard = []
    for l in range(size):
        newcard.append(numpy.array(str(raw_input[0][x+l]).strip().replace('  ', ' ').split(' ')))
    x += size
    cards.append(numpy.array(newcard, dtype=object))

def checkrows(card, guess_set):
    for k in range(size):
        if set(card[k]).issubset(guess_set):
            return True
    return False

def checkcols(card, guess_set):
    for k in range(size):
        if set(card[:,k]).issubset(guess_set):
            return True
    return False

def checkcards(cardlist, guess_set):
    for j in range(len(cardlist)):
        r = checkrows(cardlist[j], guess_set)
        c = checkcols(cardlist[j], guess_set)
        if r or c:
            return True, j
    return False, '-1'

def countunmarked(card, guess_set):
    sum = 0
    for y in range(size):
        for z in range(size):
            value = card[y, z]
            if value not in guess_set:
                sum += int(value)
    return sum

for i in range(len(guesses)):
    guess_set = set(guesses[:i+1])
    check = checkcards(cards, guess_set)
    if check[0] == True:
        winningindex = check[1]
        unmarkedsum = countunmarked(cards[winningindex], guess_set)
        output1 = int(guesses[i]) * unmarkedsum
        break

print('Output1: ' + str(output1))

j = 0
remainingcards = cards.copy()
while len(remainingcards) > 0:
    guess_set2 = set(guesses[:j+1])
    check = checkcards(remainingcards, guess_set2)
    if check[0] == True:
        remainingcards.pop(check[1])
    else:
        j += 1
    if len(remainingcards) == 1:
        lastcard = remainingcards[0]

unmarkedsum2 = countunmarked(lastcard, guess_set2)
output2 = int(guesses[j]) * unmarkedsum2
print('Output2: ' + str(output2))
