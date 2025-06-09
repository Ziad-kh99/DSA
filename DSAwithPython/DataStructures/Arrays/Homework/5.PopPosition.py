import ctypes


class Array:
    def __init__(self, size):
        self.size = size  # user size
        self._capacity = max(16, 2 * size)  # actual memory size

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = None

    def expand_capacity(self):
        self._capacity *= 2
        print(f'Expand capacity to {self._capacity}')

        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):  # copy
            new_memory[i] = self.memory[i]

        del self.memory
        self.memory = new_memory

    def append(self, item):
        if self.size == self._capacity:
            self.expand_capacity()
        self.memory[self.size] = item
        self.size += 1

    def insert(self, idx, item):

        assert 0 <= idx < self.size

        if self.size == self._capacity:
            self.expand_capacity()

        for p in range(self.size - 1, idx - 1, - 1):
            self.memory[p + 1] = self.memory[p]
        self.memory[idx] = item
        self.size += 1

    def left_shift(self, idx):
        for i in range(idx, self.size - 1):
            self.memory[i] = self.memory[i + 1]

    def pop_position(self, idx = -1):
        if self.size == 0:
            return
        
        # Last Position:
        if idx == self.size - 1:
            last_item = self.memory[self.size - 1]
            self.size -= 1
            return last_item
    
        item = self.memory[idx]
        self.left_shift(idx)
        self.size -= 1

        return item
        
    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.memory[idx]  

    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __repr__(self):
        result = ''
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        return result
    

if __name__ == '__main__':
    array = Array(0)
    array.append(0)
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    print(array)
    result = array.pop_position(1) 
    print(array)
    print(result)


