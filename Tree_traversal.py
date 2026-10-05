class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):      # left -> root -> right
        """
        :type root: TreeNode
        :rtype: List[int]
        left -> root  -> right
        """
        op = []
        stack = []
        height = 0
        while root or stack:
            while root:
                stack.append(root)
                height = max(height, len(stack))
                root = root.left
            root = stack.pop()
            op.append(root.val)
            root = root.right
        print("Height of Tree: %s" % height)
        return op

    def preorderTraversal(self, root):  #  root -> left -> right
        """
        :type root: TreeNode
        :rtype: List[int]
        root -> left -> right
        """
        op = []
        stack = []
        # height=0
        while root or stack:
            while root:
                stack.append(root)
                # height=max(height,len(stack))
                op.append(root.val)
                root = root.left
            root = stack.pop()
            root = root.right
        # print("Height of pre: %s" % height)
        return op
    def pstorderTraversal_stk_rev(self, root):   # left -> right -> root
        """
        :type root: TreeNode
        :rtype: List[int]
         left -> right -> root
        """
        op = []                                     #      1
        stack = [root]                              #    /   \
        while stack:                                #   2     3
            node = stack.pop()                      #  / \   / \
            if node :                               # 4   5 6   7
                op.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)

        return op[::-1]

    def postorderTraversal_stk(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
         left -> right -> root
        """
        stack = []
        res=[]
        height=0
        # curr=root
        while stack or root:                                   #      1
            while root:                                        #    /   \
                stack.append(root)                             #   2     3
                height = max(height,len(stack))                #  / \   / \
                root = root.left                               # 4   5 6   7
            else:
                temp=stack[-1].right
                if not temp:  #temp == None
                    temp=stack.pop()
                    res.append(temp.val)
                    while stack and temp == stack[-1].right:  # here we are done with the traversal(left and right) 5 - 2 case
                        temp=stack.pop()
                        res.append(temp.val)
                else:
                    root=temp
        print("height:%s" % height)
        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

sl = Solution()

#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7


# Inorder Traversal: [4, 2, 5, 1, 6, 3, 7]
# Preorder Traversal: [1, 2, 4, 5, 3, 6, 7]
# print("Inorder Traversal: %s" % sl.inorderTraversal(node1))
# print("Preorder Traversal: %s" % sl.preorderTraversal(node1))

# Postorder Traversal: [4, 5, 2, 6, 7, 3, 1]
print("Pstorder Traversal: %s" % sl.pstorderTraversal_stk_rev(node1))
print("Postorder Traversal: %s"% sl.postorderTraversal_stk(node1))
