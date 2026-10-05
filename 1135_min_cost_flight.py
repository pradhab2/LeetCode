import sys
print(sys.version)

import heapq
from collections import defaultdict

def minCostFlight(connections,N):
	res=0
	q=[(0,N)]
	d=defaultdict(list)
	visited=[]
	for city1,city2,cost in connections:
		d[city1].append((cost,city2))
		d[city2].append((cost,city1))
	while q and len(visited) < N:
		cost,city = heapq.heappop(q)
		res += cost
		visited.append(city)
		for edgcost,neighbor_city in d[city]:
			heapq.heappush(q,(edgcost,neighbor_city))
	return res if len(visited)==N else -1


assert minCostFlight([[1,2,8],[1,3,1],[2,3,5]],3)==6

# # def main():
# # 	assert minCostFlight([1,2,8],[1,3,1],[2,3,5],N)==6


# # if __name__ == '__main__':
# # 	main()
# # 	print("Successfully complted")

