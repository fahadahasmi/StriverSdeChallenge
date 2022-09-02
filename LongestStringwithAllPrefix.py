from typing import *
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
        
        

    def checkExists(self, word: str) -> bool:
        temp = self.root
        f = True
        for i in range(len(word)):
            ind = self.__getNext(word[i])
            
            if not temp.link[ind]:
                return False
            else:
                temp = temp.link[ind]
                f = f & temp.flag
        
        return f

def completeString(n: int, a: List[str])-> str:
    
    # Write your Code here
    longest = ""
    
    t = Trie()
    
    for i in a:
        t.insert(i)
        
    for i in a:
        
        if t.checkExists(i):
            if len(i) > len(longest):
                longest = i
            elif len(i) == len(longest) and longest > i:
                longest = i
    if not longest:
        return None
    return longest
    
    
    
