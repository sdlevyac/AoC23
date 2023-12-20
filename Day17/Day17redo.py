filename = "inputSmall.txt"
#filename = "inputBig.txt"
data = open(filename).read().split("\n")

def refresh():
	remNodes = [node for node in queue]
	remVals = [node[2] for node in remNodes]
	sortedQueue = [node for _,node in sorted(zip(remVals,queue))]
	return sortedQueue

def getNeighbours(x,y):
	neighbours = []
	for d in [[1,0],[-1,0],[0,1],[0,-1]]:
		dx = x + d[0]
		dy = y + d[1]
		if 0 <= dx < len(data) and 0 <= dy < len(data[0]):
			neighbour = (dx, dy)
			neighbours.append(neighbour)
	return neighbours

import heapq
width = len(data[0])
height = len(data)
heatmap = {(n//width,n%height):int(data[n//width][n%height]) for n in range(len(data) * len(data[0]))}
loss = {(n//width,n%height):float("inf")for n in range(len(data) * len(data[0]))}
loss[(0,0)] = 0
print(heatmap)
print(loss)

#tuples in queue are:
#(x, y, total heat loss, direction travelled to get here, length of run in direction)
queue = [(0,0,0,"",0)]

queue = refresh()
print(queue)
while len(queue) != 0:
	queue = refresh()
	current = queue.pop(0)
	neighbours = getNeighbours(current[0], current[1])
	for neighbour in neighbours:
		alt = current[2] + heatmap[neighbour]
		if alt < loss[neighbour]:
			print(neighbour,alt)#create rest of data needed for queue tuple
		input()

