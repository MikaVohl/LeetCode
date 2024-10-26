from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        seen = {}
        def traverse(source):
            if source in seen:
                return seen[source]
            
            clone = Node(source.val)
            seen[source] = clone
            for neighbor in source.neighbors:
                clone.neighbors.append(traverse(neighbor))

            return clone
        
        return traverse(node)