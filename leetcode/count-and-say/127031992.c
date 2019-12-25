// title: count-and-say
// detail: https://leetcode.com/submissions/detail/127031992/
// datetime: Mon Nov  6 18:01:21 2017
// runtime: 0 ms
// memory: N/A

char* countAndSay(int n) {
    int size = 10;
    char* new_str = (char*) malloc(size);
    char* str = NULL;
    int i, j, k, count;
    char c0, c1;
    
    if(n == 1){
        str =  (char*) malloc(2);
        str[0] = '1';
        str[1] = 0;
        return str;
    }
    str = countAndSay(n - 1);
    
    c0 = str[0];
    j = 0;
    count = 0;
    k = 0;
    while((c1 = str[j]) != 0){
        if(c1 != c0){
            new_str[k ++] = count + '0';
            if(k >= size){
                size += 5;
                new_str = (char*)realloc(new_str, size);
            }
            new_str[k ++] = c0;
            count = 0;
            c0 = c1;
        }
        if(c1 == c0){
            count ++;
        }
        j ++;
    }
    new_str[k ++] = count + '0';
    if(k >= size){
        size += 5;
        new_str = (char*)realloc(new_str, size);
    }
    new_str[k ++] = c0;
    new_str[k] = 0;
    return new_str;
}