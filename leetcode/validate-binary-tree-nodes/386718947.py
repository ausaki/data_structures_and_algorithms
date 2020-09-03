# title: validate-binary-tree-nodes
# detail: https://leetcode.com/submissions/detail/386718947/
# datetime: Thu Aug 27 00:56:51 2020
# runtime: 312 ms
# memory: 15.5 MB

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        '''
        非法情况:
        1. 两个非根节点之间的循环, 检查某个节点的indegree == 2.
        2. 非根节点和根节点的循环, 检查是否存在indegree == 0的节点.
        3. 存在多个二叉树, 检查indegree == 0的节点数量.
        '''
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
        s = 0
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                in0 += 1
                if in0 > 1:
                    return False
                if outdegrees[i] == 0 and n > 1:
                    return False
            s += indegree
        if in0 != 1 or s != n - 1:
            return False
        return True