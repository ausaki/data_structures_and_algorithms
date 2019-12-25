// title: min-stack
// detail: https://leetcode.com/submissions/detail/193116396/
// datetime: Mon Dec  3 17:26:20 2018
// runtime: 12 ms
// memory: N/A

typedef struct {
    int size;
    int top;
    int* buffer;
} MinStack;

/** initialize your data structure here. */
MinStack* minStackCreate(int maxSize) {
    MinStack *ms = (MinStack*)malloc(sizeof(MinStack));
    ms->size = maxSize;
    ms->buffer = (int*)malloc(sizeof(int) * ms->size * 2);
    ms->top = 0;
    return ms;
}

void minStackPush(MinStack* obj, int x) {
    int min = 0;
    if(obj->top == 0){
        min = x;
    }else{
        min = obj->buffer[obj->top - 1];
    }
    obj->buffer[obj->top++] = x;
    if(x < min){
        min = x;
    }
    obj->buffer[obj->top++] = min;
}

void minStackPop(MinStack* obj) {
    obj->top -= 2;
}

int minStackTop(MinStack* obj) {
    if(obj->top == 0){
        return -1;
    }
    return obj->buffer[obj->top - 2];
}

int minStackGetMin(MinStack* obj) {
    return obj->buffer[obj->top - 1];
}

void minStackFree(MinStack* obj) {
    free(obj->buffer);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * struct MinStack* obj = minStackCreate(maxSize);
 * minStackPush(obj, x);
 * minStackPop(obj);
 * int param_3 = minStackTop(obj);
 * int param_4 = minStackGetMin(obj);
 * minStackFree(obj);
 */