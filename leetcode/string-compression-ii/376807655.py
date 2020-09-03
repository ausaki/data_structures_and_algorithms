# title: string-compression-ii
# detail: https://leetcode.com/submissions/detail/376807655/
# datetime: Thu Aug  6 12:57:57 2020
# runtime: 2692 ms
# memory: 212.8 MB

from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if k == len(s):
            return 0
        n = len(s)
        enc = []
        curr = s[0]
        cnt = 0
        for c in s:
            if c == curr:
                cnt += 1
            else:
                enc.append([curr, cnt])
                curr = c
                cnt = 1
        enc.append([curr, cnt])
        n = len(enc)
        # print(enc)
        
        @lru_cache(None)
        def count(i, last_char, last_count, k):
            # print(i, last_char, last_count, k)
            if k < 0:
                return 200
            if i == n:
                return 0
            char, cnt = enc[i]
            result = 200
            if char == last_char:
                j = 0
                cnt += last_count
                if (last_count == 1 and cnt >= 2) or (last_count < 10 and cnt >= 10) or (last_count < 100 and cnt >= 100):
                    j = 1
                result = j + count(i + 1, last_char, cnt, k)
            else:
                j = 0
                if cnt == 1:
                    j = 1
                elif cnt < 10:
                    j = 2
                elif cnt < 100:
                    j = 3
                else:
                    j = 4
                c1 = j + count(i + 1, char, cnt, k)
                result = c1
                while cnt > 0 and k > 0:
                    if cnt == 1:
                        if k >= 1:
                            k -= 1
                            cnt = 0
                            c2 = count(i + 1, last_char, last_count, k)
                            result = min(result, c2)
                        else:
                            break
                    elif cnt < 10:
                        if k >= cnt - 1:
                            # delete (cnt - 1) `char`
                            k -= cnt - 1
                            cnt = 1
                            c2 = 1 + count(i + 1, char, cnt, k)
                            result = min(result, c2)
                        else:
                            break
                    elif cnt < 100:
                        if k >= cnt - 9:
                            k -= cnt - 9
                            cnt = 9
                            c2 = 2 + count(i + 1, char, cnt, k)
                            result = min(result, c2)
                        else:
                            break
                    else:
                        if k >= cnt - 99:
                            k -= cnt - 99
                            cnt = 99
                            c2 = 3 + count(i + 1, char, cnt, k)
                            result = min(result, c2)
                        else:
                            break
            # print('result:', i, result)
            return result
            
        return count(0, '', 0, k)
                    