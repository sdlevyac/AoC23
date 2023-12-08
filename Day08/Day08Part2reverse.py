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

current = "AAA"
currents = [node for node in allNodes if node[-1] == "A"]
startIndices = [i for i in range(len(allNodes)) if allNodes[i][-1] == "A"]
startPoints = [allNodes[i] for i in startIndices]


allLoops = []

for sp in startPoints:
    count = 0
    fullCount = 0

    current = sp

    loops = []

    while len(loops) != 1:  
        currentChildren = children[current]
        nextInst = instructions[count]
        #print(f"at {current} with children {currentChildren}, going {nextInst}")
        count = (count + 1) % len(instructions)

        if nextInst == "L":
            nextNode = currentChildren[0]
        else:
            nextNode = currentChildren[1]
        #print(f"\tto {nextNode}")
        #input()
        current = nextNode
        fullCount += 1
        if current[-1] == "Z":
            loops.append(fullCount)
            #print(current, fullCount, loops)
            #input()
    allLoops.append(loops)
#print(allLoops)
#print("#"*100)

nums = [loop[0] for loop in allLoops]
#print(nums)

answer = lcm(nums[0], lcm(nums[1], lcm(nums[2], lcm(nums[3], lcm(nums[4], nums[5])))))
print(answer)