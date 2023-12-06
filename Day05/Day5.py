filename = "inputSmall.txt"
filename = "inputBig.txt"




data = open(filename,"r").read().split("\n\n")

seeds = [int(seed) for seed in data[0].split(" ")[1:]]
seedRanges = [[seeds[i],seeds[i] + seeds[i+1]] for i in range(0,len(seeds),2)]
tables = [[[int(val) for val in row.split(" ")] for row in table.split("\n")[1:]] for table in data[1:]]

for table in tables:
    table = sorted(table, key=lambda x: x[1])
    for s in range(len(seeds)):
        seed = seeds[s]
        if seed < table[0][1]:
            continue
        if seed > table[-1][1] + table[-1][2]:
            continue
        for t in range(len(table)):
            if table[t][1] <= seed and seed < table[t][1] + table[t][2]:
                seed = table[t][0] + (seed - table[t][1])
                break
        seeds[s] = seed

print(min(seeds))

tables = tables[::-1]
#tables = [tables[0]]
#print(tables)

def isInRange(l):
    for seedRange in seedRanges:
        if seedRange[0] <= l < seedRange[1]:
            return True
    return False

count = 178000000


while True:
    if count % 1000 == 0:
        print(count)
    loc = count
    for table in tables:
        table = sorted(table, key=lambda x: x[0])
        #print(table)
        for row in table:
            if row[0] <= loc < row[0] + row[2]:
                loc += row[1] - row[0]
                break
    if isInRange(loc):
        print(count)
        break
    count += 1