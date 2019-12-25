# title: additive-number
# detail: https://leetcode.com/submissions/detail/281953574/
# datetime: Wed Nov 27 10:34:16 2019
# runtime: 28 ms
# memory: 12.9 MB

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def add(a, b, c):
            N = b - a
            M = c - b
            i = b - 1
            j = c - 1
            s = 0
            result = ''
            while i >= a and j >= b:
                s, m = divmod(s + int(num[i]) + int(num[j]), 10)
                result = str(m) + result
                i -= 1
                j -= 1
            while i >= a:
                s, m = divmod(s + int(num[i]), 10)
                result = str(m) + result
                i -= 1
            while j >= b:
                s, m = divmod(s + int(num[j]), 10)
                result = str(m) + result
                j -= 1
            if s:
                result = str(s) + result
            return result
        i = 0
        j = 0
        k = 0
        N = len(num)
        if N < 3:
            return False
        for i in range(N // 2):
            if i + 1 > 1 and num[0] == '0':
                break
            for j in range(i + 1, N - 1):
                a = 0
                b = i + 1
                c = j + 1
                if c - b > 1 and num[b] == '0':
                    break
                flag = False
                while c < N:
                    print(a, b, c)
                    if max(b - a, c - b) > N - c:
                        flag = True
                        break
                    third = add(a, b, c)
                    print(third)
                    if num[c:c + len(third)] != third:
                        break
                    a = b
                    b = c
                    c += len(third)
                if c == N:
                    return True
                if flag:
                    break
        return False