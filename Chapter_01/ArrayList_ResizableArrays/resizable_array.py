class ResizableArray:
    def __init__(self, capacity=4):
        self.array = [None] * capacity
        self.size = 0

    def add(self, value):
        if self.size == len(self.array):
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        new_capacity = len(self.array) * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def remove(self, value):
        # Find the first occurrence
        for i in range(self.size):
            if self.array[i] == value:
                # Shift elements to the left
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.size - 1] = None  # Clear the last element
                self.size -= 1
                return True
        return False  # Value not found
    
    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        value = self.array[self.size -1]
        self.array[self.size -1] = None
        self.size -= 1
        return value



    def __str__(self):
        return str(self.array[:self.size])

# Example Usage:
ra = ResizableArray()
ra.add("Apple")
ra.add("Banana")
ra.add("Cherry")
ra.add("Date")
ra.add("Elderberry")
print(ra)  # ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

ra.add("Orange")
ra.add("Blueberry")
ra.add("Peach")
ra.add("Pumpkin")
ra.add("Tomato")
print(ra)  # ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry', 'Peach', 'Pumpkin', 'Tomato']

ra.remove("Banana")
print(ra)  # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry', 'Peach', 'Pumpkin', 'Tomato']

ra.pop()
print(ra) # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry', 'Peach', 'Pumpkin']
ra.pop()
print(ra) # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry', 'Peach']
ra.pop()
print(ra) # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Blueberry']
ra.pop()
print(ra) # ['Apple', 'Cherry', 'Date', 'Elderberry', 'Orange']