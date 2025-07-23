
from min_heap import MinHeap

def print_tree(node, level=0, label="."):
    if node is not None:
        print_tree(node.right, level + 1, "R")
        print("    " * level + f"{label}: {node.val}")
        print_tree(node.left, level + 1, "L")

def interactive_node_demo():
    h = MinHeap()
    values = [10, 4, 15, 1, 20, 3, 8]
    print("🔁 Inserting values into node-based min heap:", values)

    for v in values:
        h.insert(v)
        print(f"Inserted {v}:")
        print_tree(h.root)
        print()

    print("\n🔽 Extracting elements:")
    while h.root:
        min_val = h.extract_min()
        print(f"Extracted {min_val}:")
        print_tree(h.root)
        print()

if __name__ == "__main__":
    interactive_node_demo()
