
"""323. Number of Connected Components in an Undirected Graph
(M) You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.

i) Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

0--1      3
   |      |
   2      4
ii) Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
0-1-2-3-4  so op is 1

"""

class Solution:
    def countComponents(self, n, edges):
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])      # Path compression
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        # input  [[0,1],[1,2],[3,4]]
        parent = [i for i in range(n)]
        rank = [0] * n
        for x, y in edges:
            union(x, y)
        print(parent)
        print(rank)
        res_set = set()
        for x in parent:
            res_set.add(find(x))

        return len(res_set)

sl=Solution()

print(sl.countComponents(5,[[0,1],[1,2],[3,4]]))

# def countComponents(self,n, edges):
#     p = list(range(n))
#     def find(x):
#         if x != p[x]: p[x] = find(p[x])
#         return p[x]
#     for u, v in edges:
#         p[find(u)] = find(v)
#     # return len(set(p))
#     print(p)
#     return len(set(map(find, range(n))))

