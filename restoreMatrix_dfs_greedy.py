# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:18:58 2020

@author: ljpsy
"""


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ''' dfs search through the possibilities and early termination'''
        n , m = len(rowSum), len(colSum)
        res = [ [0]*m for _ in range(n) ] # the matrix
        def dfs(ith):
            # convert ith trial to row and column
            if ith == n*m: return True
            r = ith//m
            c = ith%m
            # what's the largest possibility for this cell?
            # try the largest pssibility first. this is the greedy aspect
            largest = min(rowSum[r], colSum[c])
            for t in range(largest,-1,-1):
                res[r][c] = t
                rowSum[r] -= t
                colSum[c] -= t
                if dfs(ith+1):
                    #early termination with success
                    return True
                #backtracking
                rowSum[r] +=t
                colSum[c] +=t
            
        
        dfs(0)
        return res