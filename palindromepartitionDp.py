#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here
        def isPal(s):
            if len(s)==1:
                return True
            elif s == s[::-1]:
                return True
            return False
        
        def helper(s,i,j,dp):
            if i>=j or isPal(s[i:j+1]):
                return 0
            
               
            mn = float("inf") 
            for k in range(i,j):
                if not isPal(s[i:k+1]):
                    continue
                if dp[i][k] != -1:
                    l = dp[i][k]
                else:
                    l = helper(s,i,k,dp)
                if dp[k+1][j] != -1:
                    r = dp[k+1][j]
                else:
                    r= helper(s,k+1,j,dp)
                ans  = 1+l+r
                mn = min(mn,ans)
            dp[i][j] = mn
            
            return dp[i][j]
        
        n = len(string)
        dp = [[-1 for x in range(n)]for y in range(n)]
        res = helper(string,0,n-1,dp)
        return res
