class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'


#> Create and Link:
# Create separate nodes:
node1 = Node(12)
node2 = Node(21)
node3 = Node(23)
node4 = Node(28)

# Link nodes:
node1.next = node2      # 1 -> 2
node2.next = node3      # 2 -> 3
node3.next = node4      # 3 -> 4


#> Navigation:
if __name__ == '__mian__':
    print(node1.data)                   # 1st element (Head)
    print(node1.next.data)              # 2nd element
    print(node1.next.next.data)         # 3rd element
    print(node1.next.next.next.data)    # 4th element 

#> Memory Details:
    print(id(node1), id(node1.next))
    print(id(node2), id(node2.next))
    print(id(node3), id(node3.next))
    print(id(node4))

