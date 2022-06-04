from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    m  = len(matrix)
    n = len(matrix[0])
    r = set()
    c = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                r.add(i)
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                c.add(j)
    
    for i in range(m):
        for j in range(n):
            if i in r:
                matrix[i][j] = 0
    
    for i in range(m):
        for j in range(n):
            if j in c:
                matrix[i][j] = 0
     
                
    
