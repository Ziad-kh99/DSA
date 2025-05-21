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

    def insert_front(self, value):
        item = Node(value)

        if not self.head:       # Empty List.
            self.head = self.tail = item
        else:
            item.next = self.head
            self.head = item

    def delete_front(self):
        if not self.head:   # Empty list
            return
        elif self.head == self.tail:    # 1 Node.
            self.head = self.tail = None
        else:
            self.head = self.head.next


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
    lst.insert_front(5)
    lst.insert_front(3)
    lst.insert_front(1)
    lst.delete_front()
    lst.delete_front()
    lst.delete_front()
    lst.delete_front()
    lst.print()


