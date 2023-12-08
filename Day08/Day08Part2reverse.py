filename = "inputSmall3.txt"
#filename = "inputBig.txt"

import datetime as dt

data = open(filename).read().split("\n")
instructions = data[0]
data = data[2:]

data = [line.split(" = ") for line in data]

data = [[line[0], line[1][1:-1].split(", ")] for line in data]

rootsR = {line[1][1] : [line[0], "R"] for line in data}
roots = {line[1][0] : [line[0], "L"] for line in data}

roots.update(rootsR)

for node in roots:
    print(node, roots[node])