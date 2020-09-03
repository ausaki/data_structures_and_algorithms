# title: probability-of-a-two-boxes-having-the-same-number-of-distinct-balls
# detail: https://leetcode.com/submissions/detail/381657685/
# datetime: Sun Aug 16 17:06:48 2020
# runtime: 3720 ms
# memory: 13.8 MB

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        def C(n, m):
            c = 1
            for i in range(n, n - m, -1):
                c *= i
            return c / math.factorial(m)
        
        t, e = 0, 0
        def choose(i, k, d1, d2):
            nonlocal t, e
            if k == 0 and i <= n:
                for j in range(i, n):
                    d2[j] = balls[j]
                t_ = 1
                for k, v in d1.items():
                    t_ *= C(balls[k], v)
                t += t_
                e += t_ if len(d1) == len(d2) else 0
                return 
            if k < 0 or i == n:
                return
            for j in range(balls[i] + 1):
                if k - j < 0:
                    break
                if j > 0:
                    d1[i] = j
                if balls[i] - j > 0:
                    d2[i] = balls[i] - j
                else:
                    d2.pop(i)
                choose(i + 1, k - j, d1, d2)
            if i in d1:
                d1.pop(i)
            if i in d2:
                d2.pop(i)
        
        n = len(balls)
        k = sum(balls)
        choose(0, k // 2, {}, {})
        # print(t, e)
        return e / t
            
                