filename = "inputSmall3.txt"
#filename = "inputBig.txt"

import datetime as dt

def over(currents):
    for node in currents:
        if node[-1] != "Z":
            return False
    return True

start = dt.datetime.now()

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

lasts = "A" * len(currents)

target = "Z" * len(currents)

while lasts != target:  
    nextInst = instructions[count]  
    count = (count + 1) % len(instructions)

    if nextInst == "L":
        currents = [children[current][0] for current in currents]
    else:
        currents = [children[current][1] for current in currents]
    #print(currents)
    #input()
    fullCount += 1
    if fullCount % 100000 == 0:
        print(f"after {fullCount} steps:")
        print("\t",currents)
        print("\t",lasts)
    lasts = "".join(current[-1] for current in currents)
    print(lasts)
print(fullCount)
print(dt.datetime.now() - start)