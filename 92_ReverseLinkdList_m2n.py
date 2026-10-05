# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return self.val


class Solution(object):
    def __init__(self, inp):
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

    # Input: 1->2->30->40->50->60->70->None

    # 30-50  2-40 40- 30
    # ll.reverseBetween(a, 3, 6)

    def reverseBetween(self, head, m, n):
        i = 0
        prevNode = head
        while prevNode:
            i += 1
            while i == m - 1:
                currNode = prevNode.next
                while i < n-1:
                    Next = currNode.next
                    currNode.next=Next.next
                    Next.next=prevNode.next
                    prevNode.next=Next
                    i += 1
            prevNode = prevNode.next

        return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(30)
d = ListNode(40)
e = ListNode(50)
f = ListNode(60)
g = ListNode(7)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = None
print("Input: ", end="")

x=ListNode(3)
y=ListNode(5)
x.next=y
y.next=None

ll = Solution(x)
print(ll)
# ll.reverseBetween(a, 3, 6)
ll.reverseBetween(x, 0, 1)
print("Output: ", end="")
print(ll)
