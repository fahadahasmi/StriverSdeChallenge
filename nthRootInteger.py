def findNthRootOfM(n,m):
    l,r=1,m+1
    
    ep = 1e-8
    
    while abs(r-l) > ep:
        mid = (l+r)/2.0
        
        if mul(mid,n) < float(m):
            l = mid
        else:
            r = mid
    
    l = "{:.6f}".format(l)
    return l

def mul(numb,n):
    ans = 1.00
    for i in range(1,n+1):
        ans*=numb
    return ans
