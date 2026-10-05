"""
Find the shortest Friend relation path equal or less than the degree provided.

friend_relation=[(“Kevin", "UserB”),(“Kevin", "UserS”),(“UserB", "UserC”),
                 (“UserA", "UserD”),(“UserX", "UserC”),(“UserY","UserX”),
                 (“Bacon", "UserY”),("UserX","Bacon")]

Kevin —— UserB —- UserC —- UserX —- UserY —- Bacon
  |
  |
UserS

Q1 : findShortestPath(Friend_relation, "Kevin", "Bacon", 5)
    O/P : ("Kevin", "UserB", "UserC", "UserX", "UserY", "Bacon")

Kevin —— UserB —- UserC —- UserX —- UserY
  |								        |
  |										|
UserS —— Bacon --------------------------


Q: addFriend("UserS", "Bacon"); # added one more relation
        findShortestPath(Friend_relation,"Kevin", "Bacon", 6)
    O/P: ("Kevin", "UserS", "Bacon"));

"""
from collections import defaultdict,deque

def findShortestPath(friend_relation,src,dst,deg):
    G = defaultdict(list)
    for rec in friend_relation:
        G[rec[0]].append(rec[1])
        G[rec[1]].append(rec[0])

    # print(G)
    q = [[src]]
    deg_cnt = 0
    visited = set()

    while q:
        # print(q,deg_cnt)

        for _ in range(len(q)):
            path=q.pop(0)
            node=path[-1]
            if node == dst and deg_cnt <= deg:
                return path

            if node not in visited:
                visited.add(node)
            for neighbor in G[node]:
                if neighbor not in visited:
                    new_path=list(path)
                    new_path.append(neighbor)
                    q.append(new_path)
        deg_cnt +=1

        # print("deg_cnt: %s" % deg_cnt)

    return ""


friend_relation=[("Kevin", "UserB"),("Kevin", "UserS"),("UserB", "UserC"),
                 ("UserA", "UserD"),("UserX", "UserC"),("UserY","UserX"),
                 ("Bacon", "UserY")]

print(findShortestPath(friend_relation, "Kevin", "Bacon", 5))
# Expected o/p : ['Kevin', 'UserB', 'UserC', 'UserX', 'UserY', 'Bacon']
#
# friend_relation=[("Kevin", "UserB"),("Kevin", "UserS"),("UserB", "UserC"),
#                  ("UserA", "UserD"),("UserX", "UserC"),("UserY","UserX"),
#                  ("Bacon", "UserY"),("UserS", "Bacon")]
#{'Kevin': ['UserB', 'UserS'], 'UserB': ['Kevin', 'UserC'],
# 'UserS': ['Kevin', 'Bacon'], 'UserC': ['UserB', 'UserX'],
# 'UserA': ['UserD'], 'UserD': ['UserA'], 'UserX': ['UserC',
# 'UserY'], 'UserY': ['UserX', 'Bacon'], 'Bacon': ['UserY', 'UserS']}
# print(findShortestPath(friend_relation, "Kevin", "Bacon", 6))

# Expected o/p : ['Kevin', 'UserS', 'Bacon']

# friend_relation=[("A", "B"),("A", "E"),("A", "F"),("D","L"),("L","K"),
#                  ("B", "C"),("C", "D"),
#                  ("E", "G"),("G", "I"),("G", "J"),("J", "K"),("F", "H")]
#
# print(findShortestPath(friend_relation, "A", "K", 4))