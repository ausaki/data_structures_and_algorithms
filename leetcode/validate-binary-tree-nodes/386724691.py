# title: validate-binary-tree-nodes
# detail: https://leetcode.com/submissions/detail/386724691/
# datetime: Thu Aug 27 01:11:48 2020
# runtime: 308 ms
# memory: 15.2 MB

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        '''
        非法情况:
        1. 两个非根节点之间的循环, 检查某个节点的indegree == 2.
        2. 非根节点和根节点的循环, 检查是否存在indegree == 0的节点.
        3. 存在多个二叉树, 检查indegree == 0的节点数量.
        '''
        indegrees = [0] * n
        for i in range(n):
            l = leftChild[i]
            r = rightChild[i]
            if l >= 0:
                indegrees[l] += 1
                if indegrees[l] > 1:
                    return False
            if r >= 0:
                indegrees[r] += 1
                if indegrees[r] > 1:
                    return False
        in0 = 0
        s = 0
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                in0 += 1
                if in0 > 1:
                    return False
                if leftChild[i] == -1 and rightChild[i] == -1 and n > 1:
                    return False
            s += indegree
        if in0 != 1 or s != n - 1:
            return False
        return True