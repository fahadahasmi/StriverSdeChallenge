denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    i = len(denominations)-1
    ans = [] 
    while i>=0:
        while amount>=denominations[i]:
            amount -= denominations[i]
            ans.append(denominations[i])
        i-=1
    return len(ans)
    
