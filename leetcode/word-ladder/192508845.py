# title: word-ladder
# detail: https://leetcode.com/submissions/detail/192508845/
# datetime: Fri Nov 30 11:04:18 2018
# runtime: 824 ms
# memory: N/A

        
from collections import deque 

class Solution(object):
    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = set(wordList)
        word_length = len(beginWord)
        level = 0
        next_words = set()
        next_words.add(beginWord)
        temp_set = set()
        while next_words and words:
            for word in next_words:
                word = list(word)
                for i in range(word_length):
                    char = word[i]
                    for j in range(97, 123):
                        word[i] = chr(j)
                        next_word = ''.join(word)
                        if next_word in words:
                            temp_set.add(next_word)
                            words.remove(next_word)
                            if next_word == endWord:
                                return level + 2
                    word[i] = char
            next_words.clear()
            next_words = temp_set
            temp_set = set()
            level += 1
        return 0
                    
        
        
        