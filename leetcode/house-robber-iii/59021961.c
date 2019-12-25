// title: house-robber-iii
// detail: https://leetcode.com/submissions/detail/59021961/
// datetime: Thu Apr 14 19:09:03 2016
// runtime: 860 ms
// memory: N/A

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int rob(struct TreeNode* root) {
    if(root == NULL){
        return 0;
    }
    int money1 = 0;
    int money2 = root->val;
    if(root->left != NULL){
        money1 += rob(root->left);
        if(root->left->left != NULL){
            money2 += rob(root->left->left);
        }
        if(root->left->right != NULL){
            money2 += rob(root->left->right);
        }
    }
    if(root->right != NULL){
        money1 += rob(root->right);
        if(root->right->left != NULL){
            money2 += rob(root->right->left);
        }
        if(root->right->right != NULL){
            money2 += rob(root->right->right);
        }
    }
    if(money1 > money2){
        return money1;
    }
    return money2;
}