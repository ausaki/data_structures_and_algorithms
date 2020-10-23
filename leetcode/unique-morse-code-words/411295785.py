# title: unique-morse-code-words
# detail: https://leetcode.com/submissions/detail/411295785/
# datetime: Wed Oct 21 11:24:00 2020
# runtime: 28 ms
# memory: 14.2 MB

class Solution:
    coding = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(''.join(self.coding[ord(c) - 97] for c in w) for w in words))
        