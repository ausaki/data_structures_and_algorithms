# title: decoded-string-at-index
# detail: https://leetcode.com/submissions/detail/280862103/
# datetime: Fri Nov 22 22:57:24 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        code = []
        N = len(S)
        K -= 1
        i = 0
        prev_len = 0
        while i < N:
            j = i
            while j < N and S[j].isalpha():
                j += 1
            s = S[i:j]
            i = j
            cnt = 1
            while j < N and S[j].isdigit():
                cnt *= int(S[j])
                j += 1
            code.append([s, cnt, prev_len])
            prev_len = (prev_len + len(s)) * cnt
            i = j
        # print(code)
        def recursive(k, i):
            # print('i', i, 'k', k)
            prev_len = code[i][2]
            l = len(code[i][0])
            if k < prev_len:
                return recursive(k, i - 1)
            if k < prev_len + l:
                return code[i][0][k - prev_len]
            if k < (prev_len + l) * code[i][1]:
                r = k % (prev_len + l)
                # print('r', r)
                return recursive(r, i)
            else:
                return recursive(k, i + 1)
        return recursive(K, 0)
            
            
            
        
        
        