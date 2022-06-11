#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        
        def helper(egg,floor,dp):
            
            if egg == 0 or floor==0:
                return 0
            if egg == 1 or floor == 1:
                return floor
                
            if dp[egg][floor] != -1:
                return dp[egg][floor]
            
            mn = float("inf")
            
            for x in range(1,floor+1):
                ans = 1+ max(helper(egg-1,x-1,dp),helper(egg,floor-x,dp))
                mn = min(mn,ans)
            
            dp[egg][floor] = mn
            return dp[egg][floor]
        
        dp = [[-1 for x in range(k+1)]for y in range(n+1)]
        res = helper(n,k,dp)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends
