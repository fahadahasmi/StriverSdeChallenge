from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ans = []
        
        c = dict(reversed(sorted(c.items(), key=lambda item: item[1])))
        
        i = 0
        for key,val in c.items():
            if i==k:
                break
            ans.append(key)
            i+=1
        
        return ans
        
