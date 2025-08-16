from .node import Node

def print_inorder(current:Node):
    if not current:
        return
    
    print_inorder(current.left)
    print(current.data, end = ' ')
    print_inorder(current.right)

def print_postorder(current:Node):
    if not current:
        return 

    print_postorder(current.left)
    print_postorder(current.right)
    print(current.data, end=' ')    


if __name__ == '__main__':
    root = Node('*')
    r_left = Node('+')
    r_right = Node('4')
    r_left_left = Node('2')
    r_left_right = Node('3')

    root.left = r_left
    root.right = r_right
    r_left.left = r_left_left
    r_left.right = r_left_right

    print_inorder(root)    

