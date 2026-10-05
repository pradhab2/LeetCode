# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        currNode = head
        stack = []
        ret = []
        i = 0

        while currNode:
            val = currNode.val
            ret.append(0)
            while stack and val > stack[-1][0]:
                _, indx = stack.pop()
                ret[indx] = val

            stack.append((val, i))
            currNode = currNode.next
            i += 1

        return ret

"""
Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
"""