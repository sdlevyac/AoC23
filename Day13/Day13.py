filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n\n")

data = [[list(splitLine) for splitLine in line.split("\n")] for line in data]

def findMirror(grid):
    mirrors = []
    for r in range(1,len(grid)):
        tr = r - 1
        br = r
        mirror = True
        while tr >= 0 and br < len(grid) and mirror:
            if "".join(grid[tr]) != "".join(grid[br]):
                mirror = False
            else:
                tr -= 1
                br += 1
        if mirror:
            mirrors.append(100*r)
    for r in range(1,len(grid) - 1):
        tr = r - 1
        br = r + 1
        while tr >= 0 and br < len(grid) and mirror:
            if "".join(grid[tr]) != "".join(grid[br]):
                mirror = False
            else:
                tr -= 1
                br += 1
        if mirror:
            mirrors.append(100*r)
    for c in range(1,len(grid[0])):
        lc = c - 1
        rc = c
        mirror = True
        while lc >= 0 and rc < len(grid[0]) and mirror:
            if "".join([row[lc] for row in grid]) != "".join([row[rc] for row in grid]):
                mirror = False
            else:
                lc -= 1
                rc += 1
        if mirror:
            mirrors.append(c)
    for c in range(1,len(grid[0]) - 1):
        lc = c - 1
        rc = c + 1
        mirror = True
        while lc >= 0 and rc < len(grid[0]) and mirror:
            if "".join([row[lc] for row in grid]) != "".join([row[rc] for row in grid]):
                mirror = False
            else:
                lc -= 1
                rc += 1
        if mirror:
            mirrors.append(c)
    return mirrors

def draw(grid):
    output = ""
    for row in grid:
        for col in row:
            output += col
        output += "\n"
    print(output)
    
def smudge(cleanGrid, x, y):
    smudgedGrid = [["" for c in r] for r in cleanGrid]
    for i in range(len(cleanGrid)):
        for j in range(len(cleanGrid[i])):
            if i == x and j == y:               
                smudgedGrid[i][j] = "#" if cleanGrid[i][j] == "." else "."
            else:
                smudgedGrid[i][j] = cleanGrid[i][j]
    return smudgedGrid


for part2 in [False, True]:
    answer = 0
    for g, grid in enumerate(data):
        original = findMirror(grid)[0]
        if part2:
            smudgedVals = []
            found = False
            for i in range(len(grid)):
                if found: break
                for j in range(len(grid[i])):
                    smudgedGrid = smudge(grid, i, j)
                    smudged = [val for val in findMirror(smudgedGrid) if val != original]
                    smudgedVals.extend(smudged)
            if len(smudgedVals) > 2:
                print(smudgedVals)
                draw(grid)
            answer += max(smudgedVals)
        else:
            answer += original
           
    print(answer)