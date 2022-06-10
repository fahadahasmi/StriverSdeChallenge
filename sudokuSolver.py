class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isValid(board,row,col,c):
            
            for i in range(0,9):
                if board[row][i] == c:
                    return False
                
                if board[i][col]==c:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                    return False
            
            return True
        
        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":

                        for c in range(1,9+1):
                            if isValid(board,i,j,str(c)):
                                board[i][j] = str(c)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'

                        return False
        
            return True
        
        solve(board)
        
