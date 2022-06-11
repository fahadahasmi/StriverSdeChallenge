#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this function
    
    def helper(s,i,dp):
        if i==len(s):
            return 1
        
        for x in range(len(s)):
            for j in dictionary:
                if s[i:x+1] == j:
                    if helper(s,x+1,dp):
                        dp[x] = 1
                        return dp[x]
        
        dp[i] = 0
        return dp[i]
    
    dp = [-1]*len(line)
    ans = helper(line,0,dp)
    return ans
    
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        number_of_elements = int(input())
        dictionary = [word for word in input().strip().split()]
        line = input().strip()
        res = wordBreak(line, dictionary)
        if res:
            print(1)
        else:
            print(0)
# } Driver Code Ends
