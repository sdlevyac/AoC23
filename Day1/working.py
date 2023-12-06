fileName = "inputSmall.txt"
#fileName = "inputBig.txt"
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
data = open(fileName,"r").read().split("\n")

values = []

for i in range(len(data)):
    digits = []

    for c in range(len(data[i])):
        if data[i][c].isdigit():
            digits.append(data[i][c])
        else:
            for n in range(len(numbers)):
                if data[i][c:].startswith(numbers[n]):
                    
                    digits.append(str(n+1))
    print(data[i],digits,[digits[0],digits[-1]])
    values.append(int(digits[0] + digits[-1]))

print(values)
print(sum(values))