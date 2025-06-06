class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'

class LinkedList:
    size = 0
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


    def insert_front(self, value):
        item = Node(value)

        if not self.head:       # Empty List.
            self.head = self.tail = item
        else:
            item.next = self.head
            self.head = item

        size += 1
        

    def delete_front(self):
        if not self.head:   # Empty list
            return
        elif self.head == self.tail:    # 1 Node.
            self.head = self.tail = None
        else:
            self.head = self.head.next

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

    def get_nth_from_back(self, n):
        if not self.head:
            print('Empty list')
        
        cur = self.head
        size = 0
        
        # Get length:
        while cur is not None:
            size += 1
            cur = cur.next

        target = (size - n) + 1
        node = self.get_nth(target)
        return node
        


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
    lst.insert_end(11)
    lst.insert_end(22)
    lst.insert_end(33)
    lst.insert_end(44)
    lst.insert_end(55)
    lst.insert_end(66)

    print(lst.get_nth_from_back(7))

    