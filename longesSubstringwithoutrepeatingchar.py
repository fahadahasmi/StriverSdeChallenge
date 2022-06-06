#soln 1:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        n = len(s)
        maxL= 0
        hSet = set()
        for i in range(n):
            
            if s[i] in hSet:
                
                while l<i and s[i] in hSet:
                    hSet.remove(s[l])
                    l+=1
            
            hSet.add(s[i])
            maxL = max(maxL,i-l+1)
        
        return maxL
  #soln 2:
  
  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        n = len(s)
        maxL= 0
        hSet = {}
        for i in range(n):
            
            if s[i] in hSet:
                l = max(l,hSet[s[i]]+1)
            
            hSet[s[i]] = i
            maxL = max(maxL,i-l+1)
        
        return maxL
