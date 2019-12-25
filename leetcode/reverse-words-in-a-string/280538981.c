// title: reverse-words-in-a-string
// detail: https://leetcode.com/submissions/detail/280538981/
// datetime: Thu Nov 21 13:37:25 2019
// runtime: 4 ms
// memory: 7.5 MB



char * reverseWords(char * s){
    int i, j, k, m, spaces;
    char tmp;
    i = 0;
    while(s[i]){
        j = i;
        while(s[j] == ' '){
            j ++;
        }
        if(s[j] == 0){
            break;
        }
        spaces = j - i;
        if(spaces >= 1){
            if(i == 0)
                spaces ++;
            else
                i += 1;
        }
        while(s[j] != 0 && s[j] != ' '){
            if(spaces > 1){
                s[j - spaces + 1] = s[j];
                s[j] = ' ';
            }
            j ++;
        }
        if(spaces > 1){
            j -= spaces;
        } else {
            j --;
        }
        
        k = i;
        m = j;
        while(k < m){
            tmp = s[k];
            s[k] = s[m];
            s[m] = tmp;
            k ++;
            m --;
        }
        i = j + 1;
    }
    s[i] = 0;
    k = 0;
    m = i - 1;
    while(k < m){
        tmp = s[k];
        s[k] = s[m];
        s[m] = tmp;
        k ++;
        m --;
    }
    return s;
}

