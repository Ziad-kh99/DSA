class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, value):
        item = Node(value)
        if not self.head:
            self.head = self.tail = item
        else:
            self.tail.next = item
            self.tail = item

    def get_nth(self, n):
        if not self.head:       # Empty list
            print('List is empty')
            exit()
        
        position = 1
        cur = self.head

        while cur is not None:
            if position == n:
                return cur 
            else:
                position += 1
                cur = cur.next

        if cur is None:
            print('Invalid position!')
            exit()

    def swap_head_tail(self):
        head_next = self.head.next
        cur_node = self.head

        if not self.head:
            print('Empty List')
            exit()

        if self.head == self.tail:
            return


        while cur_node.next is not None:
            if cur_node.next.next is None:
                cur_node.next = self.head
                self.head.next = None
            cur_node = cur_node.next
        
        self.tail.next = head_next
        # self.head.next = None

        print('Swapping Done!')

    def print(self):
        temp_head = self.head

        while temp_head is not None:
            print(temp_head.data, end=' -> ')
            temp_head = temp_head.next
        print()

    def __iter__(self):
        temp_head = self.head

        while temp_head is not None:
            yield temp_head
            temp_head = temp_head.next

if __name__ == '__main__':
    lst = LinkedList()
    lst.insert_end(1)
    lst.insert_end(2)
    lst.insert_end(3)
    lst.insert_end(4)
    lst.print()
    print(f'Head Val: {lst.head.data} - Head add: {id(lst.head)}')
    print(f'Tail Val: {lst.tail.data} - Tail add: {id(lst.tail)}')
    lst.swap_head_tail()
    print(f'Head Val: {lst.head.data} - Head add: {id(lst.head)}')
    print(f'Tail Val: {lst.tail.data} - Tail add: {id(lst.tail)}')
    # print(lst.head.next)