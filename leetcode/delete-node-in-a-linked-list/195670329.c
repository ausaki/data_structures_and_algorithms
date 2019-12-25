// title: delete-node-in-a-linked-list
// detail: https://leetcode.com/submissions/detail/195670329/
// datetime: Tue Dec 18 10:48:18 2018
// runtime: 0 ms
// memory: 856.1 KB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    struct ListNode **p = &node;
    while((*p)->next){
        (*p)->val = (*p)->next->val;
        p = &((*p)->next);
    }
    *p = NULL;
}