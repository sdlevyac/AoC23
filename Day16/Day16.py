filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n")
data = [list(line) for line in data]

def draw(grid):
    output = ""
    for row in grid:
        for col in row:
            output += col
        output += "\n"
    print(output)

energy = [["." for j in i] for i in data]

trails = {"r":">",
          "l":"<",
          "u":"^",
          "d":"v"}

directions = {"r":[0,1],
              "l":[0,-1],
              "u":[-1,0],
              "d":[1,0]}

beams = [[0,0,"r"]]

active = True

draw(data)
draw(energy)



while active:
    changes = 0
    #print(len(beams),"beams")
    for beam in beams:  
        x = beam[0]
        y = beam[1]
        data[x][y] = trails[beam[2]] if data[x][y] == "." else data[x][y]
        if energy[x][y] == ".":
            energy[x][y] = "#"
            changes += 1
        direction = directions[beam[2]]
        beam[0] += direction[0]
        beam[1] += direction[1]
        try:
            newCell = data[beam[0]][beam[1]]
        except :
            continue      
        if newCell == "\\":
            if beam[2] == "r":
                beam[2] = "d"
            elif beam[2] == "l":
                beam[2] = "u"
            elif beam[2] == "u":
                beam[2] = "l"
            elif beam[2] == "d":
                beam[2] = "r"
        elif newCell == "/":
            if beam[2] == "r":
                beam[2] = "u"
            elif beam[2] == "l":
                beam[2] = "d"
            elif beam[2] == "u":
                beam[2] = "r"
            elif beam[2] == "d":
                beam[2] = "l"
        elif newCell == "|":
            beam[2] = "u"
            beams.append([beam[0],beam[1],"d"])
        elif newCell == "-":
            beam[2] = "l"
            beams.append([beam[0],beam[1],"r"])
    beams = [beam for beam in beams if ((beam[0] >= 0 and beam[0] < len(data) and beam[1] >= 0 and beam[1] < len(data[0])))]# and data[beam[0]][beam[1]] in ["|","-",".","/","\\"] and data[beam[0]][beam[1]] not in ["<",">","^","v"])]
    draw(data)
    #draw(energy)
    if changes == 0:
        break
    print(len(beams),"beams")
    print(changes,"changes")
    #input()
    
print(sum([line.count("#") for line in energy]))     