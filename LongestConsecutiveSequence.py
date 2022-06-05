class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longStreak = 0
        s = set(nums)
        
        for i in nums:
            
            if i-1 not in s:
                curNum = i
                curStreak = 1
                
                while curNum+1 in s:
                    curStreak += 1
                    curNum += 1
                
                longStreak = max(longStreak,curStreak)
        
        return longStreak
