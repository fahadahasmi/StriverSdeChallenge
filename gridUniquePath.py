class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        def helper(i,j,dp):
            
            if  i==0 and j==0:
                return 1
            
            if j<0:
                return 0
            if i<0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            top = helper(i-1,j,dp)
            left = helper(i,j-1,dp)
            
            dp[i][j] = top+left
            
            return dp[i][j]
        
        dp = [[-1 for x in range(n)]for y in range(m)]
        ans = helper(m-1,n-1,dp)
        
        return ans
            
            
