class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        left -> root  -> right
        """
        op=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            op.append(root.val)
            root=root.right
        
        return op

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        root -> left -> right 
        """
        op=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                op.append(root.val)
                root=root.left
            root=stack.pop()
            
            root=root.right
        
        return op


    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        root -> left -> right 
        """
        op=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root)                
                root=root.left
                        
            root=root.right
            root=stack.pop()
            op.append(root.val)
        
        return op



node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
node6=TreeNode(6)
node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node3.left=node6


sl=Solution()

   #      1
   #    /   \
   #   2     3
   #  / \   /
   # 4   5 6
print("Inorder Traversal: %s"% sl.inorderTraversal(node1))
print("Preorder Traversal: %s"% sl.preorderTraversal(node1))
# print("Postorder Traversal: %s"% sl.postorderTraversal(node1))
