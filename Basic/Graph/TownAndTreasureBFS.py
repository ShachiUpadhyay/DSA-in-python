#https://neetcode.io/problems/islands-and-treasure/question
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        visited: List[List[bool]] = [[False for _ in range(m)] for _ in range(n)]

        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited[i][j] = True
        
        dist : int = 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            dist += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<n and 0<=ny<m and visited[nx][ny]== False and grid[nx][ny] == 2147483647:
                        visited[nx][ny] = True
                        grid[nx][ny] = dist
                        queue.append((nx,ny))
        

            


                
        