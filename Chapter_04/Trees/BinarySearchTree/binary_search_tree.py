class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Recursive Insert
    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    # Iterative Insert
    def insert_iterative(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                return  # Duplicate values not inserted

    # Recursive Search
    def search(self, key):
        def _search(node, key):
            if node is None or node.key == key:
                return node
            if key < node.key:
                return _search(node.left, key)
            return _search(node.right, key)

        return _search(self.root, key)

    # Iterative Search
    def search_iterative(self, key):
        current = self.root
        while current:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    # Delete node
    def delete(self, key):
        def _delete(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # Case 1: No child
                if node.left is None and node.right is None:
                    return None
                # Case 2: One child
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # Case 3: Two children
                successor = self._min_value_node(node.right)
                node.key = successor.key
                node.right = _delete(node.right, successor.key)
            return node

        self.root = _delete(self.root, key)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # In-order Traversal (Sorted order)
    def inorder_traversal(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.key, end=' ')
                _inorder(node.right)
        _inorder(self.root)

    # Visual Representation
    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, prefix + ("|   " if is_left else "    "), False)
        print(prefix + ("|-- " if is_left else "\\-- ") + str(node.key))
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "|   "), True)


# --- Example Usage ---
bst = BST()
values = [10, 5, 15, 3, 7, 12, 18]
for val in values:
    bst.insert(val)

print("\nInorder traversal (sorted):")
bst.inorder_traversal()

print("\n\nVisual Tree:")
bst.print_tree()

# Search
print("\nSearch 7:", "Found" if bst.search(7) else "Not found")

# Delete node
print("\nDeleting 10 (root node)...")
bst.delete(10)
bst.print_tree()
