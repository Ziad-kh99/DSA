import ctypes

class Array:
    def __init__(self, size):
        self.size = size                    # user defined size
        self._capacity = max(16, 2 * size)  # actual memory size

        array_data_type = ctypes.py_object * self._capacity
        self.memory = array_data_type()

        for i in range(self._capacity):     # array initialized by 'None'
            self.memory[i] = None       

        
    def expand_capacity(self):
        # double the actual array size
        self._capacity *= 2
        print(f'Expand capacity to {self._capacity}')

        # create a new array of _capacity
        array_data_type = ctypes.py_object * self._capacity
        new_memory = array_data_type()

        for i in range(self.size):          # copy 
            new_memory[i] = self.memory[i]

        # use the new memory and delete old one
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

    
    def __len__(self):
        return self.size
    
    def __getitem__(self, idx):
        # TODO: Is a valid index or not?
        return self.memory[idx]
    
    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __repr__(self):
        result = ''
        for i in range(self.size):
            result += str(self.memory[i]) + ', '
        return result
    



        
