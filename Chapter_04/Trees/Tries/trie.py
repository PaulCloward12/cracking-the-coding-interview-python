class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True

    def visualize(self, node=None, prefix='', level=0):
        if node is None:
            node = self.root
            print("Trie Visualization:\n")

        for char, child_node in sorted(node.children.items()):
            end_marker = '*' if child_node.is_end_of_word else ''
            print('  ' * level + f'└── {char}{end_marker}')
            self.visualize(child_node, prefix + char, level + 1)
