import ctypes

class Array:
    def __init__(self, size):
        self.size = size           
        self._capacity = max(16, 2 * size) 

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):   
            self.memory[i] = None       

        
    def expand_capacity(self):
        self._capacity *= 2
        print(f'Expand capacity to {self._capacity}')

        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):          # copy 
            new_memory[i] = self.memory[i]

        del self.memory
        self.memory = new_memory

    def append(self, item):        
        '''
            Add item at the end of the array.
        '''
        if self.size == self._capacity:
            self.expand_capacity()

        self.memory[self.size] = item
        self.size += 1

    def insert(self, idx, item):    
        '''
            Add item at a specific index in the array.
        '''
        assert 0 <= idx < self.size

        if self.size == self._capacity:
            self.expand_capacity()

        for p in range(self.size - 1, idx -1, -1):
            self.memory[p + 1] = self.memory[p]

        self.memory[idx] = item
        self.size += 1

    def right_rotation(self):
        if self.size == 0:
            return
        
        last_item = self.__getitem__(self.size -1)

        for i in range(self.size -1, 0, -1):
            self.memory[i] = self.memory[i - 1]

        self.memory[0] = last_item


    def right_rotation_steps(self, steps):
        '''
            - We don't have to rotate n_steps if n_steps > array.length
                We only need size - 1 iterations.
            - If n_steps == array.length then we'll come up with the same array order.
            - If n_steps > array.length then n_steps mod array.lenght = actual_n_steps
        '''
        # Check num of steps:
        if steps > self.size:
            steps = steps % self.size
        elif steps == self.size:
            return 
        
        for i in range(steps):
            self.right_rotation()
        
    def reverse(self, idx1, idx2):
        while idx1 <= idx2:
            self.memory[idx1], self.memory[idx2] = self.memory[idx2], self.memory[idx1]
            idx1 += 1
            idx2 -= 1
    
    def right_rotation_steps_v2(self, steps):
        if steps > self.size:
            steps %= self.size

        # 1. Reverse the whole array:
        self.reverse(0, self.size - 1)

        # 2. Reverse at split point:
        

        # 3. Revers each splitted part:


    
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
    array.reverse(0, array.size - 1)
    print(array)

    # array.right_rotation_steps(10)
    # print(array)




