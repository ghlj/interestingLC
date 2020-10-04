# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 16:58:10 2020

@author: ljpsy
"""
from typing import List
class Solution:
    def _guess(self,board):
        '''
        keep guessing using depth first search
        when todo list is finished in one search, return True and determinate the search
        backtrack if failed (i.e., not reaching the end due to conflict)
        '''
        import heapq
        if not self.todo: return True
        _,(row,col) = heapq.heappop(self.todo)
        #if board[row][col] != '.': return guess(n+1)
        sol = self.rowsol[row].intersection(self.colsol[col]).intersection(self.boxsol[row//3][col//3])
        #if len(sol) == 0: return False
        for ans in sol:
            board[row][col] = ans
            self.rowsol[row].remove(ans)
            self.colsol[col].remove(ans)
            self.boxsol[row//3][col//3].remove(ans)
            succeed = self._guess(board)
            if succeed: return True
            else:
                #back track
                self.rowsol[row].add(ans)
                self.colsol[col].add(ans)
                self.boxsol[row//3][col//3].add(ans)
                board[row][col] = '.'
        heapq.heappush(self.todo,[len(sol),(row,col)] ) 
        return False
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        compute the possible solutions for each cell and keep them in a to-do list
        maintain the todo list as a minheap so that the cell with the least options get to be guessed first.
        In this way, the overall searching time is optimized
        """
        #initialize the solution for each row, col and box as '1-9'
        self.rowsol = [set(str(i) for i in range(1,10)) for _ in range(9) ]
        self.colsol = [set(str(i) for i in range(1,10)) for _ in range(9) ]
        self.boxsol = [[set(str(i) for i in range(1,10)) for _ in range(3) ] for _ in range(3) ]
        #remove the digits that has already appeared for each row, col and box
        for row in range(9):
            for col in range(9):
                if board[row][col] in self.rowsol[row]: self.rowsol[row].remove(board[row][col])
                if board[row][col] in self.colsol[col]: self.colsol[col].remove(board[row][col])
                if board[row][col] in self.boxsol[row//3][col//3]: self.boxsol[row//3][col//3].remove(board[row][col])
        
        # construct the solution space for each cell as a todo list
        self.todo = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    sol = self.rowsol[row].intersection(self.colsol[col]).intersection(self.boxsol[row//3][col//3])
                    self.todo.append([len(sol),(row,col)])
        
        # use a minheap to maintain the todo list so that we can do the least option cell first
        import heapq
        heapq.heapify(self.todo)
        
        self._guess(board)

