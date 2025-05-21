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
    lst.insert_end(6)
    lst.insert_end(10)
    lst.insert_end(14)
    lst.insert_end(19)  
    lst.print()
    print(lst.get_nth(5).data)
    
