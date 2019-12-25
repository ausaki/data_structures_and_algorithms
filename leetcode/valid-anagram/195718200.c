// title: valid-anagram
// detail: https://leetcode.com/submissions/detail/195718200/
// datetime: Tue Dec 18 15:10:28 2018
// runtime: 4 ms
// memory: 942.1 KB

bool isAnagram(char* s, char* t) {
    int letters[26] = {0};
    while(*s){
        letters[(*s) - 'a'] ++;
        s++;
    }
    while(*t){
        letters[*t - 'a'] --;
        t++;
    }
    for(int i = 0; i < 26; i ++){
        if(letters[i] != 0){
            return false;
        }
    }
    return true;
}