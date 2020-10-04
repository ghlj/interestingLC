# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:27:25 2020

@author: ljpsy
"""
from typing import List
def minCostConnectPoints(self, points: List[List[int]]) -> int:
    '''
    prim's algorithm.
    for each left over points:
        add the new point with shortest edge to the tree.
        use the edges to the new point to update the shortest edge to the tree for each of the left over points.
    '''
    cost = 0
    Left_over_points_minEdge = [(abs(points[i][0]-points[0][0])+abs(points[i][1]-points[0][1]),0,i) for i in range(1,len(points))]
    import heapq
    heapq.heapify(Left_over_points_minEdge)
    #mst = [] # to store the minimal spanning tree. Not necessary here.
    while Left_over_points_minEdge: # K for K in N-1... 1
        shortest, frm, to = heapq.heappop(Left_over_points_minEdge) #(O(1))
        cost += shortest
        #mst.append((frm,to))
        
        # "add or rather use" new edges from "to" and update the min distance to the tree
        for pos,(d, _, i ) in enumerate( Left_over_points_minEdge ): #O(K-1)
            dist = abs(points[i][0]-points[to][0])+abs(points[i][1]-points[to][1])
            if dist < d:
                Left_over_points_minEdge[pos] = (dist,to,i)
                heapq._siftdown(Left_over_points_minEdge,0,pos) #(O(log(K))
        
        #heapq.heapify(Left_over_points_minEdge) #O(K-1)
        
    #print(mst)    
    return cost
