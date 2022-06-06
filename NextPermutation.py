class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for x in range(n-1,-1,-1):
            if nums[x] > nums[x-1]:
                break
        
        if x!=0:
            for j in range(n-1,-1,-1):
                if nums[j] > nums[x-1]:
                    break
            
            nums[j],nums[x-1] = nums[x-1],nums[j]
            nums[x:] = reversed(nums[x:])
        else:
            nums.reverse()
