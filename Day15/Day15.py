filename = "inputSmall.txt"
filename = "inputBig.txt"

def showBoxes():
    for b, box in enumerate(boxes):
        if len(box) != 0:
            print(b,box)

def getFocus(b, box):
    f = 0
    for l,lens in enumerate(box):
        f += ((b + 1) * (l + 1) * lens[1])
    return f

def hash(plaintext):
    val = 0
    for letter in plaintext:
        val = ((val + (ord(letter))) * 17) % 256
    return val

data = open(filename).read().split(",")
boxes = [[] for _ in range(256)]
hashVal = 0

for inst in data:
    hashVal += hash(inst)
    if "-" in inst:
        split = inst.index("-")
    else:
        split = inst.index("=")
        lens = [inst[:split],int(inst[split+1:])]
    label = inst[:split]
    boxIndex = hash(label)
    action = inst[split]
    value = inst[split + 1:]
    box = boxes[boxIndex]
    if action == "=":
        swapped = False
        for l in box:
            if l[0] == lens[0]:
                l[1] = lens[1]
                swapped = True
                break
        if not swapped:
            box.append(lens)
    if action == "-":
        index = -1
        for l, lVal in enumerate(box):
            if lVal[0] == label:
                index = l
                break
        if index != -1:
            box.pop(index)

focus = 0

for b, box in enumerate(boxes):
    if len(box) != 0:
        focus += getFocus(b, box)

print(hashVal)
print(focus)