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
private:
    unordered_map<int,int> mp;
    TreeNode* help(vector<int>& in, vector<int>& pos, int left, int right, int rootidx){

        if(left > right)
            return NULL;
        int val = pos[rootidx];
        TreeNode* node = new TreeNode(val);
        int p = mp[val];
        node->right = help(in,pos,p+1,right,rootidx-1);
        node->left = help(in,pos,left,p-1,rootidx-1-(right-p));

        return node;
    }
public:
    TreeNode* buildTree(vector<int>& in, vector<int>& pos) {
        for(int i=0;i<in.size();i++){
            mp[in[i]]=i;
        }

        return help(in,pos,0,in.size()-1,pos.size()-1);
    }
};

