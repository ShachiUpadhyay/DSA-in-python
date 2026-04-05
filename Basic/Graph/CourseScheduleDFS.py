#https://neetcode.io/problems/course-schedule/question

from typing import List, Dict
#DFS + state keeping, finding the cycle in graph
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        state = [0] * numCourses
        ## 0 = not visited
        ## 1 = visiting
        ## 2 = visited

        adj: dict[int, List[int]] = {}

        for a,b in prerequisites:
            if b not in adj:
                adj[b] = []
            adj[b].append(a)

        
        def dfs( node : int) -> bool:
            if state[node] == 1:
                return False
            
            if state[node] == 2:
                return True
            
            state[node] = 1

            for nxt in adj.get(node, []):
                if not dfs(nxt):
                    return False
            
            state[node] = 2

            return True
        
        for node in range(numCourses):
            if state[node] == 0:
                if not dfs(node):
                    return False
        
        return True
                
        