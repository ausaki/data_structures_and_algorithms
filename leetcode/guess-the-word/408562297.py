# title: guess-the-word
# detail: https://leetcode.com/submissions/detail/408562297/
# datetime: Wed Oct 14 15:37:20 2020
# runtime: 28 ms
# memory: 14.2 MB

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for i in range(10):
            word = random.choice(wordlist)
            m = master.guess(word)
            if m == 6:
                break
            wordlist = [w for w in wordlist if sum(a == b for a, b in zip(w, word)) == m]
        
            