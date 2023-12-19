filename = "inputSmall.txt"
filename = "inputBig.txt"

class rule:
    def __init__(self,xmas,comp,limit,destination):
        self.xmas = xmas
        self.comp = comp
        self.limit = int(limit)
        self.destination = destination
    def checkValue(self,value):
        if ((self.xmas == 0 and self.comp == 0 and self.limit == 0) or 
            (self.comp == "<" and value < self.limit) or 
            (self.comp == ">" and value > self.limit)):
            #if it is final rule or if value meets comparison
            return self.destination
        return "no"
    def checkType(self,valueType):
        return (self.xmas == valueType or 
                (self.xmas == 0 and self.comp == 0 and self.limit == 0))

def parseRule(thisRule):
    if "<" in thisRule:
        cIndex = thisRule.index("<")
        dIndex = thisRule.index(":")
        xmas = thisRule[:cIndex]
        comp = "<"
        value = thisRule[cIndex+1:dIndex]
        destination = thisRule[dIndex+1:]
    elif ">" in thisRule:
        cIndex = thisRule.index(">")
        dIndex = thisRule.index(":")
        xmas = thisRule[:cIndex]
        comp = ">"
        value = thisRule[cIndex+1:dIndex]
        destination = thisRule[dIndex+1:]
    else:
        xmas = 0
        comp = 0
        value = 0
        destination = thisRule
    return rule(xmas,comp,value,destination)

data = open(filename).read().split("\n\n")
workflows = data[0].split("\n")
workflows = [wf.split("{") for wf in workflows]
workflows = [[wf[0], wf[1][:-1].split(",")] for wf in workflows]
workflows = {wf[0]:[parseRule(r) for r in wf[1]] for wf in workflows}

parts = data[1].split("\n")
parts = [part[1:-1].split(",") for part in parts]
parts = [[val.split("=") for val in part] for part in parts]
parts = [[(val[0], int(val[1])) for val in part] for part in parts]

rules = workflows["in"]
answer = 0
for part in parts:
    print(part)
    dest = "in"
    while dest not in ["A","R"]:
        rules = workflows[dest]
        dest = ""
        for r in rules:
            print(r.xmas,r.comp,r.limit,r.destination)
            for val in part:
                if r.checkType(val[0]):
                    temp = r.checkValue(val[1])
                    if temp != "no":
                        dest = temp
                        print("\t",dest)
                        break
            if dest != "":
                break
        
        #input()
    if dest == "A":
        answer += sum([val[1] for val in part])
    #input()
print(answer)