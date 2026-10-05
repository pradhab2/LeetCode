""" Complexity: Hard
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 3
               ^ ^ ^
Output: [3,2,1,4,5]             # 4,5 remain unchanged, 1,2,3 -> 3,2,1

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]             # 1,2 -> 2,1 and 3,4 -> 4,3 and 5 remain unchanged
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        dummy=ListNode(0)              # Hold the head of the result
        prev = dummy
        while head:
            tmp=None
            count = 0
            curr = head
            while head and count < k:
                tmp = head
                head = head.next
                count += 1
            tmp.next = None
            if count < k:
                prev.next = curr
            else:
                prev.next = self.reverse_ll(curr)
                prev = curr
        return dummy.next



    def reverse_ll(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev=head
            head=nxt

        return prev


a=ListNode('1')
b=ListNode('2')
c=ListNode('3')
d=ListNode('4')
e=ListNode('5')
a.next=b
b.next=c
c.next=d
d.next=e
e.next=None

sl=Solution()
# cr,pv,kt=sl.reverse(a,2)
# print("Value of curr:")
# while cr:
#     print(cr.val)
#     cr=cr.next
# print("Value of prev:")
# while pv:
#     print(pv.val)
#     pv=pv.next
#
# while kt:
#     print(kt.val)
#     kt=kt.next

# print("Input: 1->2->3->4->5")
# res=sl.reverseKGroup(a,2)
#
# while res:
#     print(res.val)
#     res=res.next


print("Input: 1->2->3->4->5")
res=sl.reverseKGroup(a,3)

while res:
    print(res.val)
    res=res.next