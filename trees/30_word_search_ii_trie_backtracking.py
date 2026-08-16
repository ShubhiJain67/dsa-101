class Trie:
    def __init__(self):
        self.children  = [None]*26
        self.wordEnd = False
    
    def insert(self, word):
        curr = self
        index = 0
        while index < len(word):
            chIndex = ord(word[index]) - ord('a')
            if curr.children[chIndex] == None:
                curr.children[chIndex] = Trie()
            curr = curr.children[chIndex]
            index += 1
        curr.wordEnd = True
    
    def hasPrefix(self, word):
        curr = self
        index = 0
        while index < len(word):
            chIndex = ord(word[index]) - ord('a')
            if curr.children[chIndex] == None:
                return False
            curr = curr.children[chIndex]
            index += 1
        return True
    
    def hasWord(self, word):
        curr = self
        index = 0
        while index < len(word):
            chIndex = ord(word[index]) - ord('a')
            if curr.children[chIndex] == None:
                return False
            curr = curr.children[chIndex]
            index += 1
        return curr.wordEnd

class Solution:
    directions = [[-1,0],[1,0],[0,1],[0,-1]]
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            t.insert(word)
        allWords = set()
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                # self.find(board, row, col, t, "", visited, allWords)
                self.findOptimised(board, row, col, t, "", visited, allWords)
        return list(allWords)

    def findOptimised(self, board, i, j, t, word, visited, allWords):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])) or visited[i][j]:
            return
        ch = board[i][j]
        chIndex = ord(ch) - ord('a')
        if t.children[chIndex] is None:
            return
        t = t.children[chIndex]
        word += ch
        if t.wordEnd:
            allWords.add(word)
        visited[i][j] = True
        for dirc in self.directions:
            ni = i+dirc[0]
            nj = j+dirc[1]
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and not visited[ni][nj]:
                self.findOptimised(board, ni, nj, t, word, visited, allWords)
        visited[i][j] = False
        
    def find(self, board, i, j, t, word, visited, allWords):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])) or visited[i][j]:
            return
        word += board[i][j]
        if not t.hasPrefix(word):
            return
        if t.hasWord(word):
            allWords.add(word)
        visited[i][j] = True
        for dirc in self.directions:
            ni = i+dirc[0]
            nj = j+dirc[1]
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and not visited[ni][nj]:
                self.find(board, ni, nj, t, word, visited, allWords)
        visited[i][j] = False
