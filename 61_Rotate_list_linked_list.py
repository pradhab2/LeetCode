class ListNode():
    def __init__(self,val):
        self.val= val
        self.next=None
        self.prev=None

class rotate_likedlist_k_times():

    def rotate_ll_k_tms(self,head: ListNode,k:int)-> ListNode:
        if not head:
            return head
        tail = head
        length=1
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length    #effectiive k value

        if k == 0:
            return head

        tail.next=head    # making it circular
        tail = head

        for i in range(length-k-1):
            tail=tail.next

        head=tail.next
        tail.next=None

        return head


obj=rotate_likedlist_k_times()

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

res=obj.rotate_ll_k_tms(head,2)
while res:
    print(res.val)
    res=res.next








