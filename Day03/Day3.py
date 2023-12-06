filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename, "r").read().split("\n")
data = [list(line) for line in data]

gears = []

counter = 0
numbers = {}
positions = {}
parts = []
isNumber = False
number = ""
spots = []
ratios = []

def inRange(num):
    return num >= 0 and num < len(data)

for i in range(len(data)):
    for j in range(len(data[i])):
        if isNumber:
            if data[i][j].isdigit():
                number += data[i][j]
                spots.append([i,j])
            else:
                isNumber = False
                numbers[counter] = number
                positions[counter] = spots
                counter += 1
                spots = []
                number = ""
                if data[i][j] == "*":
                    gears.append([i,j])
        else:
            if data[i][j].isdigit():
                isNumber = True
                number += data[i][j]
                spots.append([i,j])
            elif data[i][j] == "*":
                gears.append([i,j])

for i in range(counter):
    takenSpots = positions[i]
    extraSpots = []
    for takenSpot in takenSpots:
        x = takenSpot[0]
        y = takenSpot[1]
        for dx in range(-1,2):
            for dy in range(-1,2):
                thisExtraSpot = [x+dx, y+dy]
                if thisExtraSpot not in extraSpots and thisExtraSpot not in takenSpots and inRange(x+dx) and inRange(y+dy):
                    extraSpots.append(thisExtraSpot)
    positions[i].extend(extraSpots)  
    for spot in positions[i]:
        if data[spot[0]][spot[1]] != "." and not data[spot[0]][spot[1]].isdigit():
            parts.append(int(numbers[i]))
            break

for gear in gears:
    for i in range(counter):
        for position in positions[i]:
            if position[0] == gear[0] and position[1] == gear[1]:
                gear.append(int(numbers[i]))
                break
    if len(gear) == 4:
        ratio = gear[-2] * gear[-1]
        ratios.append(ratio)
      
print("part 1:",sum(parts))
print("part 2:",sum(ratios))
