import numpy as np

filename = "inputSmall.txt"
filename = "inputBig.txt"

dirEncoded = {"0":"R",
              "1":"D",
              "2":"L",
              "3":"U"}

directions = {"U":[-1,0],
              "D":[1,0],
              "L":[0,-1],
              "R":[0,1]}

perims = [0,0,0,0]

answer = 0

def decode(hexadecimal):
    output = [dirEncoded[hexadecimal[-1]],0]
    for c, char in enumerate(hexadecimal[:-1][::-1]):
        if char.isdigit():
            output[1] += int(char) * (16**c)
        else:
            output[1] += (ord(char) - 87) * (16**c)
    return output

data = open(filename).read().split("\n")

data = [line.split(" ") for line in data]
data = [decode(line[2][2:-1]) for line in data]

x = 0
xMin = 0
xMax = 0
y = 0
yMin = 0
yMax = 0

for line in data:
    if line[0] == "U":
        x -= line[1]
        perims[0] += line[1]
    elif line[0] == "D":
        x += line[1]
        perims[1] += line[1]
    elif line[0] == "L":
        y -= line[1]
        perims[2] += line[1]
    elif line[0] == "R":
        y += line[1]
        perims[3] += line[1]
    xMax = max([x,xMax])
    xMin = min([x,xMin])
    yMax = max([y,yMax])
    yMin = min([y,yMin])

coords = [(0,0)]
for line in data:
    direction = directions[line[0]]
    cx = coords[-1][0] + (line[1] * direction[0])
    cy = coords[-1][1] + (line[1] * direction[1])
    coords.append((cx,cy))

def shoelace(vertices):
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0 
    for i in range(0,numberOfVertices-1):
        sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
        sum2 = sum2 + vertices[i][1] *  vertices[i+1][0] 
    sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]   
    sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]   
    area = abs(sum1 - sum2) / 2
    return area

area = shoelace(coords)
adjusted_area = area + max(perims) + min(perims) + 1
print(adjusted_area)
