# Memoization 
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        
        def helper(arr,i,j,dp):
            if i==j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
                
            mn = float("inf")
            for k in range(i,j):
                ans = (arr[i-1]*arr[k]*arr[j])+helper(arr,i,k,dp)+helper(arr,k+1,j,dp)
                mn = min(mn,ans)
                dp[i][j] = mn
            return dp[i][j]
        
        dp = [[-1 for x in range(N)]for y in range(N)]
        res = helper(arr,1,N-1,dp)
        return res
#Bottom-Up

class Solution:
    def matrixMultiplication(self, N, arr):
        dp = [[0 for x in range(N)]for y in range(N)]
        
        for i in range(N):
            dp[i][i] =0
            
        
        for i in range(N-1,0,-1):
            for j in range(i+1,N):
                mn = float("inf")
                for k in range(i,j):
                    ans = (arr[i-1]*arr[j]*arr[k]) + dp[i][k]+dp[k+1][j]
                    if ans<mn:
                        mn = ans
                dp[i][j] = mn 
                
        return dp[1][N-1]
