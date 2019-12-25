// title: first-unique-character-in-a-string
// detail: https://leetcode.com/submissions/detail/71634545/
// datetime: Thu Aug 25 15:44:01 2016
// runtime: 12 ms
// memory: N/A

int firstUniqChar(char* s) {
    int charCount[26] = {0};
    int charPos[26] = {-1};
    char* c = s;
    int i = 0;
    while(*c != 0){
        if(charCount[*c - 'a'] == 0){
            charPos[*c - 'a'] = i;
        }
        charCount[*c - 'a'] ++;
        c ++;
        i ++;        
    }
    int firstPos = i;
    for(int j = 0; j < 26; j++){
        if(charCount[j] == 1 && charPos[j] < firstPos){
            firstPos = charPos[j];
        }
    }
    return firstPos == i ? -1: firstPos;
}