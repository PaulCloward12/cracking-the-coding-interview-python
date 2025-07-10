class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0
        self.load_factor_threshold = 0.75

    def hash_code(self, key):
        hash_value = 0
        prime = 31
        mod = 10**9 + 9
        for char in key:
            hash_value = (hash_value * prime + ord(char)) % mod
        return hash_value

    def put(self, key, value):
        if self.count / self.size >= self.load_factor_threshold:
            self.resize()

        index = self.hash_code(key) % self.size
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        bucket.append(Entry(key, value))
        self.count += 1

    def get(self, key):
        index = self.hash_code(key) % self.size
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value
        return None

    def remove(self, key):
        index = self.hash_code(key) % self.size
        bucket = self.buckets[index]

        for i, entry in enumerate(bucket):
            if entry.key == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def resize(self):
        new_size = self.size * 2
        new_buckets = [[] for _ in range(new_size)]

        for bucket in self.buckets:
            for entry in bucket:
                index = self.hash_code(entry.key) % new_size
                new_buckets[index].append(entry)

        self.size = new_size
        self.buckets = new_buckets

# Example usage:
if __name__ == "__main__":
    ht = HashTable()
    for fruit in ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]:
        ht.put(fruit, len(fruit))

    print(ht.get("apple"))    # Output: 5
    print(ht.remove("apple")) # Output: True
    print(ht.get("apple"))    # Output: None
    print(ht.get("grape"))    # Output: 5
