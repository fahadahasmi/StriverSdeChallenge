class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r = 1
        n =  len(prices)
        maxProfit = 0
        while r < n:
            cProfit = prices[r] - prices[l]
            
            if prices[l] < prices[r]:
                maxProfit = max(cProfit,maxProfit)
            else:
                l = r
            r+=1
        
        return maxProfit
