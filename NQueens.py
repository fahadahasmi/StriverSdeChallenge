class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def check(board,row,col):
            
            i = col
            while i>=0:
                if board[row][i]:
                    return False
                i-=1 
            
            i=row
            j=col
            
            while i>=0 and j>=0:
                if board[i][j]:
                    return False
                i-=1
                j-=1
            
            i=row
            j=col
            while i<n and j>=0:
                if board[i][j]:
                    return False
                i+=1
                j-=1
            
            return True
        
        def solve(board,ind):
            if ind==n:
                ans.append([])
                for i in range(n):
                    ans[-1].append("")
                    for j in range(n):
                        if board[i][j]:
                            ans[-1][-1] += "Q"
                        else:
                            ans[-1][-1] += "."
                            
                return
            
            for i in range(n):
                if check(board,i,ind):
                    board[i][ind] = 1
                    solve(board,ind+1)
                    board[i][ind] = 0
            return 
        
        ans = []
        board = [[0 for x in range(n)]for y in range(n)]
        solve(board,0)
        board.clear()
        return ans
                        
