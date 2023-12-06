filename = "inputSmall.txt"
filename = "inputBig.txt"

data = open(filename, "r").read().split("\n")
times = [int(time) for time in data[0][data[0].index(":") + 1:].split(" ") if time not in ["", " "]]
dists = [int(dist) for dist in data[1][data[1].index(":") + 1:].split(" ") if dist not in ["", " "]]

score = 1



for i in range(len(times)):
    time = times[i]
    time = int("".join([str(t) for t in times]))
    dist = dists[i]
    dist = int("".join([str(d) for d in dists]))
    print(time,dist)
    input()
    thisScore = 0
    for t in range(time):
        if t%10000 == 0:
            print(t,time, t/time)
        speed = t
        timeLeft = time - t
        distance = speed * timeLeft
        if distance > dist:
            thisScore += 1
    score *= thisScore
    break
print(score)
