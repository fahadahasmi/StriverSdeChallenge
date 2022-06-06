class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        l = 0
        r = n-1
        maxL = 0
        maxR = 0
        total = 0
        while l<=r:
            if height[l] <= height[r]:
                maxL = max(maxL,height[l])
                total += maxL - height[l]
                l+=1
            else:
                maxR = max(maxR,height[r])
                total += maxR - height[r]
                r-=1
                
        return total
