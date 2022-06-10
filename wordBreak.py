class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def helper(s,i,n,dp):
            if i==n:
                return True
            
            if dp[i] != -1:
                return dp[i]
            
            for x in range(i,n):
                for w in range(len(wordDict)):
                    if s[i:x+1] == wordDict[w]:
                        if helper(s,x+1,n,dp):
                            dp[i] = True
                            return dp[i]
            
            dp[i] = False
            return dp[i]
        
        n = len(s)
        dp = [-1]*(n+1)
        
        res = helper(s,0,n,dp)
        return res
