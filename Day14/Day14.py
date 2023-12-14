filename = "inputSmall.txt"
#filename = "inputBig.txt"

def compress(grid):
    return("\n".join(["".join(line) for line in grid]))

def decompress(dataString):
    return [list(line) for line in dataString.split("\n")]

def compare(source, alt):
    for i in range(len(source)):
        for j in range(len(source[i])):
            if source[i][j] != alt[i][j]:
                return False
    return True

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

#draw(data)

def totalLoad(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                ans += len(grid) - i
    return ans

def tiltGeneral(grid,dx,dy):
    totalChanges = 0
    tilt = True
    while tilt:
        changes = 0
        copyGrid = copy2dList(grid)
        if dx == -1:
            iRange = range(1,len(grid))
        elif dx == 1:
            iRange = range(0,len(grid)-1)
        else:
            iRange = range(0,len(grid))
        if dy == -1:
            jRange = range(1,len(grid[0]))
        elif dy == 1:
            jRange = range(0,len(grid[0])-1)
        else:
            jRange = range(0,len(grid[0]))
        for i in iRange:
            for j in jRange:
                if grid[i][j] == "O" and grid[i+dx][j+dy] == ".":
                    copyGrid[i][j] = "."
                    copyGrid[i+dx][j+dy] = "O"
                    changes += 1
        grid = copy2dList(copyGrid)
        totalChanges += changes
        if changes == 0:
            tilt = False
    return grid, totalChanges

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
        #print(f"{changes} changes")
        grid = copy2dList(copyGrid)
        #input()
        if changes == 0:
            tilt = False
    return grid

initialData = copy2dList(data)

#part1
data = tiltNorth(data)
answer = totalLoad(data)
print(answer)

states = {}

#part2
data = copy2dList(initialData)
cycleLength = -1
cycleStates = []
limit = 1000000000
for i in range(limit):
    #print(f"cycle {i} / 1000000000")
    initialState = copy2dList(data)
    initialStateCompressed = compress(initialState)
    if initialStateCompressed in states:
        if len(cycleStates) == 0:
            cycleStates.append(initialStateCompressed)
        else:
            if initialStateCompressed in cycleStates:
                #print(f"cycle of length {len(cycleStates)}")
                loads = [totalLoad(decompress(cycleState)) for cycleState in cycleStates]
                #print(loads)
                #print(f"{i} cycles")
                #print(f"loop of {len(cycleStates)} states")
                #print(f"{limit - i} cycles remaining")
                #print(f"{(limit-i)%len(cycleStates)}")
                print(loads[(limit-i)%len(cycleStates)])
                break            
            else:
                cycleLength += 1
                cycleStates.append(initialStateCompressed)
        #print("state has already been computed")
        dataCompressed = states[initialStateCompressed]
        data = decompress(dataCompressed)
        #input()
        continue
    #print(initialStateCompressed)
    #print(f"cycle {i} / 1000000000")
    for cycle in [[-1,0],[0,-1],[1,0],[0,1]]:               
        data, changes = tiltGeneral(data,cycle[0],cycle[1])
    dataCompressed = compress(data)
    states[initialStateCompressed] = dataCompressed
    #print(dataCompressed)
