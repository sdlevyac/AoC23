filename = "inputSmall.txt"
#filename = "inputBig.txt"
data = open(filename).read().split("\n")
grid = [list(line) for line in data]


def draw(grid):
    for row in grid:
        print("".join(row))
    print("~"*len(grid[0]))

draw(grid)
places = {}
placesTotal = {}

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i,j)
        places[(i,j)] = 0
        placesTotal[(i,j)] = 0

print(start)
gridBuffer = [list(line) for line in data]
draw(gridBuffer)
for d in [(1,0),(0,1),(-1,0),(0,-1)]:
    dx = d[0] + start[0]
    dy = d[1] + start[1]
    if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] != "#":
        gridBuffer[dx][dy] = "O"
        places[(dx,dy)] = 1
        placesTotal[(dx,dy)] = 1

draw(gridBuffer)
input()
limit = 200
for s in range(2,limit-1):
    grid = [[gridBuffer[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    gridBuffer = [list(line) for line in data]
    steps = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                steps.append((i,j))
            else:
                places[(i,j)] = 0


    for step in steps:
        for d in [(0,1)]:#(1,0),(0,1),(-1,0),(0,-1)]:
            dxr = (d[0] + step[0])
            dyr = (d[1] + step[1])
            dx = (d[0] + step[0]) % len(data) 
            dy = (d[1] + step[1]) % len(data[0])
            if grid[dx][dy] != "#":
                print(dxr,dyr)
                gridBuffer[dx][dy] = "O"
                places[(dx,dy)] += places[(step[0], step[1])]
                placesTotal[(dxr,dyr)] = places[(step[0], step[1])]
            #if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] != "#":
            #    gridBuffer[dx][dy] = "O"
    grid = [[gridBuffer[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "O":
                places[(i,j)] = 0


    draw(gridBuffer)
    print(s)
    print(sum([line.count("O") for line in gridBuffer]))
    print([(place, places[place]) for place in places if places[place] != 0])
    print(sum([places[place] for place in places]))
    input()