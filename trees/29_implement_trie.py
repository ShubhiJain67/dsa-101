class Trie:

    def __init__(self):
        self.children = [None]*26
        self.wordEnd = False

    def insert(self, word: str) -> None:
        index = 0
        curr = self
        while index < len(word):
            chIndex = ord(word[index]) - ord('a')
            if not curr.children[chIndex]:
                curr.children[chIndex] = Trie()
            curr = curr.children[chIndex]
            index += 1
        curr.wordEnd = True


    def search(self, word: str) -> bool:
        index = 0
        curr = self
        while index < len(word):
            chIndex = ord(word[index]) - ord('a')
            if not curr.children[chIndex]:
                return False
            curr = curr.children[chIndex]
            index += 1
        return curr.wordEnd

    def startsWith(self, prefix: str) -> bool:
        index = 0
        curr = self
        while index < len(prefix):
            chIndex = ord(prefix[index]) - ord('a')
            if not curr.children[chIndex]:
                return False
            curr = curr.children[chIndex]
            index += 1
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
