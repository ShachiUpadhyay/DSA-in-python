#https://leetcode.com/problems/minimum-knight-moves/editorial/?envType=company&envId=uber&favoriteSlug=uber-thirty-days

# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


# Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

# Example 1:

# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
# Example 2:

# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

# Constraints:

# -300 <= x, y <= 300
# 0 <= |x| + |y| <= 300
 

from collections import deque
class Solution:
    def minKnightMoves(self, tx: int, ty: int) -> int:
        if tx == 0 and ty==0:
            return 0
        visited: Set[Tuple[int, int]] = set()
        queue: deque[tuple[int, int]] = deque()
        dir = [(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,1),(2,-1)]

        queue.append((0,0))
        visited.add((0,0))
        steps: int = 0
        while queue:
            ql = len(queue)
            steps += 1
            for _ in range(ql):
                x,y = queue.popleft()       
                for dx, dy in dir:
                    nx = x + dx
                    ny = y + dy

                    if nx == tx and ny == ty:
                        return steps
                    else:
                        if (nx, ny) not in visited:
                            queue.append((nx, ny))
                            visited.add((nx, ny))

        return -1


        





        