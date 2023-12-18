filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n")

data = [line.split(" ") for line in data]
data = [[line[0], int(line[1]), line[2]] for line in data]

def draw(grid):
    output = ""
    for row in grid:
        output += "".join(row) + "\n"
    print(output)

directions = {"U":[-1,0],
              "D":[1,0],
              "L":[0,-1],
              "R":[0,1]}

x = 1
xMin = 0
xMax = 0
y = 1
yMin = 0
yMax = 0

for line in data:
    if line[0] == "U":
        x -= line[1]
    elif line[0] == "D":
        x += line[1]
    elif line[0] == "L":
        y -= line[1]
    elif line[0] == "R":
        y += line[1]
    if x > xMax:
        xMax = x
    if x < xMin:
        xMin = x
    if y > yMax:
        yMax = y
    if y < yMin:
        yMin = y

grid = [["." for y in range(yMin,yMax+1)] for x in range(xMin,xMax+1)]

x = 1-xMin 
y = 1-yMin

for line in data:
    direction = directions[line[0]]
    magnitude = line[1]
    for m in range(magnitude):
        grid[x][y] = "#"
        x += direction[0]
        y += direction[1]
    #draw(grid)
    #input()

start = (1-xMin + 1,1-yMin + 1)
toVisit = [start]


while len(toVisit) != 0:
    current = toVisit.pop(0)
    grid[current[0]][current[1]] = "#"
    for d in [[1,0],[-1,0],[0,1],[0,-1]]:
        dx = current[0] + d[0]
        dy = current[1] + d[1]
        if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy] == ".":
            if (dx,dy) not in toVisit:
                toVisit.append((dx,dy))

#draw(grid)
print(sum([line.count("#") for line in grid]))