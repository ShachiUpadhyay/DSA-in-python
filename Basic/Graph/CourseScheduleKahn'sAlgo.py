#https://neetcode.io/problems/course-schedule/question?list=neetcode250
from typing import List, Dict
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adj : dict[int, List[int]] = {}
        queue = deque()

        for a,b in prerequisites:
            indegree[a] += 1
            if b not in adj:
                adj[b] = []
            
            adj[b].append(a)
        
        completed : int = 0
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            completed += 1
            for neighbour in adj.get(curr,[]):
                indegree[neighbour] = indegree[neighbour] - 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        
        return completed == numCourses
        
       

        
        