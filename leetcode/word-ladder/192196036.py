# title: word-ladder
# detail: https://leetcode.com/submissions/detail/192196036/
# datetime: Wed Nov 28 18:34:57 2018
# runtime: 1628 ms
# memory: N/A

        
from collections import deque 

class Solution(object):
    
    def can_transfer(self, word1, word2):
        c = 0
        i, j = 0, len(word1) - 1
        while i <= j:
            if word1[i] != word2[i]:
                c += 1
            if i != j and word1[j] != word2[j]:
                c += 1
            i += 1
            j -= 1
            if c >= 2:
                break
        return c == 1
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        length = 0
        word_length = len(beginWord)
        words = set(wordList)
        queue = deque()
        queue.append((beginWord, 0))
        while queue and words:
            node = queue.popleft()
            for i in range(word_length):
                for j in range(97, 123):
                    word = list(node[0])
                    word[i] = chr(j)
                    word = ''.join(word)
                    if word in words:
                        child = (word, node[1] + 1)
                        queue.append(child)
                        words.remove(word)
                        if word == endWord:
                            length = child[1] + 1
                            return length
        return length
                    
        
        
        