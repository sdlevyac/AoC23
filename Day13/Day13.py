filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n\n")

data = [[list(splitLine) for splitLine in line.split("\n")] for line in data]

def draw(grid):
    output = ""
    for row in grid:
        for col in row:
            output += col
        output += "\n"
    print(output)

ansR = 0
ansC = 0

for g,grid in enumerate(data):
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
            print(f"mirrored about y = {r}, for {r} rows")
            grid.insert(r,["-" for _ in grid[0]])
            draw(grid)
            ansR += r
            anyMirror = True
    if not anyMirror:
        for r in range(1,len(grid)):
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
                print(f"mirrored about y = {r}, for {r} rows")
                grid[r] = ["-" for _ in len(grid[r])]
                draw(grid)
                ansR += r
                anyMirror = True
    if not anyMirror:
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
                print(f"mirrored about x = {c}, for {c} columns")
                ansC += c
                for r in range(len(grid)):
                    grid[r].insert(c, "|")
                draw(grid)
                anyMirror = True
    if not anyMirror:
        for c in range(1,len(grid[0])):
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
                print(f"mirrored about x = {c}, for {c} columns")
                ansC += c
                for r in range(len(grid)):
                    grid[r][c] = "|"
                draw(grid)
                anyMirror = True
    if not anyMirror:
        draw(grid)
        print(g)
        input()
            
ans = (100*ansR) + ansC
print(ans)