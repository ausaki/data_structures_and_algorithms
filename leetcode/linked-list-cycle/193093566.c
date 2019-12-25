// title: linked-list-cycle
// detail: https://leetcode.com/submissions/detail/193093566/
// datetime: Mon Dec  3 14:54:48 2018
// runtime: 4 ms
// memory: N/A

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    if(head == NULL){
        return false;
    }
    if(head->next == NULL){
        return false;
    }
    struct ListNode *prev, *next, *tmp;
    prev = NULL;
    next = head;
    while(next){
        tmp = next->next;
        next->next = prev;
        prev = next;
        next = tmp;
    }
    return prev == head;
}