length = 6
num = 100000
for i in range(100000):
    length += 5

print(length)

#filename = "inputSmall.txt"
##filename = "inputBig.txt"

#data = open(filename).read().split("\n")
#data = [list(line) for line in data]

#def isEmpty(thisList):
#    return len(thisList) == thisList.count(".")

#row = 0
#while row != len(data):
#    #print(data[row])
#    #input()
#    if isEmpty(data[row]):
#        data.insert(row, [c for c in data[row]])
#        row += 1
#    row += 1

#col = 0
#while col != len(data[0]):
#    column = [row[col] for row in data]
#    if isEmpty(column):
#        for r in range(len(data)):
#            data[r].insert(col, ".")
#        col += 1
#    col += 1

#coords = {}
#pairs = {}

#count = 1
#for i in range(len(data)):
#    for j in range(len(data[0])):
#        if data[i][j] == "#":
#            label = f'{count:03d}'
#            data[i][j] = label
#            coords[label] = [i,j]
#            count += 1
#        else:
#            data[i][j] = " . "

#for row in data:
#    print("".join(row))

#for coord in coords:
#    pairs[coord] = [star for star in coords if star != coord and ((star in pairs and coord not in pairs[star]) or star not in pairs)]

#for pair in pairs:
#    print(pair, pairs[pair])

