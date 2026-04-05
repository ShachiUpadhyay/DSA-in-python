#https://neetcode.io/problems/course-schedule-iv/question?list=neetcode250
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
         # Step 1: Build graph + indegree array
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        
        # Step 2: Each course keeps a set of its prerequisites
        prereq_sets = [set() for _ in range(numCourses)]
        
        # Step 3: Kahn's Topological Sort
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            u = queue.popleft()
            
            for v in graph[u]:
                # u is a direct prerequisite of v
                prereq_sets[v].add(u)
                
                # all prerequisites of u are also prerequisites of v
                prereq_sets[v].update(prereq_sets[u])
                
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        
        # Step 4: Answer queries
        return [u in prereq_sets[v] for u, v in queries]
    