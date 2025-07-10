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
    
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == len(self.array):
            self._resize()
        
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def removeAt(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1



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

ra.insert(0, 'Popcorn')
print(ra) # ['Popcorn', 'Apple', 'Cherry', 'Date', 'Elderberry', 'Orange']
ra.insert(ra.size, 'Pizza')
print(ra) # ['Popcorn', 'Apple', 'Cherry', 'Date', 'Elderberry', 'Orange', 'Pizza']
ra.insert(3, 'Gatorage')
print(ra) # ['Popcorn', 'Apple', 'Cherry', 'Gatorage', 'Date', 'Elderberry', 'Orange', 'Pizza']
ra.removeAt(0)
print(ra) # ['Apple', 'Cherry', 'Gatorage', 'Date', 'Elderberry', 'Orange', 'Pizza']
ra.removeAt(3)
print(ra) # ['Apple', 'Cherry', 'Gatorage', 'Elderberry', 'Orange', 'Pizza']
ra.removeAt(ra.size - 1)
print(ra) # ['Apple', 'Cherry', 'Gatorage', 'Elderberry', 'Orange', 'Pizza']