import pandas
import numpy

# Get and process input
path = r'2023/04/04_input.txt'
raw_input = pandas.read_csv(path, header=None, skip_blank_lines=False)[0]

test = raw_input[0]

# Define functions
def ProcessCard(card: str) -> (set[int], set[int]):
    RemoveCardName = card.split(':')[1]
    SplitNums = RemoveCardName.split('|')
    WinningNums = set([int(num) for num in SplitNums[0].split(' ') if num.strip()])
    CardNums = set([int(num) for num in SplitNums[1].split(' ') if num.strip()])
    return CardNums, WinningNums

def CountWinningNums(Nums: set[int], WinningNums: set[int]) -> int:
    Winners = Nums.intersection(WinningNums)
    return len(Winners)

def CalcCardScore(WinningNums: int) -> int:
    if WinningNums == 0:
        Score = 0
    else:
        Score = 2 ** (WinningNums-1)
    return Score

# Iterate through scratchcards
NumCards = len(raw_input)
Output1 = 0
CardCounts = [1 for i in range(NumCards)]
for i in range(NumCards):
    CardNums, WinningNums = ProcessCard(raw_input[i])
    NumWinners = CountWinningNums(CardNums, WinningNums)
    # Part 1
    CardScore = CalcCardScore(NumWinners)
    Output1 += CardScore
    # Part 2
    for j in range(NumWinners):
        CardCounts[i + j + 1] += CardCounts[i]

Output2 = sum(CardCounts)

print('Output1: ' + str(Output1))
print('Output2: ' + str(Output2))
