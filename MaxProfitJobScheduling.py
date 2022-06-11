class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = list(zip(startTime,endTime,profit))
        
        jobs.sort()
        dp = [-1]*n
        def helper(i):
            if i==n:
                return 0
            if dp[i] != -1:
                return dp[i]
            k = i+1
            while k<n and jobs[i][1] > jobs[k][0]:
                k+=1
            take = helper(k)+jobs[i][2]
            notTake = helper(i+1)
            dp[i] = max(take,notTake)
            return dp[i]
        
        ans = helper(0)
        return ans
