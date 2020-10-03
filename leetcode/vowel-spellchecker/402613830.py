# title: vowel-spellchecker
# detail: https://leetcode.com/submissions/detail/402613830/
# datetime: Wed Sep 30 16:22:31 2020
# runtime: 188 ms
# memory: 16.4 MB

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        replace = lambda w: re.sub(r'[aeiou]', '*', w)
        
        lowercases = {}
        for w in wordlist:
            ww = w.lower()
            lowercases.setdefault(ww, w)
            lowercases.setdefault(replace(ww), w)
        words = set(wordlist)
        answer = []
        for w in queries:
            if w in words:
                answer.append(w)
                continue
            ww = w.lower()
            answer.append(lowercases.get(ww, lowercases.get(replace(ww), '')))
        return answer