# title: validate-binary-tree-nodes
# detail: https://leetcode.com/submissions/detail/386687295/
# datetime: Wed Aug 26 23:30:26 2020
# runtime: 304 ms
# memory: 15.5 MB

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegrees = [0] * n
        outdegrees = [0] * n
        for i in range(n):
            l = leftChild[i]
            r = rightChild[i]
            if l >= 0:
                indegrees[l] += 1
                outdegrees[i] += 1
                if indegrees[l] > 1 or outdegrees[i] > 2:
                    return False
            if r >= 0:
                indegrees[r] += 1
                outdegrees[i] += 1
                if indegrees[r] > 1 or outdegrees[i] > 2:
                    return False
        in0 = 0
        for i, o in zip(indegrees, outdegrees):
            if i == 0:
                in0 += 1
                if in0 > 1:
                    return False
                if o == 0 and n > 1:
                    return False
            if i > 1:
                return False
            if o > 2:
                return False
        if in0 != 1:
            return False
        return True