"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
Example 1:
              (1)
          /    |   \
        (3)   (2)   (4)
      /    \
    (5)    (6)
guest
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
                  (1)
          /    |    |     \
        (2)   (3)  (4)    (5)
      /    \        |     /  \
    (6)    (7)     (8)   (9)  (10)
            |       |     |
           (11)    (12)  (13)
            |
           (14)

"""
from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        que=deque([root])
        while len(que) > 0:
            level=[]
            for _ in range(len(que)):
                node = que.popleft()
                level.append(node.val)
                for child in node.children:
                    que.append(child)

            res.append(level)

        return res

    # def levelOrderByLevel(self, root: 'Node', lvl: int) -> List[List[int]]:
    def levelOrderByLevel(self, root: 'Node', lvl: int) -> str:
        res=[]
        que=deque([root])
        vLevel=1
        while len(que) > 0:
            level = []
            for i in range(len(que)):
                node = que.popleft()
                level.append(node.val)

                for child in node.children:
                    que.append(child)

            # res.append(level)
            if (vLevel == lvl):
                res.append(level)
            vLevel += 1

        return ",".join(map(str,res[0]))

n6=Node(6,[])
n5=Node(5,[])
n4=Node(4,[])
n3=Node(3,[n5,n6])
n2=Node(2,[])
n1=Node(1,[n2,n3,n4])

sl=Solution()
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# print(sl.levelOrder(n1))
print(sl.levelOrderByLevel(n1,2))



