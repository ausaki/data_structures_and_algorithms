// title: remove-linked-list-elements
// detail: https://leetcode.com/submissions/detail/193850746/
// datetime: Fri Dec  7 17:32:09 2018
// runtime: 8 ms
// memory: 2.6 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode *prev, *curr;
    prev = NULL;
    curr = head;
    if(curr == NULL){
        return head;
    }
    while(curr && curr->val == val){
        head = curr = curr->next;
    }
    while(curr){
        if(curr->val == val){
            prev->next = curr->next;    
        }else{
            prev = curr;
        }
        curr = curr->next;
    }
    return head;
}