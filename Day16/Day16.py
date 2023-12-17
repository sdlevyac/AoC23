filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n")
data = [list(line) for line in data]

def showEnergy(energy):
    output = ""
    for row in energy:
        for col in row:
            if col > 0:
                output += "#"
            else:
                output += "."
        output += "\n"
    print(output)
def draw(grid,separator=""):
    for i in range(len(data)):
        print(separator.join(list(map(str,grid[i]))))
    print("~"*len(data[0]))



#could just try every option
#may be a clever method...


nextSteps = {">":[0,1],
             "<":[0,-1],
             "^":[-1,0],
             "v":[1,0]}

transforms = {">":{"/":"^",
                   "\\":"v",
                   "|":"^v",
                   "-":">"},
              "<":{"/":"v",
                   "\\":"^",
                   "|":"^v",
                   "-":"<"},
              "^":{"/":">",
                   "\\":"<",
                   "|":"^",
                   "-":"<>"},
              "v":{"/":"<",
                   "\\":">",
                   "|":"v",
                   "-":"<>"}}

def evaluate(si,sj,symbol):
    data = open(filename).read().split("\n")
    data = [list(line) for line in data]
    energy = [[data[i][j] for j in range(len(data[i]))] for i in range(len(data))]
    energy = [[0 for j in i] for i in data]
    lasers = [["." for j in i] for i in data]
    lasers[si][sj]=symbol
    vals = []
    while True:
        #start = sum([len([cell for cell in line if cell > 0]) for line in energy])
        lasersBuffer = [line[:] for line in lasers]
        for i in range(len(data)):
            for j in range(len(data[i])):
                energy[i][j] = energy[i][j] + 1 if lasers[i][j] != "." else energy[i][j]
        #print("applying tranforms...")
        for i in range(len(data)):
            for j in range(len(data[i])):          
                if lasers[i][j] != "." and data[i][j] in ["/","\\","-","|"]:
                    new = ""
                    for symbol in lasers[i][j]:
                        new += transforms[symbol][data[i][j]]
                    lasers[i][j] = new
        #print("transforms applied")
        for i in range(len(data)):
            for j in range(len(data[i])):
                if lasers[i][j] != ".":
                    for symbol in lasers[i][j]:
                        direction = nextSteps[symbol]
                        if 0 <= i + direction[0] < len(data) and 0 <= j + direction[1] < len(data[i]):
                            if lasersBuffer[i+direction[0]][j+direction[1]] != "." and data[i+direction[0]][j+direction[1]] not in ["-","|"]:
                                lasersBuffer[i+direction[0]][j+direction[1]] += symbol
                            else:
                                lasersBuffer[i+direction[0]][j+direction[1]] = symbol
                    lasersBuffer[i][j] = "."
        #showEnergy()
        lasers = [line[:] for line in lasersBuffer]
        end = sum([len([cell for cell in line if cell > 0]) for line in energy])
        vals.append(end)
        #print(end, len(vals))
        if len(vals) > 10: 
            vals = vals[-10:]
            if len(list(set(vals))) == 1:
                #showEnergy(energy)
                print("\t",vals[-1])
                return vals[-1]
    
    #input()


allVals = []
for i in range(0,len(data)):
    print(i+1,"/",len(data))
    allVals.append(evaluate(i,0,">"))
    with open("output.txt","a") as w:
        w.write(f"{allVals[-1]}\n")
    allVals.append(evaluate(i,-1,"<"))
    with open("output.txt","a") as w:
        w.write(f"{allVals[-1]}\n")
for j in range(0,len(data[0])):
    print(j+1,"/",len(data[0]))
    allVals.append(evaluate(0,j,"v"))
    with open("output.txt","a") as w:
        w.write(f"{allVals[-1]}\n")
    allVals.append(evaluate(-1,j,"^"))
    with open("output.txt","a") as w:
        w.write(f"{allVals[-1]}\n")
    
print("anser=",max(allVals))