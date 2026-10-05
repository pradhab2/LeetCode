""" --  Minimum distance between nodes in an undirected and unweighted Graph  --- 
Lets say we want to find how "far apart" people are in their social circles.

Given a social network of friendships, find the degree of separation between the neighbors.
(The degree of separation of two people is the shortest number of friendships needed to go from one person to another.

Example: Below is a social network.

A - B - C -D - W
|     \ |
E - F - G - H

The lettters represent people in the network and the lines represent friendships between people.

The degree of separation between A and C is 2
                                 A and H is 3
                                 D and E is 4.

inp=[('A','B'),('A','E'),('B','C'),('B','G'),('E','F'),('F','G'),('G','H'),('C','G'),('C','D')]
"""
from collections import defaultdict
from collections import deque
# def deg_separation(inp,src,dst):
#     G=defaultdict(list)
#     for rec in inp:
#         G[rec[0]].append(rec[1])
#         G[rec[1]].append(rec[0])
#     # print(G)
#     q=deque(src)
#     deg_cnt=0
#     visited=set()
#     visited.add(src)
#     while q:
#         for _ in range(len(q)):
#             new_src=q.popleft()
#             if new_src == dst:
#                 return deg_cnt
#             for neighbor in G[new_src]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     q.append(neighbor)
#         deg_cnt += 1
#     return -1
def deg_separation(inp,src,dst):
    G=defaultdict(list)
    for rec in inp:
        G[rec[0]].append(rec[1])
        G[rec[1]].append(rec[0])
    # print(G)
    q=[src]
    visited=set()
    while q:
        path=q.pop(0)
        node=path[-1]
        if node not in visited:
            visited.add(node)
        if node == dst:
            return path
        for neighbor in G[node]:
            if neighbor not in visited:
                new_path=list(path)
                new_path.append(neighbor)
                q.append(new_path)

    return ""

inp=[('A','B'),('A','E'),('B','C'),('B','G'),('E','F'),('F','G'),('G','H'),('C','G'),('C','D'),('D','W')]
# A - B - C -D - W
# |     \ |
# E - F - G - H


print(deg_separation(inp,'A','C'))  # 2
print(deg_separation(inp,'A','H'))  # 3
print(deg_separation(inp,'D','E'))  # 4
print(deg_separation(inp,'W','H'))  # 4


# def six_deg_separation(frnd_list,src,dst,deg):
#     G = defaultdict(list)
#     for rec in inp:
#         G[rec[0]].append(rec[1])
#         G[rec[1]].append(rec[0])
#
#     q = deque(src)
#     deg_cnt = 0
#     visited = set()
#     res=[]
#     while q:
#         for _ in range(len(q)):
#             new_src = q.popleft()
#             visited.add(new_src)
#             res.append(new_src)
#             if new_src == dst:
#                 return deg_cnt
#             for neighbor in G[new_src]:
#                 if neighbor not in visited:
#                     q.append(neighbor)
#         deg_cnt += 1
#     return -1
