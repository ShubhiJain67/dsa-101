from typing import List
class Solution:
    directions = [[-1, 0],[1, 0], [0, -1], [0, 1]]
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not visited[i][j] and self.exitRec(board, i, j, visited, word, 0):
                    return True
        return False
        
    def exitRec(self, board, i, j, visited, word, index):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        if visited[i][j]:
            return False
        if board[i][j] != word[index]:
            return False
        visited[i][j] = True
        for direction in self.directions:
            if self.exitRec(board, i+direction[0], j+direction[1], visited, word, index+1):
                visited[i][j] = False
                return True
        visited[i][j] = False
        return False
