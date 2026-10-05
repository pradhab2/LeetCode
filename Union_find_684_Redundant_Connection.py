
from collections import defaultdict
class Solution(object):
    # def __init__(self):
    #     self.unvrslMap = defaultdict(lambda: -1, {})
    #
    # def findRedundantConnection(self, edges):
    #     """
    #     :type edges: List[List[int]]
    #     :rtype: List[int]
    #     """
    #
    #     for edge in edges:
    #         u, v = edge
    #         x = self.findParent(self.unvrslMap, u)
    #         y = self.findParent(self.unvrslMap, v)
    #         if x == y:
    #             print(self.unvrslMap)
    #             return([u, v])
    #
    #         self.union(self.unvrslMap, x, y)
    #
    #     return res[-1]
    #
    # def findParent(self, unvrslMap, i):
    #     if unvrslMap[i] == -1:
    #         return i
    #     if unvrslMap[i] != -1:
    #         return self.findParent(unvrslMap, unvrslMap[i])
    #
    # def union(self, unvrslMap, x, y):
    #     xParent = self.findParent(unvrslMap, x)
    #     yParent = self.findParent(unvrslMap, y)
    #     if xParent != yParent:
    #         self.unvrslMap[xParent] = yParent
    def findRedundantConnection(self, edges):
        p = [x for x in range(len(edges) + 1)]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            if find(x) == find(y):
                return True
            p[find(x)] = find(y)

        for x, y in edges:
            if union(x, y):
                return [x, y]

sl = Solution()

print(sl.findRedundantConnection( [[2,3],[5,2],[1,5],[4,2],[4,1]] ))

# Ans  : [4,1] as it is coming last in the array.
#
# (4)----(2)----(3)
#  |      |
#  |      |
# (1)----(5)