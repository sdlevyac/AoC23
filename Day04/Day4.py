filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename,"r").read().split("\n")
sets = []
for line in data:
    #print(line)
    wins = [int(n) for n in line[line.index(": ") + 2:line.index(" | ")].split(" ") if n != ""]
    nums = [int(n) for n in line[line.index("| ") + 2:].split(" ") if n != ""]
    sets.append([wins,nums])
    

scores = []
matches = 0
cards = {i:1 for i in range(1,len(sets) + 1)}


for n, numSet in enumerate(sets):
    wins = numSet[0]
    nums = numSet[1]
    score = 0
    for num in nums:
        if num in wins:
            matches += 1
            if score == 0:
                score = 1
            else:
                score *= 2
    scores.append(score)
    for m in range(matches):
        cards[n + 2 + m] += cards[n+1]
    matches = 0
    
print(sum(scores))   
print(sum(cards.values()))