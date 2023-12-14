filename = "inputSmall.txt"
filename = "inputBig.txt"

def draw(grid):
    output = ""
    for row in grid:
        for col in row:
            output += col
        output += "\n"
    print(output)

def copy2dList(source):
    copy = [[source[i][j] for j in range(len(source[i]))] for i in range(len(source))]
    return copy

data = open(filename).read().split("\n")
data = [list(line) for line in data]

draw(data)

def totalLoad(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                ans += len(grid) - i
    return ans

def tiltNorth(grid):

    tilt = True
    while tilt:
        changes = 0
        copyGrid = copy2dList(grid)
        for i in range(1,len(grid)):
            for j in range(0,len(grid)):
                if grid[i][j] == "O" and grid[i-1][j] == ".":
                    copyGrid[i][j] = "."
                    copyGrid[i-1][j] = "O"
                    changes += 1
        #draw(copyGrid)
        print(f"{changes} changes")
        grid = copy2dList(copyGrid)
        #input()
        if changes == 0:
            tilt = False
    return grid

data = tiltNorth(data)
draw(data)
answer = totalLoad(data)
print(answer)