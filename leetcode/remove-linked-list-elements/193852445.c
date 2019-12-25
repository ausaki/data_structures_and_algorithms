// title: remove-linked-list-elements
// detail: https://leetcode.com/submissions/detail/193852445/
// datetime: Fri Dec  7 17:53:25 2018
// runtime: 4 ms
// memory: 2.6 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    if(head == NULL){
        return head;
    }
    struct ListNode **curr = &head;
    
    while(*curr){
        if((*curr)->val == val){
            *curr = (*curr)->next;
        }else{
            curr = &((*curr)->next);
        }
    }
    return head;
}