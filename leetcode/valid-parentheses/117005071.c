// title: valid-parentheses
// detail: https://leetcode.com/submissions/detail/117005071/
// datetime: Mon Sep  4 18:24:57 2017
// runtime: 3 ms
// memory: N/A

bool isValid(char* s) {
    int i,j;
    i = 0;
    j = 1;
    
    if(s[i] == 0){
        return false;
    }
    if(s[j] == 0){
        return false;
    }
    
    while(s[j] != 0){
       if(s[j] - s[i] == 1 || s[j] - s[i] == 2){
           i --;
           j ++;
       } else {
           i ++;
           s[i] = s[j];
           j ++;
       }
    }
    if(i >= 0){
        return false;
    }
    return true;
}