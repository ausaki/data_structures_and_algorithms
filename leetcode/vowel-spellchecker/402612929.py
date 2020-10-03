# title: vowel-spellchecker
# detail: https://leetcode.com/submissions/detail/402612929/
# datetime: Wed Sep 30 16:19:23 2020
# runtime: 184 ms
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
            if ww in lowercases:
                answer.append(lowercases[ww])
                continue
            ww = replace(ww)
            if ww in lowercases:
                answer.append(lowercases[ww])
                continue
            answer.append('')
        return answer