
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class MinHeap:
    def __init__(self):
        self.root = None
        self.nodes = []

    def insert(self, val):
        new_node = Node(val)
        self.nodes.append(new_node)
        if not self.root:
            self.root = new_node
            return
        parent_index = (len(self.nodes) - 2) // 2
        parent = self.nodes[parent_index]
        new_node.parent = parent
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
        self._heapify_up(new_node)

    def extract_min(self):
        if not self.root:
            return None
        if len(self.nodes) == 1:
            val = self.root.val
            self.root = None
            self.nodes.pop()
            return val
        min_val = self.root.val
        last_node = self.nodes.pop()
        if self.nodes:
            self.root.val = last_node.val
            if last_node.parent:
                if last_node.parent.right == last_node:
                    last_node.parent.right = None
                else:
                    last_node.parent.left = None
            self._heapify_down(self.root)
        return min_val

    def _heapify_up(self, node):
        while node.parent and node.val < node.parent.val:
            node.val, node.parent.val = node.parent.val, node.val
            node = node.parent

    def _heapify_down(self, node):
        while node:
            smallest = node
            if node.left and node.left.val < smallest.val:
                smallest = node.left
            if node.right and node.right.val < smallest.val:
                smallest = node.right
            if smallest == node:
                break
            node.val, smallest.val = smallest.val, node.val
            node = smallest

    def inorder(self, node=None):
        if node is None:
            node = self.root
        return (self.inorder(node.left) if node.left else []) + [node.val] + (self.inorder(node.right) if node.right else []) if node else []

    def peek(self):
        return self.root.val if self.root else None

    def __str__(self):
        return str(self.inorder())


# Example
heap = MinHeap()
heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.insert(1)

print(heap)  # Inorder traversal (not heap order)

print(heap.peek())        # Output: 1
print(heap.extract_min()) # Output: 1
print(heap.peek())      # Output: 4