# title: word-ladder
# detail: https://leetcode.com/submissions/detail/192500196/
# datetime: Fri Nov 30 10:17:22 2018
# runtime: 80 ms
# memory: N/A

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordDict;
        for(int i = 0; i < wordList.size(); i++){
            wordDict.insert(wordList[i]);
        }
        queue<string> toVisit;
        addNextWords(beginWord, wordDict, toVisit);
        int dist = 2;
        while (!toVisit.empty()) {
            int num = toVisit.size();
            for (int i = 0; i < num; i++) {
                string word = toVisit.front();
                toVisit.pop();
                if (word == endWord) return dist;
                addNextWords(word, wordDict, toVisit);
            }
            dist++;
        }
        return 0;
    }
private:
    void addNextWords(string word, unordered_set<string>& wordDict, queue<string>& toVisit) {
        wordDict.erase(word);
        for (int p = 0; p < (int)word.length(); p++) {
            char letter = word[p];
            for (int k = 0; k < 26; k++) { 
                word[p] = 'a' + k;
                if (wordDict.find(word) != wordDict.end()) {
                    toVisit.push(word);
                    wordDict.erase(word);
                }
            }
            word[p] = letter;
        } 
    } 
};