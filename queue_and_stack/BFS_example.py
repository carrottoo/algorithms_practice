"""
    A example of using bfs to solve a problem of finding the number of islands in a given 2d grid of '0' (water) and '1'(land). 
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. Assume that all four edges of the grid are all surrounded by water.

    Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    Output: 1
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    visited |= self.bfs(i,j, grid)
                    islands += 1
        return islands
                           
    
    def bfs(self,i, j, grid):
        queue = []
        explored = set()
        queue.append((i, j))
        explored.add((i, j))

        direction = [(1,0), (-1,0), (0, 1), (0,-1)]
        k = 0
        while k < len(queue):
            x, y = queue[k]
            for m, n in direction:
                if x + m < len(grid) and y + n < len(grid[0]) and x + m >= 0 and y + n >= 0 and grid[x+m][y+n] == '1' and (x+m, y+n) not in explored:
                    queue.append((x+m, y+n))
                    explored.add((x+m,y+n))
            k += 1
        return explored 