filename = "inputsmall.txt"
filename = "inputbig.txt"

data = open(filename).read().split("\n")
data = [list(line) for line in data]

def isempty(thislist):
    return len(thislist) == thislist.count(".")

emptyRows = []
emptyCols = []
for i in range(len(data)):
    if isempty(data[i]):
        emptyRows.append(i)

for j in range(len(data[0])):
    if isempty([row[j] for row in data]):
        emptyCols.append(j)

print(emptyRows)
print(emptyCols)
input()

def expandTwo():
    row = 0
    while row != len(data):
        #print(data[row])
        #input()
        if isempty(data[row]):
            data.insert(row, [c for c in data[row]])
            row += 1
        row += 1

    col = 0
    while col != len(data[0]):
        column = [row[col] for row in data]
        if isempty(column):
            for r in range(len(data)):
                data[r].insert(col, ".")
            col += 1
        col += 1

coords = {}
pairs = {}

answer = 0

count = 1
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "#":
            label = f'{count:03d}'
            data[i][j] = label
            coords[label] = [i,j]
            count += 1
        else:
            data[i][j] = " . "

for row in data:
    print("".join(row))

for coord in coords:
    pairs[coord] = [star for star in coords if star != coord and ((star in pairs and coord not in pairs[star]) or star not in pairs)]

for pair in pairs:
    print(pair, pairs[pair])

def manhattan(start, end):
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    return dx + dy

def manhattanExpanded(start, end, expansion):
    expansion -= 1
    crossedRows = [r for r in emptyRows if min([start[0], end[0]]) < r <= max([start[0], end[0]])]   
    crossedCols = [c for c in emptyCols if min([start[1], end[1]]) < c <= max([start[1], end[1]])]
    dx = abs(start[0] - end[0]) + (len(crossedRows) * (expansion))
    dy = abs(start[1] - end[1]) + (len(crossedCols) * (expansion))
    print(crossedRows, crossedCols)
    return dx + dy

for pair in pairs:
    for star in pairs[pair]:
        print(pair,star)
        distance = manhattanExpanded(coords[pair], coords[star], 1000000)
        print(distance)
        answer += distance

print(answer)