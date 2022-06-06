from os import *
from sys import *
from collections import *
from math import *

def missingAndRepeating(arr, n):
    # Write your code here
    s = n*(n+1)//2
    sS = n*(n+1)*(2*n+1)//6
    
    for i in range(n):
        s -= arr[i]
        sS -= arr[i] * arr[i]
        
    missNo = (s + sS//s)//2
    repeatNo = missNo - s
    
    return [missNo,repeatNo]
