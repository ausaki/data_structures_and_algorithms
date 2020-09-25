# title: swap-for-longest-repeated-character-substring
# detail: https://leetcode.com/submissions/detail/396581400/
# datetime: Wed Sep 16 22:00:39 2020
# runtime: 76 ms
# memory: 15.4 MB

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        result = 1
        cnt = collections.Counter(text)
        c, k = text[0], 1
        encode = []
        for i in range(1, len(text)):
            if text[i] == c:
                k += 1
            else:
                encode.append([c, k])
                c = text[i]
                k = 1
        encode.append([c, k])
        for i, (c, k) in enumerate(encode):
            if i + 1 < len(encode) and encode[i + 1][1] == 1:
                    if i + 2 < len(encode) and encode[i + 2][0] == c:
                        result = max(result, k + encode[i + 2][1] + (cnt[c] > k + encode[i + 2][1]))
            result = max(result, k + (cnt[c] > k))
        return result
            