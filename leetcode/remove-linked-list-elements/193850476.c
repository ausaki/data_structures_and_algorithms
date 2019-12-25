// title: remove-linked-list-elements
// detail: https://leetcode.com/submissions/detail/193850476/
// datetime: Fri Dec  7 17:29:12 2018
// runtime: 12 ms
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
    while(curr){
        if(curr->val == val){
            if(prev == NULL){
                head = curr->next;
            }else{
                prev->next = curr->next;    
            }
        }else{
            prev = curr;
        }
        curr = curr->next;
    }
    return head;
}