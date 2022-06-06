from os import *
from sys import *
from collections import *
from math import *

def merge(arr,ans,n,l,m,h):
    i = l
    k = l
    j = m+1
    c = 0 
    while i<=m and j<=h:
        if arr[i] <= arr[j]:
            ans[k] = arr[i]
            i+=1
            k+=1
        else:
            ans[k] = arr[j]
            k+=1
            j+=1
            c += m-i+1
   
    while i<=m:
        ans[k] = arr[i]
        i+=1
        k+=1
    
    while j<=h:
        ans[k] = arr[j]
        k+=1
        j+=1
    
    for v in range(l,h+1):
        arr[v] = ans[v]
    
    return c
   

def mergeS(arr,ans,n,l,h):
    invC = 0
    if l<h:
        mid = (l+h)//2
        invC += mergeS(arr,ans,n,l,mid)
        invC += mergeS(arr,ans,n,mid+1,h)
        invC += merge(arr,ans,n,l,mid,h)
    return invC
        

def getInversions(arr, n):
    res = [0]*n
    ans = mergeS(arr,res,n,0,n-1)
    return ans

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))
