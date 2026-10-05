
class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right



class Solution(object):
    """
    E.g.1: Input: root = [3, 9, 20, null, null, 15, 7]
    (3)
    / \
 (9)   (20)
       / \
    (15) (7)

    Preorder Traversal o/p: [3,9,20,15,7]
    Inorder Traversal o/p:  [9,3,15,20,7]

    """
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        curr = root
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right
                if pred.right is None:
                    res.append(curr.val)
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    curr = curr.right

        return res



    def inorderTraversal(self, root):
        res = []
        curr = root
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    res.append(curr.val)
                    curr = curr.right

        return res

        # Recurssion
    #     def inorderTraversal(self, root):
    #         """
    #         :type root: TreeNode
    #         :rtype: List[int]
    #         """

    #         return self.helper(root,[])

    #     def helper(self,root,res=[]):
    #         if root:
    #             if root.left:
    #                 self.helper(root.left,res)
    #             res.append(root.val)
    #             if root.right:
    #                 self.helper(root.right,res)
    #         return res

    # Iterative method
    #        op=[]
    #         stack=[]
    #         while root or stack:
    #             while root:
    #                 stack.append(root)
    #                 root=root.left
    #             root=stack.pop()
    #             op.append(root.val)
    #             root=root.right

    #         return op

    def preorderTraversal_iterative(self, root):
        res, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            root=stack.pop()
            root = root.right
        return res

    def inorderTraversal_iterative(self, root):
        res, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root=stack.pop()
            res.append(root.val)
            root = root.right
        return res



# n1=TreeNode(1)
# n2=TreeNode(2)
# n3=TreeNode(3)
# # n4=TreeNode(6)
# # n5=TreeNode(8)
# # n6=TreeNode(9)
#
# n1.right=n2
# n2.left=n3
# # n3.left=n4
# # n3.right=n5
# # n5.right=n6

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

sl=Solution()
# print(sl.preorderTraversal(n1))
# print(sl.inorderTraversal(n1))
print(sl.preorderTraversal_iterative(n1))
print(sl.inorderTraversal_iterative(n1))
