filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename).read().split("\n")
data = [line.split(" ") for line in data]
runs = [line[0] for line in data]
patterns = [line[1] for line in data]

#part 2 expansions
runs = ["?".join([run, run, run, run, run]) for run in runs]
patterns = [",".join([p,p,p,p,p]) for p in patterns]


patterns = [[int(p) for p in pattern.split(",")] for pattern in patterns]

computed = {}
def ways(runs, patterns, i, j, l):
    key = (i, j, l)
    #print(key, runs[i:], patterns[j:], "#"*l)
    if key in computed:
        #print(key,"already computed")
        return computed[key]
    #if at end of run then some valid cases
    if i==len(runs):
        #if After the last pattern and not in a row of #
        if j==len(patterns) and l==0:
            return 1
        #if at the last pattern and length matches pattern
        elif j==len(patterns)-1 and patterns[j]==l:
            return 1
        #all other cases invalid
        else:
            return 0
    ans = 0
    for c in ['.', '#']:
        if runs[i]==c or runs[i]=='?':
            if c=='.' and l==0:
                #if . and not currently in a row of # 
                #then move index of run by 1 and call ways
                ans += ways(runs, patterns, i+1, j, 0)
            elif c=='.' and l>0 and j<len(patterns) and patterns[j]==l:
                #if . and ARE currently in a row o
                #and not on the last of patterns and this . ends 
                #the current row of #
                #then call move index of run and 
                #index of patterns by 1 each and call ways
                ans += ways(runs, patterns, i+1, j+1, 0)
            elif c=='#':
                #if # then move index of run, extend 
                #length of row of # by 1 and call ways
                ans += ways(runs, patterns, i+1, j, l+1)
    computed[key] = ans
    return ans

answer = 0

for i in range(len(data)):   
    print(runs[i])
    print(patterns[i])
    answer += ways(runs[i], patterns[i], 0, 0, 0)
    computed.clear()
print(answer)