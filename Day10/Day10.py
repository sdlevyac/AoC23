import os

filename = "inputSmall1.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n")
data = [list(line) for line in data]

def draw(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print()
    print("~" * len(data))
    print()

for line in data:
    for col in line:
        print(col, end="")
    print()
    
def getNeighbours(x, y):
    neighbours = []
    for d in [[1,0], [-1,0], [0,1], [0,-1]]:
        this = data[x][y]         
        if 0 <= x + d[0] < len(data) and 0 <= y + d[1] < len(data):
            neighbours.append([x + d[0], y + d[1]])
    return neighbours

validNeighbours = {"F" : [[0, 1], [1, 0]],
                   "|" : [[-1, 0], [1, 0]],
                   "-" : [[0, 1], [0, -1]],
                   "L" : [[-1, 0], [0, 1]],
                   "J" : [[-1, 0], [0, -1]],
                   "7" : [[0, -1], [1, 0]]}

def fixStart(start):
    data[start[0]][start[1]] = "L"


def getNeighboursPipes(x, y):
    #x+ is down, x- is up
    #y+ is left, y- is right
    ns = validNeighbours[data[x][y]]
    ns = [[n[0] + x, n[1] + y] for n in ns]
    ns = [n for n in ns if 0 <= n[0] < len(data) and 0 <= n[1] < len(data)]
    return ns

distances = [[-1 for _ in line] for line in data]
render = [[" " for _ in line] for line in data]

start = [-1, -1]
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            start = [i, j]
            break
        
toVisit = [[start[0], start[1]]]
distances[start[0]][start[1]] = 0
visited = []

fixStart(start)

render[start[0]][start[1]] = "#"

while len(toVisit) != 0:
    current = toVisit.pop(0)
    visited.append(current)
    # neighbours = getNeighbours(current[0], current[1])
    neighbours = getNeighboursPipes(current[0], current[1])
    for neighbour in neighbours:
        if(distances[neighbour[0]][neighbour[1]] == -1 or distances[current[0]][current[1]] + 1 < distances[neighbour[0]][neighbour[1]]):
            distances[neighbour[0]][neighbour[1]] = distances[current[0]][current[1]] + 1
            render[neighbour[0]][neighbour[1]] = data[neighbour[0]][neighbour[1]]
            
    toVisit.extend(n for n in neighbours if n not in toVisit and n not in visited)
    # os.system('cls')
    # draw(render)

draw(render)
print(max([max(line) for line in distances]))