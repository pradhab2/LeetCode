
"""Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level)
Example 1:
Input: root = [3,9,20,null,null,15,7]
         (3)
        /   \
    (9)      (20)
            /    \
          (15)   (7)

Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []


"""


from collections import deque
class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right



class Solution(object):

        def levelOrder(self, root):
            if not root:
                return []
            queue = deque([root])
            result = []
            while len(queue) > 0:
                level = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(level)

            return result





n1=TreeNode(3)
n2=TreeNode(9)
n3=TreeNode(20)
n4=TreeNode(15)
n5=TreeNode(7)
# n6=TreeNode(9)

n1.left=n2
n1.right=n3
n3.left=n4
n3.right=n5
# n5.right=n6

sl=Solution()
print(sl.levelOrder(n1))
# print(sl.inorderTraversal(n1))