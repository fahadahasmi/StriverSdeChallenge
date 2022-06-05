class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = float("-inf")
        
        countOnes = 0
        n = len(nums)
        for i in range(n):
            
            if nums[i] == 0:
                countOnes = 0
            else:
                countOnes += 1
            maxOne = max(maxOne,countOnes)
        
        return maxOne
