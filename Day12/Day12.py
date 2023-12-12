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

data = expandData(data)

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