class Trie:
    def __init__(self) -> None:
        self.children = {}
        self.exist = False
        return

    def addWord(self, word: str):
        if len(word) == 0:
            self.exist = True
            return
        ch = word[0]
        if not ch in self.children:
            self.children[ch] = Trie()
        self.children[ch].addWord(word[1:])
        return

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.exist
        ch = word[0]
        if ch == '.':
            children = self.children.keys()
            res = False
            for child in children:
                res = res or self.children[child].search(word[1:])
            return res
        else:
            if not ch in self.children:
                return False
            else:
                return self.children[ch].search(word[1:])


class WordDictionary:
    def __init__(self) -> None:
        self.root = Trie()
        return

    def addWord(self, word: str) -> None:
        return self.root.addWord(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)
