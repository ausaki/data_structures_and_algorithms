# title: largest-multiple-of-three
# detail: https://leetcode.com/submissions/detail/387045933/
# datetime: Thu Aug 27 16:45:10 2020
# runtime: 96 ms
# memory: 14 MB

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        '''
        0 3 6 9
        1 4 7
        2 5 8
        '''
        cnt = [0] * 10
        r = 0
        for d in digits:
            cnt[d] += 1
            r = (r + d) % 3
        r = r % 3
        if r == 1:
            for i in [1, 4, 7]:
                if cnt[i] >= 1:
                    cnt[i] -= 1
                    break
            else:
                k = 2
                for i in [2, 5, 8]:
                    if cnt[i] >= k:
                        cnt[i] -= k
                        break
                    elif cnt[i] >= k - 1:
                        cnt[i] -= k - 1
                        k = 1
                
        if r == 2:
            for i in [2, 5, 8]:
                if cnt[i] >= 1:
                    cnt[i] -= 1
                    break
            else:
                k = 2
                for i in [1, 4, 7]:
                    if cnt[i] >= k:
                        cnt[i] -= k
                        break
                    elif cnt[i] >= k - 1:
                        cnt[i] -= k - 1
                        k = 1
        s = []
        for i in reversed(range(10)):
            if cnt[i] > 0:
                s.append(str(i) * cnt[i]) 
        if s and s[0][0] == '0':
            return '0'
        return ''.join(s)