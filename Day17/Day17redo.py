filename = "inputSmall.txt"
filename = "inputBig.txt"
#data = open(filename).read().split("\n")

#def refresh():
#	remNodes = [node for node in queue]
#	remVals = [node[2] for node in remNodes]
#	sortedQueue = [node for _,node in sorted(zip(remVals,queue))]
#	return sortedQueue

#directions = {(1,0):"V",
#			  (-1,0):"^",
#			  (0,1):">",
#			  (0,-1):"<"}



#def getNeighbours(node):
#	x = node[0]
#	y = node[1]
#	neighbours = []
#	for d in [(1,0),(-1,0),(0,1),(0,-1)]:
#		dx = x + d[0]
#		dy = y + d[1]
#		direction = directions[d]
#		run = node[4] + 1 if d == node[3] else 1
#		print(node,run)
#		if not (d == node[3] and run > 3):		
#			if 0 <= dx < len(data) and 0 <= dy < len(data[0]):
#				neighbour = [dx, dy, loss[(dx,dy)], direction, run, (node[0],node[1])]
#				neighbours.append(neighbour)
#	return neighbours

#import heapq
#width = len(data[0])
#height = len(data)
#heatmap = {(n//width,n%height):int(data[n//width][n%height]) for n in range(len(data) * len(data[0]))}
#loss = {(n//width,n%height):float("inf")for n in range(len(data) * len(data[0]))}
#movements = {(n//width,n%height):"." for n in range(len(data) * len(data[0]))}
#parents = {(n//width,n%height):None for n in range(len(data) * len(data[0]))}
#loss[(0,0)] = 0

##tuples in queue are:
##(x, y, total heat loss, direction travelled to get here, length of run in direction, previous node)
#queue = [(0,0,0,"",0,(0,0))]

#queue = refresh()

#seen = set()

#while len(queue) != 0:
#	queue = refresh()
#	current = queue.pop(0)
#	neighbours = getNeighbours(current)
#	for neighbour in neighbours:
#		if tuple(neighbour) in seen:
#			continue
#		nNode = (neighbour[0],neighbour[1])
#		alt = current[2] + heatmap[nNode]
#		if alt < loss[nNode]:
#			neighbour[2] = alt
#			neighbour = tuple(neighbour)
#			loss[nNode] = neighbour[2]
#			movements[nNode] = neighbour[3]
#			parents[nNode] = (current[0],current[1])
#			queue.append(neighbour)
#			seen.add(neighbour)
#		#input()



#output = [["." for j in range(len(data[i]))] for i in range(len(data))]

#node = (12,12)
#while node != (0,0):
#	nextNode = parents[node]
#	output[node[0]][node[1]] = movements[nextNode]
#	node = nextNode




#for row in output:
#	print("".join(row))

from heapq import heappush, heappop

grid = [list(map(int, line.strip())) for line in open(filename)]

seen = set()
#     (heat loss, row, column, deltaRow, deltColumn, length of run)
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    hl, r, c, dr, dc, n = heappop(pq)
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print(hl)
        break

    if (r, c, dr, dc, n) in seen:
        continue

    seen.add((r, c, dr, dc, n))
    
    if n < 10 and (dr, dc) != (0, 0):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

    if n >= 4 or (dr, dc) == (0, 0):
        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))