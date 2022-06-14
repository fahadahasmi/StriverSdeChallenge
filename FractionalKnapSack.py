
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        # code here
        Items.sort(key=lambda x: x.value/x.weight,reverse=True)
        profit = 0
        for i in Items:
            if i.weight < W:
                profit+=i.value
                W-=i.weight
            elif W>0:
                profit += i.value*(W/i.weight)
                W=0
                break
            else:
                break
        
        return profit
