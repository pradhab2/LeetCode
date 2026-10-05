#
# venv/src/1135_Connecting_Cities_With_Min_Cost_union_and_find.py
class Solution(object):
    # def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        '''
        Prim's/Krushkal's Algorithm:
        1) Initialize a tree with a single vertex, chosen
        arbitrarily from the graph.
        2) Grow the tree by one edge: of the edges that
        connect the tree to vertices not yet in the tree,
        find the minimum-weight edge, and transfer it to the tree.
        3) Repeat step 2 (until all vertices are in the tree).
        '''
        # city1 <-> city2 may have multiple different cost connections,
        # so use a list of tuples. Nested dict will break algorithm.

    #         G=defaultdict(list)
    #         q=[(0,N)]
    #         visited=set()
    #         total=0

    #         for city1,city2,cost in connections:
    #             G[city1].append((cost,city2))
    #             G[city2].append((cost,city1))

    #         while q and len(visited) < N:
    #             cost,city =heapq.heappop(q)     # min heap
    #             if city not in visited:
    #                 visited.add(city)
    #                 total += cost

    #                 for edgCost,nxtCity in G[city]:
    #                     heapq.heappush(q,(edgCost,nxtCity))

    #         return total if len(visited)==N else -1

    # (1)- 5 -(2)
    # |       /
    # 6     1
    # |   /
    # (3)

    # Union Find  Algo
        def minimumCost(self, N, connections):

            parent = {city: city for city in range(N + 1)}
            total = 0

            def find(city):
                if parent[city] != city:
                    parent[city] = find(parent[city])    # path compression we change the orginal parent dict
                return parent[city]

            def union(c1, c2):
                root1 = find(c1)
                root2 = find(c2)
                if root1 == root2:
                    return False
                parent[root2] = root1

                return True

            connections.sort(key=lambda x: x[2])

            for city1, city2, cost in connections:
                if union(city1, city2):
                    total += cost

            # For disjoint sets/ two component as example 2

            mainRoot = find(N)

            return total if all(mainRoot == find(city) for city in range(1, N + 1)) else -1


sl=Solution()

print(sl.minimumCost(3, [[1,2,8],[1,3,6],[2,3,1]]))





# //
# import heapq
# from collections import defaultdict
#
#
# def minCostFlight(connections, N):
#     res = 0
#     q = [(0, N)]
#     d = defaultdict(list)
#     visited = set()
#     for city1, city2, cost in connections:
#         d[city1].append((cost, city2))
#         d[city2].append((cost, city1))
#
#     while q and len(visited) < N:
#         cost, city = heapq.heappop(q)
#         if city not in visited:
#             res += cost
#             visited.add(city)
#             for edgcost, neighbor_city in d[city]:
#                 heapq.heappush(q, (edgcost, neighbor_city))
#     return res if len(visited) == N else -1
#
#
# print(minCostFlight([[1, 2, 8], [1, 3, 1], [2, 3, 5]], 3))
# # assert minCostFlight([[1, 2, 8], [1, 3, 1], [2, 3, 5]], 3) == 6
