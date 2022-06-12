class MedianFinder:
    def __init__(self):
        self.n = []
        
    def addNum(self, num: int) -> None:
        self.n.append(num)

    def findMedian(self) -> float:
        self.n.sort()
        l = len(self.n)
        m = (0+l)//2
        if l%2==0:
            return (self.n[m]+self.n[m-1]) / 2 
        else:
            return self.n[m]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
