from typing import Tuple, List, Set, DefaultDict
from collections import  defaultdict, deque
class FindPassword:
    def findPassword(self, hints: List[Tuple] ) -> str:
        graph: DefaultDict[str, Set[str]] =  defaultdict(set)
        indegree: DefaultDict[str, int] = defaultdict(int)

        #create graph and update indegree

        for a,b,c in hints:
            indegree[a] += 0   
            indegree[b] += 0
            indegree[c] += 0

            if b not in graph[a]:
                graph[a].add(b)
                indegree[b] += 1
            if c not in graph[b]:    
                graph[b].add(c)
                indegree[c] =  indegree[c]+1

        
        #Apply Kahn's algo
        
        queue = deque()

        for k in indegree:
            if indegree[k] == 0:
                queue.append(k)
        
        password: str = ""
        
        while queue:
            curr = queue.popleft()
            password = password + curr

            for nxt in graph[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        if len(password) != len(indegree):
            raise ValueError("Cycle detected")

        return password 
    
if __name__ == "__main__":
    findPassword = FindPassword()

    test_cases = [
        {
            "name": "Sample from problem statement",
            "hints": [('b','c','a'), ('b','c','d'), ('c','a','d')],
            "expected": "bcad"
        },
        {
            "name": "Minimal 3-character case",
            "hints": [('a','b','c')],
            "expected": "abc"
        },
        {
            "name": "Simple linear chain",
            "hints": [('a','b','c'), ('b','c','d')],
            "expected": "abcd"
        },
        {
            "name": "Multiple constraints same ordering",
            "hints": [('x','y','z'), ('x','y','w'), ('y','z','w')],
            "expected": "xyzw"
        },
        {
            "name": "Larger 7-character password",
            "hints": [
                ('a','b','c'),
                ('b','c','d'),
                ('c','d','e'),
                ('d','e','f'),
                ('e','f','g')
            ],
            "expected": "abcdefg"
        },
        {
            "name": "Characters introduced out of order",
            "hints": [
                ('d','e','f'),
                ('b','c','d'),
                ('a','b','c')
            ],
            "expected": "abcdef"
        }
    ]

    all_passed = True

    for i, test in enumerate(test_cases, 1):
        try:
            result = findPassword.findPassword(test["hints"])
            passed = result == test["expected"]
        except Exception as e:
            result = str(e)
            passed = False

        print(f"Test {i}: {test['name']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Got     : {result}")
        print(f"  Result  : {'PASS' if passed else 'FAIL'}\n")

        all_passed = all_passed and passed

    print("FINAL RESULT:", "ALL TESTS PASSED ✅" if all_passed else "SOME TESTS FAILED ❌")
    


#Time complexity = O(E) + O(V + E) = O(V + E)
# O(E) + O(V + E) = O(V + E)



        




