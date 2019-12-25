// title: excel-sheet-column-title
// detail: https://leetcode.com/submissions/detail/193226113/
// datetime: Tue Dec  4 09:55:47 2018
// runtime: 0 ms
// memory: N/A

char* convertToTitle(int n) {
    int i = 0, j = 0, size = 10, r;
    char c;
    char* result = (char*)malloc(sizeof(char) * size);
    
    while(n){
        r = n % 26;
        n = n / 26;
        if(r == 0){
            n --;
            c = 'Z';
        }else{
            c = 'A' + r - 1;
        }
        if(i == size){
            size *= 2;
            result = (char*)realloc(result, sizeof(char) * size);
        }
        result[i++] = c;
    }
    result[i] = 0;
    for(j = 0; j < i / 2; j++){
        c = result[j];
        result[j] = result[i - j - 1];
        result[i - j - 1] = c;
    }
    return result;
}