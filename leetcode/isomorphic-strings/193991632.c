// title: isomorphic-strings
// detail: https://leetcode.com/submissions/detail/193991632/
// datetime: Sat Dec  8 18:31:36 2018
// runtime: 0 ms
// memory: 876.5 KB

bool isIsomorphic(char* s, char* t) {
    char charmap1[256] = {0};
    char charmap2[256] = {0};
    while(*s != 0){
        if(charmap1[*s] == 0){
            if(charmap2[*t] == 1){
                return false;
            }
            charmap1[*s] = *t;
            charmap2[*t] = 1;
        }else{
            if(charmap1[*s] != *t){
                return false;
            }
        }
        s++;
        t++;
    }
    return true;
}