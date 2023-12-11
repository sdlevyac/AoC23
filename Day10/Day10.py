import os

filename = "inputSmall1.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n")
data = [list(line) for line in data]

print("part 01...")

lakes = []
inLake = []

def draw(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print()
    print("~" * len(data))
    print()
    
def getNeighboursLake(x, y, grid):
    neighbours = []
    for d in [[1,0],[-1,0],[0,1],[0,-1]]:#, [1,1], [1,-1], [-1,1], [-1,-1]]:
        dx = d[0]
        dy = d[1]
        if (dx != 0 or dy != 0) and 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] == ".":
            neighbours.append([x + dx, y + dy])
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
    ns = [n for n in ns if 0 <= n[0] < len(data) and 0 <= n[1] < len(data[0])]
    return ns


distances = [[-1 for _ in line] for line in data]

start = [-1, -1]
keepChecking = True
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "S":
            start = [i, j]
            keepChecking = False
            break
    if not keepChecking: break
        
toVisit = [[start[0], start[1]]]
distances[start[0]][start[1]] = 0
visited = []

fixStart(start)

render = [[" " for _ in line] for line in data]


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
    #draw(render)

swaps = {"-":"─",
         "|":"│",
         "F":"┌",
         "J":"┘",
         "L":"└",
         "7":"┐",
         "X":"X"}

render[start[0]][start[1]] = data[start[0]][start[1]]
render = [[swaps[cell] if cell != " " else "." for cell in line] for line in render]
#render[start[0]][start[1]] = "#"
draw(render)

print(max([max(line) for line in distances]))
print("part 02...")

def explore(x, y, grid):
    thisLake = [[x, y]]
    toExplore = [[x, y]]
    explored = []
    while len(toExplore) != 0:
        #print(len(toExplore),len(explored),end="\t")
        current = toExplore.pop(0)
        explored.append(current)
        neighbours = getNeighboursLake(current[0], current[1], grid)
        toExplore.extend([n for n in neighbours if grid[n[0]][n[1]] == "." and n not in toExplore and n not in explored])
    lakes.append(len(explored))
    inLake.extend(explored)
    for coord in explored:
        grid[coord[0]][coord[1]] = symbol[0]
    print()

symbol = ["~"]
# explore(0,0, render)

# for i in range(len(render)):
#     for j in range(len(render)):
#         if render[i][j] == "." and [i,j] not in inLake:
#             print(f"exploring lake at {[i,j]}...")
#             explore(i, j, render)
 
            
# draw(render)
# lakes = sorted(lakes)
# lakes = lakes[:-1]
# print(sum(lakes))
 
# answer = sum([line.count(".") for line in render])
# print(answer)

bigRender = [["." for col in range(len(render[0]) * 3)] for row in range(len(render) * 3)]

eStart = [start[0] - 20, start[1]]
eStart = [eStart[0] * 3, eStart[1] * 3]
eStart = [0,0]

for x in range(len(render)):
    for y in range(len(render[0])):
        midX = (x * 3) + 1
        midY = (y * 3) + 1
        if render[x][y] != ".":
            if render[x][y] == "─":
                bigRender[midX - 1][midY - 1] = "."
                bigRender[midX][midY - 1] = "─"
                bigRender[midX + 1][midY - 1] = "."
                bigRender[midX - 1][midY] = "."
                bigRender[midX][midY] = "─"
                bigRender[midX + 1][midY] = "."
                bigRender[midX - 1][midY + 1] = "."
                bigRender[midX][midY + 1] = "─"
                bigRender[midX + 1][midY + 1] = "."
            if render[x][y] == "│":
                bigRender[midX - 1][midY - 1] = "."
                bigRender[midX][midY - 1] = "."
                bigRender[midX + 1][midY - 1] = "."
                bigRender[midX - 1][midY] = "│"
                bigRender[midX][midY] = "│"
                bigRender[midX + 1][midY] = "│"
                bigRender[midX - 1][midY + 1] = "."
                bigRender[midX][midY + 1] = "."
                bigRender[midX + 1][midY + 1] = "."
            if render[x][y] == "┌":
                bigRender[midX - 1][midY - 1] = "."
                bigRender[midX][midY - 1] = "."
                bigRender[midX + 1][midY - 1] = "."
                bigRender[midX - 1][midY] = "."
                bigRender[midX][midY] = "┌"
                bigRender[midX + 1][midY] = "│"
                bigRender[midX - 1][midY + 1] = "."
                bigRender[midX][midY + 1] = "─"
                bigRender[midX + 1][midY + 1] = "."
            if render[x][y] == "┘":
                bigRender[midX - 1][midY - 1] = "."
                bigRender[midX][midY - 1] = "─"
                bigRender[midX + 1][midY - 1] = "."
                bigRender[midX - 1][midY] = "│"
                bigRender[midX][midY] = "┘"
                bigRender[midX + 1][midY] = "."
                bigRender[midX - 1][midY + 1] = "."
                bigRender[midX][midY + 1] = "."
                bigRender[midX + 1][midY + 1] = "."
            if render[x][y] == "└":
                bigRender[midX - 1][midY - 1] = "."
                bigRender[midX][midY - 1] = "."
                bigRender[midX + 1][midY - 1] = "."
                bigRender[midX - 1][midY] = "│"
                bigRender[midX][midY] = "└"
                bigRender[midX + 1][midY] = "."
                bigRender[midX - 1][midY + 1] = "."
                bigRender[midX][midY + 1] = "─"
                bigRender[midX + 1][midY + 1] = "."
            if render[x][y] == "┐":
                bigRender[midX - 1][midY - 1] = "."
                bigRender[midX][midY - 1] = "─"
                bigRender[midX + 1][midY - 1] = "."
                bigRender[midX - 1][midY] = "."
                bigRender[midX][midY] = "┐"
                bigRender[midX + 1][midY] = "│"
                bigRender[midX - 1][midY + 1] = "."
                bigRender[midX][midY + 1] = "."
                bigRender[midX + 1][midY + 1] = "."
            if render[x][y] == "X":
                bigRender[midX - 1][midY - 1] = "."
                bigRender[midX][midY - 1] = "."
                bigRender[midX + 1][midY - 1] = "."
                bigRender[midX - 1][midY] = "X"
                bigRender[midX][midY] = "X"
                bigRender[midX + 1][midY] = "."
                bigRender[midX - 1][midY + 1] = "."
                bigRender[midX][midY + 1] = "X"
                bigRender[midX + 1][midY + 1] = "."
        else:
                bigRender[midX - 1][midY - 1] = "."
                bigRender[midX][midY - 1] = "."
                bigRender[midX + 1][midY - 1] = "."
                bigRender[midX - 1][midY] = "."
                bigRender[midX][midY] = "."
                bigRender[midX + 1][midY] = "."
                bigRender[midX - 1][midY + 1] = "."
                bigRender[midX][midY + 1] = "."
                bigRender[midX + 1][midY + 1] = "."
      
   
                

draw(bigRender)
input()
explore(eStart[0],eStart[1],bigRender)
draw(bigRender)

smallRender = [['.' for y in range(int(len(bigRender[0])/3))] for x in range(int(len(bigRender)/3))]
for x in range(len(smallRender)):
    for y in range(len(smallRender[x])):
        midX = (x * 3) + 1
        midY = (y * 3) + 1
        smallRender[x][y] = bigRender[midX][midY]


draw(smallRender)
print(sum([line.count(".") for line in smallRender]))