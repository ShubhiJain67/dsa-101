from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.leftDiagonals = [False for _ in range(n*2-1)]
        self.rightDiagonals = [False for _ in range(n*2-1)]
        self.rows = [False for _ in range(n)]
        self.cols = [False for _ in range(n)]
        board = [['.']*n for _ in range(n)]
        return self.solve(n, board, 0, 0, n)
        
    def solve(self, n, board, row, col, queensToBePlaced):
        if queensToBePlaced == 0:
            return [self.transformBoard(board)]
        if row == n:
            return []
        allBoards = []
        if self.canPlace(row, col, n):
            self.placeQueen(board, row, col, n)
            boards = self.solve(n, board, row + 1, 0, queensToBePlaced-1)
            for b in boards:
                allBoards.append(b)
            self.removeQueen(board, row, col, n)

        nRow = row + 1 if col == n - 1 else row
        nCol = col + 1 if col < n -1 else 0
        boards = self.solve(n, board, nRow, nCol, queensToBePlaced)
        for b in boards:
            allBoards.append(b)
        return allBoards
        
    def placeQueen(self, board, row, col, n):
        leftDiagonal = self.getLeftDiagonal(row, col, n)
        rightDiagonal = self.getRightDiagonal(row, col, n)
        self.leftDiagonals[leftDiagonal] = True
        self.rightDiagonals[rightDiagonal] = True
        self.rows[row] = True
        self.cols[col] = True
        board[row][col] = "Q"

    def removeQueen(self, board, row, col, n):
        leftDiagonal = self.getLeftDiagonal(row, col, n)
        rightDiagonal = self.getRightDiagonal(row, col, n)
        self.leftDiagonals[leftDiagonal] = False
        self.rightDiagonals[rightDiagonal] = False
        self.rows[row] = False
        self.cols[col] = False
        board[row][col] = "."

    def canPlace(self, row, col, n):
        leftDiagonal = self.getLeftDiagonal(row, col, n)
        rightDiagonal = self.getRightDiagonal(row, col, n)
        if self.leftDiagonals[leftDiagonal]:
            return False
        if self.rightDiagonals[rightDiagonal]:
            return False
        if self.rows[row]:
            return False
        if self.cols[col]:
            return False
        return True

    def getLeftDiagonal(self, row, col, n):
        i = row
        j = col
        while i > 0 and j > 0:
            i -= 1
            j -= 1
        return n - 1 - i + j

    def getRightDiagonal(self, row, col, n):
        i = row
        j = col
        while i > 0 and j < n - 1:
            i -= 1
            j += 1
        return i + j
    
    def transformBoard(self, board):
        b = []
        for row in board:
            placement = ""
            for col in row:
                placement += col
            b.append(placement)
        return b
