// title: reverse-words-in-a-string
// detail: https://leetcode.com/submissions/detail/280541129/
// datetime: Thu Nov 21 13:45:57 2019
// runtime: 0 ms
// memory: 7.3 MB


void reverse(char *s, int left, int right){
    char tmp;
    while(left < right){
        tmp = s[left];
        s[left] = s[right];
        s[right] = tmp;
        left ++;
        right --;
    }
}

char * reverseWords(char * s){
    int i, j, spaces;
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
        reverse(s, i, j);
        i = j + 1;
    }
    s[i] = 0;
    reverse(s, 0, i - 1);
    return s;
}

