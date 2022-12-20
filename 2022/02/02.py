import pandas
import numpy

colnames = ["opp", "response"]

path = r'2022/02/02_input.txt'
raw_input = pandas.read_csv(path, header=None, sep=" ", names=colnames)

shapeScores = {"Rock":1, "Paper":2, "Scissors":3}
resultScores = {"Win": 6, "Draw": 3, "Loss":0}
meaning1 = {"X": "Rock", "Y":"Paper", "Z":"Scissors"}

def rps1(opp, response):
    score = 0
    score += shapeScores[meaning1[response]]
    if (opp == "A" and response == "Y") or (opp =="B" and response == "Z") or (opp == "C" and response =="X"):
        score += resultScores["Win"]
    elif (opp == "A" and response == "X") or (opp =="B" and response == "Y") or (opp == "C" and response =="Z"):
        score += resultScores["Draw"]
    elif (opp == "A" and response == "Z") or (opp =="B" and response == "X") or (opp == "C" and response =="Y"):
        score += resultScores["Loss"]
    return score

output1 = 0
for i in range(len(raw_input["opp"])):
    output1 += rps1(raw_input["opp"][i], raw_input["response"][i])

print("Output1: " + str(output1))

meaning2 = {"X":"Loss", "Y":"Draw", "Z":"Win"}

def rps2(opp, response):
    score = 0
    score += resultScores[meaning2[response]]
    if (opp == "A" and response == "Y") or (opp =="B" and response == "X") or (opp == "C" and response =="Z"):
        score += shapeScores["Rock"]
    elif (opp == "A" and response == "Z") or (opp =="B" and response == "Y") or (opp == "C" and response =="X"):
        score += shapeScores["Paper"]
    elif (opp == "A" and response == "X") or (opp =="B" and response == "Z") or (opp == "C" and response =="Y"):
        score += shapeScores["Scissors"]
    return score

output2 = 0
for i in range(len(raw_input["opp"])):
    output2 += rps2(raw_input["opp"][i], raw_input["response"][i])

print("Output2: " + str(output2))