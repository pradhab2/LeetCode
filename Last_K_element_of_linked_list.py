
class Node(object):
	def __init__(self,val):
		self.val=val
		self.next=None

class Find_last_k_nodes():
	def find_last_k_nodes(self,head,k):
		if not head:
			return head
		left=head
		right=head
		
		for i in range(1,k):
			right = right.next
			
		while right.next:
			left=left.next
			right=right.next
		return self.rev_ll(left)
	def rev_ll(self,head):
		prev=None
		curr=head
		while head:
			tmp=head.next
			head.next=prev
			prev=head
			head=tmp
		return prev

sl=Find_last_k_nodes()

head=Node(2)
head.next=Node(6)
head.next.next=Node(9)
head.next.next.next=Node(12)
head.next.next.next.next=Node(19)
head.next.next.next.next.next=Node(21)
head.next.next.next.next.next.next=Node(34)
head.next.next.next.next.next.next.next=Node(4)

res=sl.find_last_k_nodes(head,3)
while res:
	print(res.val)
	res=res.next







