def maxProfit(values, weights, n, w):
    
    dp = [[0 for x in range(w+1)]for y in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,w+1):
            if weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j],values[i-1]+dp[i-1][j-weights[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[-1][-1]

  
