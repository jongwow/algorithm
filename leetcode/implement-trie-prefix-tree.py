class Trie:
    def __init__(self) -> None:
        self.chars = {}
        self.exist = False
        pass

    def insert(self, word: str) -> None:
        # base case
        if len(word) == 0:
            self.exist = True
            return
        # recursive
        firstCh = word[0]
        if firstCh in self.chars:
            return self.chars[firstCh].insert(word[1:])
        else:
            self.chars[firstCh] = Trie()  # register
            return self.chars[firstCh].insert(word[1:])

    def search(self, word: str) -> bool:
        # base case
        if len(word) == 0:
            return self.exist
        # recursive
        firstCh = word[0]
        if firstCh in self.chars:
            return self.chars[firstCh].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        # base case
        if len(prefix) == 0:
            return True
        # recursive
        firstCh = prefix[0]
        if firstCh in self.chars:
            return self.chars[firstCh].startsWith(prefix[1:])
        else:
            return False


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app"))  # return True
trie.insert("app")
print(trie.search("app"))     # return True

# print(trie.chars)
# print(trie.chars['a'].chars)
# print(trie.chars['a'].chars['p'].chars)
# print(trie.chars['a'].chars['p'].chars['p'].chars)
# print(trie.chars['a'].chars['p'].chars['p'].chars['l'].chars)
# print(trie.chars['a'].chars['p'].chars['p'].chars['l'].chars['e'].chars)
