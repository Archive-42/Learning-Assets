{
#include <bits/stdc++.h>
using namespace std;
struct Node {
    int data;
    Node* right;
    Node* left;
    
    Node(int x){
        data = x;
        right = NULL;
        left = NULL;
    }
};
Node *insert(Node *root,int data)
{
    if(root==NULL)
    root=new Node(data);
    else if(data<root->data)
    root->left=insert(root->left,data);
    else
    root->right=insert(root->right,data);
    
    return root;
}
//Position this line where user code will be pasted.
int main() {
    
    int testcases;
    cin>>testcases;
    while(testcases--)
    {
        Node *root=NULL;
        int sizeOfArray;
        cin>>sizeOfArray;
        int arr[sizeOfArray];
        
        for(int i=0;i<sizeOfArray;i++)
        cin>>arr[i];
        
        for(int i=0;i<sizeOfArray;i++)
        {
            root=insert(root,arr[i]);
        }
        int l,h;
        cin>>l>>h;
        cout<<getCountOfNode(root,l,h)<<endl;
    
        
    }
	return 0;
}
}
/*This is a function problem.You only need to complete the function given below*/
/*
The structure of a BST node is as follows:
struct Node {
    int data;
    Node* right;
    Node* left;
    
    Node(int x){
        data = x;
        right = NULL;
        left = NULL;
    }
};
*/
int getCountOfNode(Node *root, int l, int h)
{
    // your code goes here   
    if(!root) return 0;
    queue<Node*> q;
    int count = 0;
    q.push(root);
    while(!q.empty()){
        Node *front = q.front();
        q.pop();
        if(front->data >= l && front->data <= h)
            count++;
        if(front->left)
            q.push(front->left);
        if(front->right)
            q.push(front->right);
    }
    return count;
}
