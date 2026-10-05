class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data


class LinkedList:
    # def __init__(self):
    #     self.head = None

    # Here data is a list with many elements
    def __init__(self, data):
        self.head = None
        for i in range(len(data)):
            elm = data.pop()
            newNode = Node(elm)
            newNode.next = self.head
            self.head = newNode

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        NewNode = Node(node)
        NewNode.next = self.head
        self.head = NewNode

    def drop_node(self, inp):
        if not self.head:
            raise Exception("Linked List is empty")

        tmpNode = self.head

        if self.head.data == inp:
            self.head = self.head.next
            return

        while tmpNode is not None and tmpNode.next is not None:
            if tmpNode.next.data == inp:
                tmpNode.next = tmpNode.next.next
                return
            else:
                tmpNode = tmpNode.next

    def add_last(self, inp):
        tmpNode = self.head
        while tmpNode is not None:
            if tmpNode.next is None:
                newNode = Node(inp)
                newNode.next = None
                tmpNode.next = newNode
                return
            tmpNode = tmpNode.next

    def add_before(self, target_node, new_node):
        if not self.head:
            raise Exception("The Linked List is empty")

        """ If the new element is the first element"""
        if self.head.data == target_node:
            newNode = Node(new_node)
            newNode.next = self.head
            self.head = newNode

        tmpNode = self.head

        while tmpNode is not None:
            if tmpNode.next.data == target_node:
                newNode = Node(new_node)
                newNode.next = tmpNode.next
                tmpNode.next = newNode
                return
            tmpNode = tmpNode.next


ll = LinkedList(["a", "s", "d", "f", "b"])
# ll = LinkedList(["a","s"])
# ll.add_first("a")
# ll.add_first("b")
# ll.add_first("c")
# ll.add_first("d")
print("Initial List: ", end="")
print(ll)
ll.drop_node("b")
print("List after drop: ", end="")
print(ll)
ll.add_last('x')
print("List after add last: ", end="")
print(ll)
