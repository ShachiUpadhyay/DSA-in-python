import enum
import dataclasses
from typing import Mapping, Sequence, Set, Deque
from collections import deque 

@enum.unique
class Color(enum.Enum):
    RED = 'red'
    BLACK = 'black'
    BLUE = 'blue'

@dataclasses.dataclass(frozen = True)
class Node:
    name: str
    color: Color


Graph = Mapping[Node, Sequence[Node]]

def reverseGraph(graph : Graph) -> Graph:
    
    reversedGraph: dict[Node, list[Node]] = {node: [] for node in graph}

    for node in graph:
       for nxt in graph[node]:
           reversedGraph[nxt].append(node)
    
    return reversedGraph

def getNodesWithSpecificPath(graph: Graph) -> Set[Node]:
   
    result: Set[Node] = set()

    reversedGraph = reverseGraph(graph)
    for node in reversedGraph:
        if node.color == Color.BLUE:
            result.update(Bfs(node, reversedGraph))
                
    
    return result


def Bfs(node: Node, graph:Graph)->Set[Node]:
    result: Set[Node] = set()

    queue: Deque[Node] = deque()
    
    queue.append(node)

    pathNode = 0

    visited: Set[Node] = set()
    
    while queue:
        curr = queue.popleft()
        for nxt in graph[curr]:
            if nxt not in visited:
                if nxt.color == Color.RED:
                    queue.append(nxt)
                    visited.add(nxt)
                if pathNode > 0:
                    result.add(nxt)

        pathNode += 1
    
    return result
    





                    






