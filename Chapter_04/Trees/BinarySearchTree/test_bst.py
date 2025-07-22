from pathlib import Path

# Unit test code for the BST implementation
unit_test_code = ""
import unittest
from bst import BST

class TestBST(unittest.TestCase):

    def setUp(self):
        self.bst = BST()
        for val in [10, 5, 15, 3, 7, 12, 18]:
            self.bst.insert(val)

    def test_inorder_traversal(self):
        result = []
        def capture(node):
            if node:
                capture(node.left)
                result.append(node.key)
                capture(node.right)
        capture(self.bst.root)
        self.assertEqual(result, [3, 5, 7, 10, 12, 15, 18])

    def test_search_found(self):
        node = self.bst.search(7)
        self.assertIsNotNone(node)
        self.assertEqual(node.key, 7)

    def test_search_not_found(self):
        node = self.bst.search(99)
        self.assertIsNone(node)

    def test_delete_leaf_node(self):
        self.bst.delete(3)
        self.assertIsNone(self.bst.search(3))

    def test_delete_node_with_one_child(self):
        self.bst.insert(6)
        self.bst.delete(7)
        self.assertIsNone(self.bst.search(7))
        self.assertIsNotNone(self.bst.search(6))

    def test_delete_node_with_two_children(self):
        self.bst.delete(10)
        self.assertIsNone(self.bst.search(10))
        inorder_result = []
        def capture(node):
            if node:
                capture(node.left)
                inorder_result.append(node.key)
                capture(node.right)
        capture(self.bst.root)
        self.assertEqual(inorder_result, sorted(set([5, 15, 3, 7, 12, 18])))

if __name__ == '__main__':
    unittest.main()

# Save test file
test_file_path = "/mnt/data/test_bst.py"
Path(test_file_path).write_text(unit_test_code.strip())

test_file_path
'/mnt/data/test_bst.py'