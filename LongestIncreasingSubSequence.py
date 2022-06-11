#solution one with TC: O(n*n) gives TLE

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        arr = list(set(nums))
        arr.sort()
        
        m = len(nums)
        n = len(arr)
        
        dp = [[0 for x in range(n+1)]for y in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if nums[i-1] == arr[j-1]:
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[-1][-1]

#solution two
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1]*n
        
        for i in range(n):
            for j in range(i):
                
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        
        return max(dp)
