class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        left= nums[0]
        right = nums[0]
        isZero = False
        
        p = 1
        for i in range(len(nums)):
            p*= nums[i]
            
            if nums[i]==0:
                p=1
                isZero =True
                continue
            left = max(left,p)
        
        p = 1
        for i in range(len(nums)-1,-1,-1):
            p*= nums[i]
            
            if nums[i]==0:
                p=1
                isZero =True
                continue
            right = max(right,p)
        
        if isZero:
            return max(max(left,right),0)
        
        return max(left,right)
        
        
