# title: word-ladder
# detail: https://leetcode.com/submissions/detail/192515862/
# datetime: Fri Nov 30 11:41:21 2018
# runtime: 80 ms
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
        if endWord not in wordList:
            return 0
        head = set()
        tail = set()
        
        head.add(beginWord)
        tail.add(endWord)
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.remove(endWord)
        c = 1
        while head:
            if len(head) > len(tail):
                head,tail = tail,head
            tmp = set()
            while head:
                curw = head.pop()          
                for i in xrange(len(curw)):
                    left = curw[:i]
                    right = curw[i+1:]
                    for mutate in string.lowercase:
                        newWord = left+mutate+right
                        if newWord in tail:
                            return c+1
                        if newWord in wordList:
                            wordList.remove(newWord)
                            tmp.add(newWord)
                            
            c += 1
            head = tmp
        return 0 
                    
        
        
        