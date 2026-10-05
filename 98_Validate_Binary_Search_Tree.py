class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution(object):
    def isValidBST(self,root):
        stack,inOrder=[],float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if root.val <= inOrder:
                return False
            inOrder=root.val
            root=root.right
        return True


#           5
#          / \
#         1   7
#            / \
#           6   8
#                \
#                 9

n1=TreeNode(5)
n2=TreeNode(1)
n3=TreeNode(7)
n4=TreeNode(6)
n5=TreeNode(8)
n6=TreeNode(9)

n1.left=n2
n1.right=n3
n3.left=n4
n3.right=n5
n5.right=n6

sl=Solution()
print(sl.isValidBST(n1))


