fileName = "inputSmall.txt"
fileName = "inputBig.txt"

data = open(fileName, "r").read().split("\n")

maxColours = {"red":12,
              "blue":14,
              "green":13}

score = 0
powerScore = 0
gameNum = 1
for game in data: 
    gameID = game[game.index(" ") + 1:game.index(":")]
    cubeSets = game[game.index(":")+2:].split("; ")
    cubeSets = [cubeSet.split(", ") for cubeSet in cubeSets]
    cubeSets = [[color.split(" ") for color in cubeSet] for cubeSet in cubeSets]
    cubeSets = [{colour[1]:int(colour[0]) for colour in cubeSet} for cubeSet in cubeSets]
    colours = {}
    for cubeSet in cubeSets:
        for colour in cubeSet:
            if colour not in colours:
                colours[colour] = cubeSet[colour]
            else:
                colours[colour] = max(colours[colour], cubeSet[colour])  
    if colours["red"] <= maxColours["red"] and colours["green"] <= maxColours["green"] and colours["blue"] <= maxColours["blue"]:
        score += gameNum
    gameNum += 1
    power = colours["red"] * colours["blue"] * colours["green"]
    powerScore += power
    
print(score, powerScore)