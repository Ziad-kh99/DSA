from Node import Node


def print_list(head):
    current_node = head         # this var is just to don't lose head and we can ignore it.
    while current_node is not None:
        print(current_node.data, end=' -> ')
        current_node = current_node.next

def print_list_rec(head):
    if head is None:
        print('Hit base-case')
        exit()
    while head is not None:
        print(head.data, end=' -> ')
        print_list_rec(head.next)


if __name__ == '__main__':
    # Printing the node chain:
    node1 = Node(15)
    node2 = Node(21)
    node3 = Node(23)
    node4 = Node(28)

    node1.next = node2     
    node2.next = node3      
    node3.next = node4    

    print_list_rec(node1)



