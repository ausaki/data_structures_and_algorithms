# title: unique-binary-search-trees
# detail: https://leetcode.com/submissions/detail/147203706/
# datetime: Tue Mar 27 17:53:13 2018
# runtime: 33 ms
# memory: N/A

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(self.numTreesRecursive(n).values())
    
    def numTreesRecursive(self, n):
        if n == 0:
            return []
        if n == 1:
            return {1: 1}
        new_trees = {}
        trees = self.numTreesRecursive(n - 1)
        
        for i in trees:
            if i == 1:
                new_trees[1] = trees[i]
                new_trees[2] = trees[i]
            else:
                for k in range(1, i + 2):
                    new_trees.setdefault(k, 0)
                    new_trees[k] += trees[i]
        return new_trees
        