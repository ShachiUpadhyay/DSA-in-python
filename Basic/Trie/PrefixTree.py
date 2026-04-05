
class PrefixTree:

    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False


    def __init__(self):
        self.head = self.TrieNode()

    def insert(self, word: str) -> None:
        current: TrieNode = self.head
        for char in word:
            index = ord(char) - ord('a')
            if not current.children[index]:
                current.children[index] = self.TrieNode()
            current = current.children[index]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current: TrieNode = self.head
        for char in word:
            index = ord(char) - ord('a')
            if not current.children[index]:
               return False
            current = current.children[index]
        if current.isEnd:
            return True
        else:
            return False        

    def startsWith(self, prefix: str) -> bool:
         current: TrieNode = self.head
         for char in prefix:
            index = ord(char) - ord('a')
            if not current.children[index]:
               return False
            current = current.children[index]
         return True
        
if __name__ == "__main__":
    trie = PrefixTree()
    # Test 1: Insert and search
    trie.insert("apple")
    print("Test 1 search 'apple':", trie.search("apple"), "Expected: True")
    print("Test 1 search 'app':", trie.search("app"), "Expected: False")
    print("Test 1 startsWith 'app':", trie.startsWith("app"), "Expected: True")

    # Test 2: Insert 'app', search 'app'
    trie.insert("app")
    print("Test 2 search 'app':", trie.search("app"), "Expected: True")
    print("Test 2 startsWith 'ap':", trie.startsWith("ap"), "Expected: True")

    # Test 3: Insert 'bat', search 'bat', 'bats'
    trie.insert("bat")
    print("Test 3 search 'bat':", trie.search("bat"), "Expected: True")
    print("Test 3 search 'bats':", trie.search("bats"), "Expected: False")
    print("Test 3 startsWith 'ba':", trie.startsWith("ba"), "Expected: True")

    # Test 4: Insert 'banana', search 'banana', startsWith 'ban'
    trie.insert("banana")
    print("Test 4 search 'banana':", trie.search("banana"), "Expected: True")
    print("Test 4 startsWith 'ban':", trie.startsWith("ban"), "Expected: True")

    # Test 5: Search for word not inserted
    print("Test 5 search 'cat':", trie.search("cat"), "Expected: False")
    print("Test 5 startsWith 'ca':", trie.startsWith("ca"), "Expected: False")