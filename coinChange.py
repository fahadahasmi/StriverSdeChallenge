from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def countWaysToMakeChange(denominations, value) :
    def helper(arr,i,t,dp):
        if i==0:
            if (t%arr[0]==0):
                return 1
            else:
                return 0
        if dp[i][t] != -1:
            return dp[i][t]
        take = 0
        nonTake = helper(arr,i-1,t,dp)

        if arr[i]<=t:
            take = helper(arr,i,t-arr[i],dp)

        dp[i][t] = take+nonTake
        return dp[i][t]
    
    dp = [[-1 for x in range(value+1)]for y in range(len(denominations))]
    ans= helper(denominations,len(denominations)-1,value,dp)
    return ans



#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))
