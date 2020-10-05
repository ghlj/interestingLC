# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:33:53 2020

@author: ljpsy
"""

from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r,c = click[0],click[1]
        h,w = len(board),len(board[0])
        directions = [(i,j) for i in range(-1,2) for j in range(-1,2) if i or j]
          
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        import collections
        q = collections.deque()
        q.append((r,c))
        seen = set()
        while q:
            tr,tc = q.popleft()
            if board[tr][tc] == 'E':
                nmines = sum(board[tr+i][tc+j]=='M' for i,j in directions if h>tr+i>=0 and w>tc+j>=0)
                board[tr][tc] = str(nmines or 'B')
                if nmines==0:
                    for i, j in directions:
                        x, y = tr+i, tc+j
                        if h>x>=0 and w>y>=0 and board[x][y]=='E' and (x,y) not in seen:
                            q.append((x,y))
                            seen.add((x,y))

        return board