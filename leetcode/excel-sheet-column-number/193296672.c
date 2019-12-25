// title: excel-sheet-column-number
// detail: https://leetcode.com/submissions/detail/193296672/
// datetime: Tue Dec  4 16:06:28 2018
// runtime: 4 ms
// memory: N/A

int titleToNumber(char* s) {
    char c;
    int i = 0, result = 0;
    
    while(c = s[i++]){
        result += c - 'A' + 1;
        if(s[i] != 0){
            result *= 26;    
        }
    }
    return result;
}