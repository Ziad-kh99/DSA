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

    def is_identical(self, lst):
        cur1 = self.head
        cur2 = lst.head
        same_size = True
        same_values = True

        while True:
            if cur1 is not None and cur2 is None:
                same_size = False
                break

            if cur2 is not None and cur1 is None:
                same_size = False
                break

            if cur1.data != cur2.data:
                same_values = False
                break

            cur1 = cur1.next
            cur2 = cur2.next
        
        if same_size is True and same_values is True:
            print('List 1 and List 2 are Identical.')
        else:
            print('List 1 and List 2 are not Identical.')
        

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
    lst1 = LinkedList()
    lst1.insert_end(61)
    # lst1.insert_end(11)
    # lst1.insert_end(14)
    # lst1.insert_end(19)  

    lst2 = LinkedList()
    lst2.insert_end(61)
    # lst2.insert_end(11)
    # lst2.insert_end(14)
    # lst2.insert_end(19)
    # lst2.insert_end(17)

    lst1.print()
    lst2.print()
    lst1.is_identical(lst2)

    
