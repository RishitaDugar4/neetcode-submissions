/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    vector<int> result;

public:
    void traversal(TreeNode* node) {
        if (!node) {
            return;
        } 
        traversal(node->left);
        traversal(node->right);
        result.push_back(node->val);
    }
    
    vector<int> postorderTraversal(TreeNode* root) {
        traversal(root);
        return result;
    }
};