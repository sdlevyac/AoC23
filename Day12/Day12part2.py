filename = "inputSmall.txt"
#filename = "inputBig.txt"

def expandData(smallData):
    expandedData = [[((line[0] + "?")*5)[:-1], ((line[1] + ",")*5)[:-1]] for line in smallData]
    return expandedData

def createPattern(pattern):
    created = ["~"]
    created.extend(list("~".join(["#"*p for p in pattern])))
    created.append("~")
    return created

data = open(filename).read().split("\n")
data = [line.split(" ") for line in data]
#data = expandData(data)
data = [[line[0],[int(n) for n in line[1].split(",")]] for line in data]
data = [[line[0], createPattern(line[1])] for line in data]

for line in data:
    split = line[0].split(".")
    print(split)
    input()


