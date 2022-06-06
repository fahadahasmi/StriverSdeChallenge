class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = 0
        mSum = float("-inf")
        n =  len(nums)
        for i in range(n):
            
            csum += nums[i]
            mSum = max(mSum,csum)
            if csum <0 :
                csum = 0
            
            
        
        return mSum
