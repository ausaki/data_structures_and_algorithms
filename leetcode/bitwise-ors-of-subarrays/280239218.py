# title: bitwise-ors-of-subarrays
# detail: https://leetcode.com/submissions/detail/280239218/
# datetime: Wed Nov 20 11:43:55 2019
# runtime: 872 ms
# memory: 39.3 MB

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # result = set()
        # for i in range(len(A)):
        #     v = A[i]
        #     for j in range(i, len(A)):
        #         v |= A[j]
        #         result.add(v)
        # return len(result)
        curr = set()
        result = set()
        for i in A:
            curr = set(i | j for j in curr)
            curr.add(i)
            result |= curr
        return len(result)