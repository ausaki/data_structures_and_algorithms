// title: palindrome-linked-list
// detail: https://leetcode.com/submissions/detail/194343301/
// datetime: Mon Dec 10 15:41:18 2018
// runtime: 8 ms
// memory: 4 MB

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    if(head == NULL || head->next == NULL){
        return true;
    }
    struct ListNode *slow = head,
                    *fast = head,
                    *prev,
                    *curr,
                    *tail,
                    *tmp;
    while(fast->next && fast->next->next){
        slow = slow->next;
        fast = fast->next->next;
    }
    curr = slow->next;
    slow->next = NULL;
    prev = NULL;
    while(curr){
        tmp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = tmp;
    }
    tail = prev;
    while(head && tail && head->val == tail->val){
        head = head->next;
        tail = tail->next;
    }
    return tail == NULL;
}