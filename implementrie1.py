class Node:
    
    def __init__(self):
        self.link = [None] * 26
        self.flag = False
        

class Trie:

    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        n = Node()
        return n
    
    def __getNext(self,ch):
        return ord(ch) - ord('a')
        

    def insert(self, word: str) -> None:
        temp = self.root
        for i in range(len(word)):
            ind = self.__getNext(word[i])
            
            if not temp.link[ind]:
                temp.link[ind] = self.getNode()
            temp = temp.link[ind]
        
        temp.flag = True
        
        

    def search(self, word: str) -> bool:
        temp = self.root
        for i in range(len(word)):
            ind = self.__getNext(word[i])
            
            if not temp.link[ind]:
                return False
            temp = temp.link[ind]
        
        return temp.flag
        
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        
        for i in prefix:
            ind = self.__getNext(i)
            if not temp.link[ind]:
                return False
            temp = temp.link[ind]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
