class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = {}
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] in c:
                c[nums[i]] += 1
            else:
                c[nums[i]] = 1
            if c[nums[i]] > n//3:
                ans.append(nums[i])
                c[nums[i]] = -1
        
        return ans
        
