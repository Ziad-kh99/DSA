class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


#> Create and Link:
root = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)
node7 = Node(70)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6

node6.left = node7

# print node7:
print(root.right.left.left.data)