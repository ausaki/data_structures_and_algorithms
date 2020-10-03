# title: vowel-spellchecker
# detail: https://leetcode.com/submissions/detail/402613423/
# datetime: Wed Sep 30 16:21:02 2020
# runtime: 180 ms
# memory: 16.4 MB

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replace(w):
            return re.sub(r'[aeiou]', '*', w)
        
        lowercases = {}
        for w in wordlist:
            ww = w.lower()
            if ww not in lowercases:
                lowercases[ww] = w
            ww = replace(ww)
            if ww not in lowercases:
                lowercases[ww] = w
        words = set(wordlist)
        answer = []
        for w in queries:
            if w in words:
                answer.append(w)
                continue
            ww = w.lower()
            answer.append(lowercases.get(ww, lowercases.get(replace(ww), '')))
        return answer