#first Solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def helper(nums,c):
            
            if c== nums[c]:
                return c
            next = nums[c]
            nums[c] = c
            return helper(nums,next)
        
        ans = helper(nums,0)
        return ans
      
  #Second Solution
  class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
 
#Third Solution 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s,f,find=0,0,0
        while True:
            s = nums[s]
            f =nums[nums[f]]
            if s==f:
                while find!=s:
                    s = nums[s]
                    find = nums[find]
                return find
