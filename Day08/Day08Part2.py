def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

filename = "inputSmall3.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n")

data = [line.split("=") for line in data]
instructions = data[0][0]
data = data[2:]
children = {line[0][:-1] : line[1][2:-1].split(", ") for line in data}
allNodes = [line[0][:-1] for line in data]

startPoints = [allNodes[i] for i in range(len(allNodes)) if allNodes[i][-1] == "A"]

periods = []

for sp in startPoints:
    count = 0
    fullCount = 0
    current = sp
    period = 0
    while period == 0:  
        currentChildren = children[current]
        nextInst = instructions[count]
        count = (count + 1) % len(instructions)
        if nextInst == "L":
            nextNode = currentChildren[0]
        else:
            nextNode = currentChildren[1]
        current = nextNode
        fullCount += 1
        if current[-1] == "Z":
            period = fullCount
    periods.append(period)

while len(periods) != 1:
    newperiods = [lcm(periods[0], periods[1])]
    newperiods.extend(periods[2:])
    periods = [n for n in newperiods]

print(periods[0])