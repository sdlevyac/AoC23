filename = "inputSmall.txt"
filename = "inputBig.txt"

def allZeroes(seq):
    for n in seq:
        if n != 0:
            return False
    return True

data = open(filename).read().split("\n")
data = [[int(n) for n in line.split(" ")] for line in data]

answer = 0
answer2 = 0

for sequence in data:
    reductions = [sequence]
    reduced = [n for n in sequence]
    while not allZeroes(reduced):
        reduced = [reduced[i+1] - reduced[i] for i in range(0, len(reduced) - 1)]
        reductions.append(reduced)
    reductions = reductions[-2::-1]
    reductions[0].append(reductions[0][-1])
    reductions[0].insert(0, reductions[0][0])
    for i in range(1,len(reductions)):
        reductions[i].append(reductions[i][-1] + reductions[i-1][-1])
        reductions[i].insert(0,reductions[i][0] - reductions[i-1][0])
    answer += reductions[-1][-1]
    answer2 += reductions[-1][0]
    
print(answer, answer2)