# title: sum-of-even-numbers-after-queries
# detail: https://leetcode.com/submissions/detail/401828057/
# datetime: Mon Sep 28 22:36:09 2020
# runtime: 484 ms
# memory: 20.1 MB

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(a for a in A if a % 2 == 0)
        answer = [] 
        for v, i in queries:
            if A[i] % 2 and v % 2:
                s += A[i] + v
            if A[i] % 2 == 0:
                if v % 2:
                    s -= A[i]
                else:
                    s += v
            A[i] += v                    
            answer.append(s)
        return answer