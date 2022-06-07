class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0
        res= []
        n = len(nums)
        for i in range(n):
            ind = bisect.bisect_right(res,2*nums[i])
            ans += len(res) - ind
            bisect.insort(res,nums[i])
        
        return ans
