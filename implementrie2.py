class Node:
    
    def __init__(self):
        self.link = [None]*26
        self.ew = 0
        self.count = 0
    
    def containsKey(self,ch):
        return self.link[ord(ch)-ord('a')] != None
    
    def getNode(self,ch):
        return self.link[ord(ch)-ord('a')]
    
    def put(self,ch,Node):
        self.link[ord(ch)-ord('a')] = Node
    
    def incEnd(self):
        self.ew += 1
    
    def incPref(self):
        self.count += 1
    
    def delEnd(self):
        self.ew -= 1
    
    def redPref(self):
        self.count -= 1
    
    def getEnd(self):
        return self.ew
    
    def getCount(self):
        return self.count
   
    
    
        
    
    
    
class Trie:
    def __init__(self):
        # Write your code here.
        self.root = Node()

    def insert(self, word):
        # Write your code here.
        temp = self.root
        for i in word:
            if not temp.containsKey(i):
                temp.put(i,Node())
            temp = temp.getNode(i)
            temp.incPref()
        temp.incEnd()

    def countWordsEqualTo(self, word):
        temp = self.root
        for i in word:
            if not temp.containsKey(i):
                return 0
            else:
                 temp = temp.getNode(i)
        return temp.getEnd()

    def countWordsStartingWith(self, word):
        temp = self.root
        for i in word:
            if not temp.containsKey(i):
                return 0
            else:
                 temp = temp.getNode(i)
        return temp.getCount()

    def erase(self, word):
        # Write your code here.
        temp = self.root
        for i in word:
            if not temp.containsKey(i):
                return 
            else:
                temp = temp.getNode(i)
                temp.redPref()
                  
        temp.delEnd()
