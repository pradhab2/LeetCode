class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    # def __repr__(self):


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
""" 
            1
           / \
          2   3
        /  \   \
       4    5   6
"""


def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)


# print(printCurrentLevel(root,3))


from collections import deque


def level_order_traversal(root):
    res = []
    q = deque()
    if not root:
        return None
    q.append(root)
    while q:
        node = q.popleft()
        res.append(node.data)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return res


def level_order_traversal2(root):  # Using Simple list not deque
    res = []
    q = [root]
    while q:
        n = len(q)
        for _ in range(n):
            root = q.pop(0)
            res.append(root.data)
            if root.left: q.append(root.left)
            if root.right: q.append(root.right)
    return res


def print_a_level_elm(root, level):
    res = []
    q = [root]
    curr_level = 0
    while q:
        n = len(q)
        curr_level += 1
        for _ in range(n):
            node = q.pop(0)
            if curr_level == level:
                res.append(node.data)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return res


# print(print_a_level_elm(root, 1))


# print (level_order_traversal2(root))
#
class SOLN():

    def __init__(self):
        self.total = 0

    def sum_of_the_leaf_nodes(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.total += root.data
        self.sum_of_the_leaf_nodes(root.left)
        self.sum_of_the_leaf_nodes(root.right)

        return self.total

def sum_of_the_leaf_nodes(root):
    def helper(root,total):          # Here total can not be pass as Integer as Integer is Immutable
        if not root:
            return
        if not root.left and not root.right:
            total .append(root.data)
            if root.left: helper(root.left,total)
        if root.right: helper(root.right,total)
        return total

    return sum(helper(root,[]))


print(sum_of_the_leaf_nodes(root))

sl = SOLN()
print(sl.sum_of_the_leaf_nodes(root))
