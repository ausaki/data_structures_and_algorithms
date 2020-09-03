# title: largest-multiple-of-three
# detail: https://leetcode.com/submissions/detail/387043274/
# datetime: Thu Aug 27 16:35:09 2020
# runtime: 92 ms
# memory: 14.2 MB

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        '''
        0 3 6 9
        1 4 7
        2 5 8
        '''
        cnt = [[0] * 10 for i in range(3)]
        for d in digits:
            r = d % 3
            cnt[r][d] += 1
        r = (sum(cnt[1]) + 2 * sum(cnt[2])) % 3
        # print(cnt)
        # print(r)
        if r == 1:
            for i in [1, 4, 7]:
                if cnt[1][i] >= 1:
                    cnt[1][i] -= 1
                    break
            else:
                k = 2
                for i in [2, 5, 8]:
                    if cnt[2][i] >= k:
                        cnt[2][i] -= k
                        break
                    elif cnt[2][i] >= k - 1:
                        cnt[2][i] -= k - 1
                        k = 1
                
        if r == 2:
            for i in [2, 5, 8]:
                if cnt[2][i] >= 1:
                    cnt[2][i] -= 1
                    break
            else:
                k = 2
                for i in [1, 4, 7]:
                    if cnt[1][i] >= k:
                        cnt[1][i] -= k
                        break
                    elif cnt[1][i] >= k - 1:
                        cnt[1][i] -= k - 1
                        k = 1
        for i in [1, 4, 7]:
            cnt[0][i] += cnt[1][i]
        for i in [2, 5, 8]:
            cnt[0][i] += cnt[2][i]
        s = []
        for i in reversed(range(10)):
            if cnt[0][i] > 0:
                s.append(str(i) * cnt[0][i]) 
        if s and s[0][0] == '0':
            return '0'
        return ''.join(s)