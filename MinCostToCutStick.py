#memoization
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        def helper(arr,i,j,dp):
            if i>j:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            mn = float("inf")
            for k in range(i,j+1):
                cost = (arr[j+1] - arr[i-1]) + helper(arr,i,k-1,dp) + helper(arr,k+1,j,dp)
                mn = min(mn,cost)
            
            dp[i][j] = mn
            return dp[i][j]
        
        cuts.extend([0,n])
        cuts.sort()
        c = len(cuts)
        dp = [[-1 for x in range(c+1)]for y in range(c+1)]
        ans = helper(cuts,1,c-2,dp)
        return ans
      
 #Tabulation

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0,n])
        cuts.sort()
        c = len(cuts)
        dp = [[0 for x in range(c+1)]for y in range(c+1)]
        
        for i in range(c,0,-1):
            for j in range(1,c-1):
                if i>j:
                    continue
                
                mn = float("inf")
                for k in range(i,j+1):
                    ans = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]
                    mn = min(ans,mn)
                
                dp[i][j] = mn
        
        return dp[1][c-2]
