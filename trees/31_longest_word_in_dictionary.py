class Trie:
    def __init__(self):
        self.children = [None]*26
        self.end = False
    
    def insert(self, word):
        node = self
        for ch in word:
            index = ord(ch)-ord('a')
            if node.children[index] == None:
                node.children[index] = Trie()
            node = node.children[index]
        node.end = True
    
    def hasWord(self, word):
        node = self
        for ch in word:
            index = ord(ch)-ord('a')
            if node.children[index] == None:
                return False
            node = node.children[index]
        return node.end

    

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        longest = ""
        q = deque([[trie, ""]])

        while q:
            node, word = q.popleft()
            if word != "" and not node.end:
                continue
            first = False
            if len(word) > len(longest):
                longest = word
            for index in range(len(node.children)):
                child = node.children[index]
                if child is None:
                    continue
                ch = chr(index + ord('a'))
                q.append([child, word+ch])
        
        return longest
