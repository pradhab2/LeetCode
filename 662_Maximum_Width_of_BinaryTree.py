# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root=TreeNode(1)
# root.left=TreeNode(3)
# root.right=TreeNode(2)
# root.left.left=TreeNode(5)
# root.left.right=TreeNode(3)
# root.right.right=TreeNode(9)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)




class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        result = 1
        Q = [[root, 0]]
        while Q:
            cnt=len(Q)
            start = Q[0][1]
            end = Q[-1][1]
            result = max(result, (end - start) + 1)
            for i in range(cnt):
                p = Q.pop(0)
                idx = p[1]

                if p[0].left is not None: Q.append([p[0].left, 2 * idx + 1])
                if p[0].right is not None: Q.append([p[0].right, 2 * idx + 2])

        return result

sl=Solution()
print(sl.widthOfBinaryTree(root))

