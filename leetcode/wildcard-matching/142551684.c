// title: wildcard-matching
// detail: https://leetcode.com/submissions/detail/142551684/
// datetime: Tue Feb 27 10:29:34 2018
// runtime: 20 ms
// memory: N/A

bool isMatch(char* s, char* p) {
    int i = 0;
    int j = 0;
    int k = 0;
    int star = -1;
    int ss = -1;
    char next_char = 0;
    
    while(s[i]){
        if(p[j] == '?' || s[i] == p[j]){
            i ++;
            j ++;
            continue;
        }
        if(p[j] == '*'){
            star = j;
            j ++;
            ss = i;
            continue;
        } 
        if(star != -1){
            j = star + 1;
            ss += 1;
            i = ss;
            continue;
        }
        return false;
        
    }
    while(p[j]=='*'){j++;}

    return !p[j]; 
    // if(s[i] != 0){
    //     return false;
    // }
    // if(p[j] != 0){
    //     while(p[j] == '*'){
    //         j ++;
    //     }
    //     if(p[j] != 0){
    //         return false;
    //     }
    // }
    // return true;
}