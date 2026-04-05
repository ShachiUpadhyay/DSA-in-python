#https://neetcode.io/problems/count-connected-components/question?list=neetcode250

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent : List[int] = [i for i in range(n)]
        rank : List[int] = [1 for i in range(n)]
        components: int = n

        def find(a: int) -> int:
            if parent[a] == a:
                return a
            else:
                parent[a] = find(parent[a])
                return parent[a]
            
            

        def union(a: int, b:int) -> bool:
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            if rank[pa] >= rank[pb]:
                parent[pb] = pa
                rank[pa] = rank[pa]+rank[pb]
            else:
                parent[pa] = pb
                rank[pb] = rank[pa]+rank[pb]
            return True
        
        for a, b in edges:
            if union(a,b):
                components -= 1
        
        return components


        