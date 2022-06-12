import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        ans = heapq.nlargest(k,nums)
        return ans[-1]
