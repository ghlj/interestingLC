# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 21:26:32 2020
@author: ljpsy
"""
class Solution:
    #@functools.lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        for each edit, continue to put all the possible edits in a todo list
        search until the two words become the same.
        Breadth first search ensures to return the shortest "depth"
        '''
        stack = [(word1,word2)]
        depth = 0 # BFS depth, which is the current edits
        #possible = []
        seen = set()
        while stack:
            newstack = []
            #print(depth, stack)
            
            for w1, w2 in stack:
                i = 0
                while i < min(len(w1),len(w2)) and w1[i] == w2[i]: i+=1
                    
                if i == len(w1) and i == len(w2):
                    return depth + abs(len(w1)-len(w2))
                    #possible.append( depth + abs(len(w1)-len(w2)) )
                else:
                    if (w1[i:],w2[i+1:]) not in seen:
                        newstack.append((w1[i:],w2[i+1:])) # deletion
                        seen.add((w1[i:],w2[i+1:]))
                    if (w1[i+1:],w2[i+1:]) not in seen:
                        newstack.append((w1[i+1:],w2[i+1:])) # replacement
                        seen.add((w1[i+1:],w2[i+1:]))
                    if (w1[i+1:],w2[i:]) not in seen:
                        newstack.append((w1[i+1:],w2[i:])) # insertion
                        seen.add((w1[i+1:],w2[i:]))
                    
            #if len(possible)>0: return min(possible)
            depth += 1    
            stack = newstack
        
        #return min(possible)