from trie import Trie

def run_tests():
    trie = Trie()

    # Insert words
    words = ["apple", "app", "bat", "ball", "bark", "banana"]
    for word in words:
        trie.insert(word)

    # Test search
    assert trie.search("apple") == True, "apple should be found"
    assert trie.search("app") == True, "app should be found"
    assert trie.search("appl") == False, "appl should not be found"
    assert trie.search("bat") == True, "bat should be found"
    assert trie.search("bark") == True, "bark should be found"
    assert trie.search("ban") == False, "ban should not be found"

    # Test starts_with
    assert trie.starts_with("ap") == True, "should have prefix ap"
    assert trie.starts_with("ba") == True, "should have prefix ba"
    assert trie.starts_with("cat") == False, "should not have prefix cat"

    print("✅ All tests passed.\n")
    trie.visualize()

if __name__ == "__main__":
    run_tests()
