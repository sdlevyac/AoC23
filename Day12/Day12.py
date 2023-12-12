filename = "inputSmall.txt"
#filename = "inputBig.txt"

data = open(filename).read().split("\n")
data = [line.split(" ") for line in data]

options = [".","#"]

def match(springs, pattern):
    if "?" in springs:
        return False
    processing = [group for group in "".join(springs).split(".") if group != ""]
    processing = [len(g) for g in processing]
    if len(processing) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] != processing[i]:
            return False
    return True

def permute(p, thisPattern, permutations = []):
    if "?" in p:
        index = p.index("?")
        for option in options:
            pCopy = [c for c in p]
            pCopy[index] = option
            print(pCopy)
            permutations.extend(permute(pCopy, thisPattern, [pCopy]))
            #permutations.extend()
    return permutations#[perm for perm in permutations if match(p, thisPattern)]

def expandData(smallData):
    expandedData = [[((line[0] + "?")*5)[:-1], ((line[1] + ",")*5)[:-1]] for line in smallData]
    return expandedData

#data = expandData(data)
#working out all permutations and then deciding which ones are valid is far too time intensive
#instead we need to work out all the valid ways of representing the pattern and then apply these
#valid patterns to the initial data
#as it stands, this method is ~ok~ for part 1 but even the small data input takes an unreasonable length of time
#for part 2 - this has at least been good for practicing generating permutations based on certain rules

answer = 0
for i, line in enumerate(data):
    #print(line[0])
    #input()
    theseSprings = permute(line[0], [int(n) for n in line[1].split(",")], [])#[perm for perm in permute(line[0], []) if "?" not in perm]
    #for spring in theseSprings:
    theseSprings = [spring for spring in theseSprings if match(spring, [int(n) for n in line[1].split(",")])]
    #    print(spring)
    print(i,"/",len(data),line[0], len(theseSprings), answer)
    answer += len(theseSprings)
    theseSprings.clear()
    #input()

print(answer)