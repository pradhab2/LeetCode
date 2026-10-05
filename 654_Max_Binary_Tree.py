class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        stk = []
        last = None
        for num in nums:
            while stk and stk[-1].val < num:
                last = stk.pop()
            node = TreeNode(num)
            if stk:
                stk[-1].right = node
            if last:
                node.left = last
            stk.append(node)
            last = None
        return stk[0]

sl = Solution()

print(sl.constructMaximumBinaryTree([3,2,1,6,0,5]))