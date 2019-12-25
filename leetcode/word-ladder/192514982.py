# title: word-ladder
# detail: https://leetcode.com/submissions/detail/192514982/
# datetime: Fri Nov 30 11:36:24 2018
# runtime: 172 ms
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
        if endWord not in words:
            return 0

        word_length = len(beginWord)
        level = 0
        head_words = set()
        head_words.add(beginWord)
        tail_words = set()
        tail_words.add(endWord)
        words.remove(endWord)
        temp_set = set()

        while head_words:
            if len(head_words) > len(tail_words):
                head_words, tail_words = tail_words, head_words
            for word in head_words:
                word = list(word)
                for i in range(word_length):
                    char = word[i]
                    for j in range(97, 123):
                        word[i] = chr(j)
                        next_word = ''.join(word)
                        if next_word in tail_words:
                            return level + 2
                        if next_word in words:
                            temp_set.add(next_word)
                            words.remove(next_word)
                    word[i] = char
            head_words.clear()
            head_words = temp_set
            temp_set = set()
            level += 1
        return 0
                    
        
        
        