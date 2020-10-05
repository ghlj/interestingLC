# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:43:37 2020

@author: ljpsy
"""

from typing import List
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        use disjoint set method to keep track if a vertex is connected to a set (tree)
        apply the method for different types of edge in this context
        always keep type 3 edge if possible
        '''
        edges123 = [[]  for _ in range(3) ] 
        for t, a, b in edges: edges123[t-1].append( (a-1,b-1) )
        # type 0 1 2 for alice, bob and both
        self.res = 0
        Parents = [[i for i in range(n)] for _ in range(2) ]
        depth = [[1]*n for _ in range(2)]
        selectedEdges = [0,0]
        def FindRoot(n,t):
            '''
            Path compression by two pass method.
            find the root ID and also propagate the parent ID back!
            '''
            if Parents[t][n] != n:
                Parents[t][n] = FindRoot(Parents[t][n] ,t)
            return Parents[t][n] 
        def Union(x,y,t):
            '''
            Union rank to reduce run time.
            if not connected, connect the short tree to the taller tree, return True
            else, don't connect and return False (i.e., don't need to connect)
            '''
            rx, ry = FindRoot(x,t), FindRoot(y,t)
            if rx == ry: return False
            else:
                if depth[t][rx] >= depth[t][ry]:
                    Parents[t][ry] = rx
                    depth[t][rx] = max(depth[t][rx],depth[t][ry])
                else:
                    Parents[t][rx] = ry
                return True
            
        def connect(thetype):
            '''
            for the input type of edge, try to unite and keep track of the selected edges
            if already connected, then that edge can be deleted.
            In the end, there should be n-1 edges connecting n points.
            '''
            mytypes = [thetype] if thetype < 2 else [ 0, 1 ]
            for x, y in edges123[thetype]:
                if all(Union(x,y,t) for t in mytypes):
                    for t in mytypes: selectedEdges[t] += 1
                else:
                    self.res += 1
            # for t in mytypes: 
            #     root = [FindRoot(i,t) for i in range(n)]
            #     print(thetype,t, 'parents',Parents[t],root,selectedEdges,self.res)
                
        connect(2)
        connect(0)
        connect(1)
        return self.res if all(selectedEdges[t]==n-1 for t in [0,1]) else -1