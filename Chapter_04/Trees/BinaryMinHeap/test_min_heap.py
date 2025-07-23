from min_heap import MinHeap

def is_valid_min_heap_node(node):
    if not node:
        return True
    if node.left and node.left.val < node.val:
        return False
    if node.right and node.right.val < node.val:
        return False
    return is_valid_min_heap_node(node.left) and is_valid_min_heap_node(node.right)

def test_node_min_heap():
    h = MinHeap()
    h.insert(10)
    h.insert(4)
    h.insert(15)
    h.insert(1)

    print("After insertions (inorder traversal):", h)
    assert h.peek() == 1, f"Expected root to be 1, got {h.peek()}"
    assert is_valid_min_heap_node(h.root), "Heap structure is invalid after insertions."

    min_val = h.extract_min()
    print("Extracted min:", min_val)
    print("Heap after extraction:", h)
    assert min_val == 1, f"Expected extracted min to be 1, got {min_val}"
    assert is_valid_min_heap_node(h.root), "Heap structure is invalid after extraction."

    h.insert(0)
    h.insert(5)
    print("After more insertions:", h)
    assert h.peek() == 0, f"Expected root to be 0, got {h.peek()}"
    assert is_valid_min_heap_node(h.root), "Heap structure is invalid after reinsertion."

    sorted_out = []
    while h.root:
        sorted_out.append(h.extract_min())

    print("All extracted (should be sorted):", sorted_out)
    assert sorted_out == sorted(sorted_out), "Heap did not return elements in sorted order."

    print("✅ All node-based MinHeap tests passed.")

if __name__ == "__main__":
    test_node_min_heap()