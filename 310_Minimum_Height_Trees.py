""" Find a node in the tree where it will have the minimum height if that node become root
i.e. find the centriod of the tree.

Here approach is create a adjancecy list/grapg, find the leafs"""

from collections import defaultdict
class MHT(object):

    def minimumHeightTrees(self, n, edges):

        # base cases
        if n <= 2:
            return [i for i in range(n)]

        graph = defaultdict(list)

        # Build the graph with the adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # For in p [[0,1],[0,2],[0,3],[3,4],[4,5]]  n=6
        # print(graph)
        # {0: [1, 2, 3], 1: [0], 2: [0], 3: [0, 4], 4: [3, 5], 5: [4]}

        # Initialize the first layer of leaves
        leaves = [node for node in graph.keys() if len(graph[node]) == 1]

        # Trim the leaves until reaching the centroids
        while n > 2:
            n = n - len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)    # remove the current leaves along with the edges

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves  # prepare for the next round

        return leaves

    def MHT2(self,n, edges):
        G=defaultdict(list)
        if n <= 2:
            return [i for i in range(n)]
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)
        leaves = [node for node in G.keys() if len(G[node])==1]
        while n > 2:
            n = n - len(leaves)
            new_leaves=[]
            for leaf in leaves:
                neighbor = G[leaf].pop()
                G[neighbor].remove(leaf)
                if len(G[neighbor])==1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves






m = MHT()
# print(m.minimumHeightTrees(4,[[1,0],[1,2],[1,3]]))
# print(m.minimumHeightTrees(11, [[9, 8], [8, 4], [4, 5], [5, 6], [4, 3], [4, 2], [3, 7], [7, 10], [2, 1], [2, 0]]))
# print(m.minimumHeightTrees(6,[[0,1],[0,2],[0,3],[3,4],[4,5]]))
print(m.MHT2(6,[[0,1],[0,2],[0,3],[3,4],[4,5]]))
print(m.MHT2(2,[0,1]))