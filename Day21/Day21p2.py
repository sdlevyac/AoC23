filename = "inputSmall.txt"
#filename = "inputBig.txt"
data = open(filename).read().split("\n")
grid = [list(line) for line in data]


places = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            places.append((i,j))

steps = 1
while True:
    newPlaces = []
    for place in places:
        x = place[0]
        y = place[1]
        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            dx = place[0] + d[0]
            dy = place[1] + d[1]
            bx = dx % len(grid)
            by = dy % len(grid[0])
            #print(x,y,dx,dy,bx,by)
            if grid[bx][by] != "#":
                if (dx,dy) not in newPlaces:
                    newPlaces.append((dx,dy))
    #print(newPlaces)
    with open("out.txt","a") as a:
        a.write(f"{steps},{len(newPlaces)}\n")
    print(f"after {steps} steps ==> {len(newPlaces)} places can be reached")
    if steps in [6,10,50,100,500,1000,5000]:
        print("~"*50)
    places = [place for place in newPlaces]
    steps += 1
