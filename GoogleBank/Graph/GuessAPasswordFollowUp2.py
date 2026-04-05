from collections import defaultdict, deque
from typing import Tuple, DefaultDict, Set, List, Optional

class InteractivePasswordFinder:
    def __init__(self, length: int):
        self.length = length
        self.graph: DefaultDict[str, Set[str]] = defaultdict(set)
        self.indegree: DefaultDict[str, int] = defaultdict(int)

    def update_graph(self, a: str, b: str, c: str) -> None:
        for ch in (a, b, c):
            self.indegree.setdefault(ch, 0)

        if b not in self.graph[a]:
            self.graph[a].add(b)
            self.indegree[b] += 1

        if c not in self.graph[b]:
            self.graph[b].add(c)
            self.indegree[c] += 1

    def try_topological_sort(self) -> Optional[str]:
        indeg = dict(self.indegree)  # copy
        queue = deque([ch for ch in indeg if indeg[ch] == 0])
        result = []

        while queue:
            # 🔴 if more than one choice → not unique
            if len(queue) > 1:
                return None

            curr = queue.popleft()
            result.append(curr)

            for nxt in self.graph[curr]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    queue.append(nxt)

        if len(result) == self.length:
            return "".join(result)

        return None

    def guess_password(self, getTuple) -> str:
        while True:
            a, b, c = getTuple()
            self.update_graph(a, b, c)

            password = self.try_topological_sort()
            if password:
                return password