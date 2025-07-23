class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class MaxHeap:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, key):
        new_node = Node(key)
        self.nodes.append(new_node)

        if len(self.nodes) == 1:
            self.root = new_node
            return

        parent_index = (len(self.nodes) - 2) // 2
        parent = self.nodes[parent_index]

        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node

        self._heapify_up(len(self.nodes) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index <= 0:
            return

        if self.nodes[index].key > self.nodes[parent_index].key:
            self.nodes[index].key, self.nodes[parent_index].key = (
                self.nodes[parent_index].key,
                self.nodes[index].key,
            )
            self._heapify_up(parent_index)

    def extract_max(self):
        if not self.nodes:
            return None

        max_value = self.nodes[0].key
        last_node = self.nodes.pop()

        if not self.nodes:
            self.root = None
            return max_value

        self.nodes[0].key = last_node.key
        self._heapify_down(0)
        return max_value

    def _heapify_down(self, index):
        largest = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if (left_index < len(self.nodes) and 
            self.nodes[left_index].key > self.nodes[largest].key):
            largest = left_index

        if (right_index < len(self.nodes) and 
            self.nodes[right_index].key > self.nodes[largest].key):
            largest = right_index

        if largest != index:
            self.nodes[largest].key, self.nodes[index].key = (
                self.nodes[index].key,
                self.nodes[largest].key,
            )
            self._heapify_down(largest)

    def peek(self):
        return self.nodes[0].key if self.nodes else None

    def print_heap(self):
        print([node.key for node in self.nodes])


heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)

heap.print_heap()       # Output: [30, 20, 5, 10]
print(heap.peek())      # Output: 30
print(heap.extract_max()) # Output: 30
heap.print_heap()       # Output: [20, 10, 5]