class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'
    
class LinkedList:
    def __init__(self, initial_values = None):
        self.head = None

        if initial_values:
            for value in initial_values:
                self.add_element(value)

    def add_element(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            element = Node(value)
            element.next = self.head
            self.head = element

    def get_tail(self):
        if not self.head:
            return
        
        cur = self.head

        while cur.next: cur = cur.next
    
        return cur
    
    def print(self):
        if not self.head:
            return
        
        cur = self.head

        while cur:
            print(cur.data, end=' -> ')
            cur = cur.next
        print()


if __name__ == '__main__':
    lst = LinkedList()
    lst.add_element(10)
    lst.add_element(50)
    lst.add_element(70)
    lst.add_element(35)
    lst.print()
    print(lst.head)
    tail = lst.get_tail()
    print(f'Tail: {tail}')