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
