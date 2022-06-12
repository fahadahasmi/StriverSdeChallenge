def mergeKSortedArrays(kArrays, k:int):
    ans = []
    for i in kArrays:
        for j in i:
            ans.append(j)
    ans.sort()
    return ans
