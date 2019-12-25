# title: clone-graph
# detail: https://leetcode.com/submissions/detail/282075571/
# datetime: Wed Nov 27 23:58:56 2019
# runtime: 36 ms
# memory: 13.3 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def _clone(neighbor):
            print(neighbor.val)
            if neighbor in seen:
                return seen[neighbor]
            cnode = Node(neighbor.val, [None] * len(neighbor.neighbors))
            seen[neighbor] = cnode
            for i, nb in enumerate(neighbor.neighbors):
                cnode.neighbors[i] = _clone(nb)
            return cnode
        
        seen = {}
        new_node = Node(node.val, [None] * len(node.neighbors))
        seen[node] = new_node
        for i, nb in enumerate(node.neighbors):
            new_node.neighbors[i] = _clone(nb)
        return new_node
                
        