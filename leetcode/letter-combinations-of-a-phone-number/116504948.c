// title: letter-combinations-of-a-phone-number
// detail: https://leetcode.com/submissions/detail/116504948/
// datetime: Fri Sep  1 09:39:17 2017
// runtime: 3 ms
// memory: N/A

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** letterCombinations(char* digits, int* returnSize) {
    char** LETTERS_LIST[] = {
        "",
        "",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz",
    };
    
    int i = 0, j = 0, k = 0;
    int size = 50;
    char** result = (char**)malloc(sizeof(char*) * size);
    char ch;
    char* letters;
    char* p;
    
    int digitsSize = strlen(digits);
    if(digitsSize == 0){
        *returnSize = 0;
        return result;
    }
    int* indexes = (int*)calloc(digitsSize, sizeof(int));
    int* letters_size_list = (int*)calloc(digitsSize, sizeof(int));
    
    while(1){
        p = (char*)calloc(digitsSize + 1, sizeof(char));
        for(i = 0; i < digitsSize; i ++){
            ch = digits[i] - '0';
            letters = LETTERS_LIST[ch];
            if(letters_size_list[i] == 0){
                letters_size_list[i] = strlen(letters);
            }
            if(indexes[i] >= letters_size_list[i]){
                break;
            }
            p[i] = letters[indexes[i]];
        }
        if(i == digitsSize){
            if(k >= size){
                size += 10;
                result = (char**)realloc(result, sizeof(char*) * size);
            }
            result[k ++] = p;
            printf("%s\n", p);
            i --;
            indexes[i] ++;
        } else {
            // indexes[i] = 0;
            // if(i - 1 >= 0){
            //     indexes[i --] ++; 
            // }
        }
        if(indexes[i] >= letters_size_list[i]){
            indexes[i] = 0;
            if(i - 1 >= 0) {
                indexes[i - 1] ++;
            } else {
                break;
            }
        }
    }
    *returnSize = k;
    return result;
}