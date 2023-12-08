filename = "inputSmall1.txt"
filename = "inputSmall2.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n")

data = [line.split("=") for line in data]
instructions = data[0][0]
data = data[2:]
children = {line[0][:-1] : line[1][2:-1].split(", ") for line in data}
allNodes = [line[0][:-1] for line in data]

current = "AAA"
currents = [node for node in allNodes if node[-1] == "A"]
print(currents)
input()
count = 0
fullCount = 0
while current != "ZZZ":  
    currentChildren = children[current]
    nextInst = instructions[count]
    print(f"at {current} with children {currentChildren}, going {nextInst}")
    count = (count + 1) % len(instructions)

    if nextInst == "L":
        nextNode = currentChildren[0]
    else:
        nextNode = currentChildren[1]
    print(f"\tto {nextNode}")
    #input()
    current = nextNode
    fullCount += 1
print(fullCount)