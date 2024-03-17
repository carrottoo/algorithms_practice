"""
    A example of using bfs to traversal through a 2d grid of '0' (water) and '1'(land) to find the number of islands. 
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

def numIslands(grid: List[List[str]]) -> int:
    islands = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and (i, j) not in visited:
                visited |= bfs(i,j, grid)
                islands += 1
    return islands
                        
    
def bfs(i, j, grid):
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
    
"""
    An example of using BFS to find the shortest path in a lock opening problem

    Problem description:
    You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 

    The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the 4 wheels.

    You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

    Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

    Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
    Output: 6

"""
def openLock(deadends: List[str], target: str) -> int:
    # finding the shortest path to the target 
    deadends = set(deadends)
    step = 0
    queue = []
    explored = set()
    queue.append(((0, 0, 0, 0), step))
    explored.add((0, 0, 0, 0))
    
    move = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (-1, 0, 0, 0), (0, -1, 0, 0),
            (0, 0, -1, 0), (0, 0, 0, -1)]
    
    k = 0
    
    if '0000' in deadends:
        return -1
    
    while k < len(queue):
        cur = queue[k][0]
        step = queue[k][1]
        cur_str = str(cur[0]) + str(cur[1]) + str(cur[2]) + str(cur[3])
        
        if cur_str == target:
            return step
        
        for x, y, m, n in move:
        
            check_end = ((cur[0] + x + 10) % 10, (cur[1] + y + 10) % 10, (cur[2] + m + 10) % 10, (cur[3] + n + 10) % 10) 
            
            check_end_str = str(check_end[0]) + str(check_end[1]) + str(check_end[2]) + str(check_end[3])
            
            if check_end_str not in deadends and check_end not in explored:
                queue.append((check_end, step + 1))
                explored.add(check_end)
        
        k += 1
        
    return -1