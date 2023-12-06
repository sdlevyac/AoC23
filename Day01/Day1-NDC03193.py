fileName = "inputSmall.txt"
fileName = "inputBig.txt"
numbers = {"one":"1",
           "two":"2",
           "three":"3",
           "four":"4",
           "five":"5",
           "six":"6",
           "seven":"7",
           "eight":"8",
           "nine":"9"}
data = open(fileName,"r").read().split("\n")
print(data)
input()
for i in range(len(data)):
    print(data[i])
    anchor = 0
    while anchor < len(data[i]):
        for end in range(anchor, len(data[i]) + 1):
            if data[i][anchor:end] in numbers.keys():
                print(f"replacing {data[i][anchor:end]} with {numbers[data[i][anchor:end]]}")
                data[i] = data[i].replace(data[i][anchor:end], numbers[data[i][anchor:end]])
                
                break
        anchor += 1
    print(data[i])
    #input()
    print("\n\n")
    #for number in numbers.keys():
    #    if number in data[i]:
    #        data[i] = data[i].replace(number,numbers[number])
print(data)
input()
data = [[character for character in list(line) if character.isdigit()] for line in data]
print(data)
input()
print(data)
input()
data = [int("".join([line[0], line[-1]])) for line in data]
print(data)
print(sum(data))