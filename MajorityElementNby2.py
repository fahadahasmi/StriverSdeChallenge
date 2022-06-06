class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        for i in range(n):
            
            if c[nums[i]] > n/2:
                return nums[i]
