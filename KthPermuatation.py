#1st Solution
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [i for i in range(1,n+1)]
        p = permutations(arr)
        
        ans = []
        for i in p:
            ans.append(i)
        
        res = ans[k-1]
        s = ""
        for i in res:
            s+=str(i)
        
        return s
#2nd Solution 
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        numb = []
        
        fact = 1
        for i in range(1,n):
            numb.append(i)
            fact = fact*i
        
        numb.append(n)
        k = k-1
        
        while True:
            ans = ans + str(numb[k//fact])
            numb.pop(k//fact)
            
            if len(numb)==0:
                break
            k = k%fact
            
            fact = fact//len(numb)
        
        return ans
