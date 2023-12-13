filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n\n")

data = [[list(splitLine) for splitLine in line.split("\n")] for line in data]

def findMirror(grid):
    anyMirror = False
    for r in range(1,len(grid)):
        tr = r - 1
        br = r
        mirror = True
        #tr = top row, br = bottom row
        while tr >= 0 and br < len(grid) and mirror:
            if "".join(grid[tr]) != "".join(grid[br]):
                mirror = False
            else:
                #print(f"row {br} matches row {tr}")
                tr -= 1
                br += 1
        if mirror:
            #print(f"mirrored about y = {r}, for {r} rows")
            return 100*r
    for r in range(1,len(grid) - 1):
        tr = r - 1
        br = r + 1
        while tr >= 0 and br < len(grid) and mirror:
            if "".join(grid[tr]) != "".join(grid[br]):
                mirror = False
            else:
                #print(f"row {br} matches row {tr}")
                tr -= 1
                br += 1
        if mirror:
            #print(f"mirrored about y = {r}, for {r} rows")
            return 100*r
    for c in range(1,len(grid[0])):
        lc = c - 1
        rc = c
        mirror = True
            #lc = left column, rc = right column
        while lc >= 0 and rc < len(grid[0]) and mirror:
            if "".join([row[lc] for row in grid]) != "".join([row[rc] for row in grid]):
                mirror = False
            else:
                #print(f"column {lc} matches column {rc}")
                lc -= 1
                rc += 1
        if mirror:
            #print(f"mirrored about x = {c}, for {c} columns")
            return c
    for c in range(1,len(grid[0]) - 1):
        lc = c - 1
        rc = c + 1
        mirror = True
            #lc = left column, rc = right column
        while lc >= 0 and rc < len(grid[0]) and mirror:
            if "".join([row[lc] for row in grid]) != "".join([row[rc] for row in grid]):
                mirror = False
            else:
                #print(f"column {lc} matches column {rc}")
                lc -= 1
                rc += 1
        if mirror:
            #print(f"mirrored about x = {c}, for {c} columns")
            return c
    return 0

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

answer = 0
for g, grid in enumerate(data):
    original = findMirror(grid)
    print(f"original mirror value = {original}")
    found = False
    for i in range(len(grid)):
        if found: break
        for j in range(len(grid[i])):
            smudgedGrid = smudge(grid, i, j)
            #draw(grid)
            #draw(smudgedGrid)
            #print(f"grid {g}: smudge at ({i},{j})")
            smudged = findMirror(smudgedGrid)
            if smudged != 0 and original != smudged:
                print(f"\tsmudged mirror value = {smudged}")
                answer += smudged
                #input()
                found = True
                break
    if not found:
        print(f"\t\t\tno smudged mirror found for grid {g}: ")
        draw(grid)
        input()
    else:
        print(f"smudged mirror found for grid {g}")
           
print(answer)

# not finding a smudged mirror for some grids

# e.g.

# .##......
# ###.####.
# ##.##...#
# ..###..##
# ...##..##
# #..#.##.#
# ..#......
# .##..##..
# .##..##..