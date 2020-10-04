# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:58:28 2020

@author: ljpsy
"""
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        '''take or not take; brute force'''
        flow = [0 for _ in range(n)] 
        
        def dfs(i,accu):
            if i==len(requests):
                if all(f==0 for f in flow): return accu
                else:
                    return 0
            #take
            (frm, to) = requests[i]
            flow[frm]-=1
            flow[to]+=1
            take = dfs(i+1,accu+1)
            #not take
            flow[frm]+=1
            flow[to]-=1
            nottake = dfs(i+1,accu)
            return max(nottake,take)
        
        res = dfs(0,0)
        return res