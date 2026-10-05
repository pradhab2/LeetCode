# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution(object):
    def __init__(self,inp):
        self.head = inp

    def __repr__(self):
        node = self.head
        op = []
        while node:
            op.append(node.val)
            node = node.next
        op.append("None")
        s = [str(i) for i in op]
        return "->".join(s)

    def oddEvenList(self, head):
        """
        Put odd positioned numbers together then even positioned numbers together after that in a Linked List
        :type head: ListNode
        :rtype: ListNode
        """
        self.head = head
        odd = head
        even = head.next
        even_head = even

        while even.next and even:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

    def revLinkedListIter(self, head):
        prevNd=None
        currNd=head

        while currNd:
            nextNd=currNd.next
            currNd.next=prevNd
            prevNd=currNd
            currNd=nextNd
        self.head = prevNd
        return prevNd

    def revLinkedListRecur(self, head):

        if head is None or head.next is None:
            return head

        rest=revLinkedListRecur(head.next)

        head.next.next=head
        head.next=None

        return rest

a = ListNode(4)
b = ListNode(2)
c = ListNode(6)
d = ListNode(1)
e = ListNode(5)
f = ListNode(3)
g = ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
#f.next = g
f.next = None
print("Input: ", end="")

ll = Solution(a)
print(ll)

# ll.oddEvenList(a)
# print("Output: ", end="")
# print(ll)

print("Reversed Output Iter: ", end="")
ll.revLinkedListIter(a)
print(ll)

print("Reversed Output Recursive: ", end="")
ll.revLinkedListRecur(a)
print(ll)
