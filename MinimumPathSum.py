#Memoization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        def helper(m,i,j,dp):
            
            if i==0 and j==0:
                return m[i][j]
            
            if i<0 or j<0:
                return float("inf")
            if dp[i][j] != -1:
                return dp[i][j]
            top = m[i][j]+helper(m,i-1,j,dp)
            left = m[i][j]+helper(m,i,j-1,dp)
            
            dp[i][j] = min(top,left)
            return dp[i][j]
        
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for x in range(n)]for y in range(m)]
        ans = helper(grid,m-1,n-1,dp)
        return ans
 #Bottom up
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float("inf") for x in range(n)]for y in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = min(grid[i][j]+dp[i-1][j],grid[i][j]+dp[i][j-1])
        
        return dp[-1][-1]
