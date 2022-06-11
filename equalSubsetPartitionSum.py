class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        
        s = sum(nums)//2
        
        dp = [[False for x in range(s+1)]for y in range(len(nums)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                
                if i==0 and j==0:
                    dp[i][j] = True
                elif i==0:
                    dp[i][j] = False
                elif j==0:
                    dp[i][j] = True
                else:
                    if dp[i-1][j]==False:
                        if nums[i-1] <= j:
                            dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                        else:
                            dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
        
        return dp[-1][-1]
