class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    self.rows[i].add(board[i][j])
                    self.cols[j].add(board[i][j])
                    self.boxes[(i // 3) * 3 + (j // 3)].add(board[i][j])
        self.solve(board, 0, 0)
        return board
    
    def solve(self, board, row, col):
        if row == 9 :
            return True

        nextRow = row + 1 if col == 8 else row
        nextCol = 0 if col == 8 else col + 1

        if board[row][col] != ".":
            return self.solve(board, nextRow, nextCol)
        for num in "123456789":
            box = (row // 3) * 3 + (col // 3)
            if self.canPlaceOptimised(row, col, box, num):
                board[row][col] = num
                self.cacheNum(row, col, box, num)
                if self.solve(board, nextRow, nextCol):
                    return True
                self.deleteNum(row, col, box, num)
                board[row][col] = "."
        return False

    def canPlaceOptimised(self, row, col, box, num):
        return num not in self.rows[row] and num not in self.cols[col] and num not in self.boxes[box]
        
    def cacheNum(self, row, col, box, num):
        self.rows[row].add(num)
        self.cols[col].add(num)
        self.boxes[box].add(num)
    
    def deleteNum(self, row, col, box, num):
        self.rows[row].remove(num)
        self.cols[col].remove(num)
        self.boxes[box].remove(num)

    def canPlace(self, board, i, j, num):
        for row in range(9):
            if board[row][j] == num:
                return False
        for col in range(9):
            if board[i][col] == num:
                return False
        si = (i // 3) * 3
        sj = (j // 3) * 3
        for row in range(si, si+3):
            for col in range(sj, sj+3):
                if board[row][col] == num:
                    return False
        return True
