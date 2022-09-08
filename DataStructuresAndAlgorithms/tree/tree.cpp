#include <iostream>
using namespace std;

struct BstNode{
    char data;
    BstNode* left;
    BstNode* right;
};
BstNode* GetNewNode(char data){
    BstNode* new_node=new BstNode();
    new_node->data=data;
    new_node->left=new_node->right=NULL;
    return new_node;
}

BstNode* Insert(BstNode* root,char data){
    BstNode* temp=GetNewNode(data);
    BstNode* tempt=root;
    if (root==NULL){
        root=GetNewNode(data);
        return root;
    }
    //BstNode* tempt_next_left=tempt->left;
    //BstNode* tempt_next_right=tempt->right;
    while (true){
        cout<<tempt->data<<endl;
        if (data<=tempt->data && tempt->left!=NULL){
            tempt=tempt->left;

        }
        else if(data>(tempt->data) && tempt->right!=NULL){
            tempt=tempt->right;
        }
        else{
            if (data<=tempt->data){
                temp->left=tempt->left;
                tempt->left=temp;
            }
            else{
                temp->right=tempt->right;
                tempt->right=temp;
            }
            break;
        }
        }
    return root;
    }
            //root->left=Insert(root->left,data)

bool Search(BstNode* root, int data){
    if (root==NULL) return false;
    else if (root->data==data) return true;
    else if(data<=root->data) return Search(root->left,data);
    else return Search(root->right,data);
    }
int findHeight(BstNode* root){
    int left_b;
    int right_b;
    if (root==NULL){
        return -1;
    }
    left_b=findHeight(root->left);
    right_b=findHeight(root->right);
    return (left_b>right_b ?left_b : right_b)+1;
}


int findMin(BstNode* root){
    if (root==NULL){
        cout<< "Sorry boss, shit empty"<<endl;
        return -1;
    }
    else if (root->left==NULL){
        return root->data;
    }
    return findMin(root->left);

}
int findMax(BstNode* root){
    if (root==NULL){
        cout<< "Sorry boss, shit empty"<<endl;
        return -1;
    }
    else if (root->right==NULL){
        return root->data;
    }
    return findMax(root->right);
}

void Print(BstNode* root){
    if (root->left==NULL && root->right==NULL){
        cout<<root->data<<endl;
        return;
    }
    cout<<root->data<<endl;
    if (root->right!=NULL){
        Print(root->right);
    }
    else{
        Print(root->left);
    }
}
void PreorderDFS(BstNode* root){
    cout<<root->data<<" ";
    if (root->left!=NULL){
        PreorderDFS(root->left);
    }
    if (root->right!=NULL){
        PreorderDFS(root->right);
    }
    else return;
}
void InorderDFS(BstNode* root){
    if (root->left!=NULL){
        InorderDFS(root->left);
    }
    cout<<root->data<<" ";
    if (root -> right!=NULL){
        InorderDFS(root->right);
    }
    return;
}

void PostorderDFS(BstNode* root){
    if (root->left!=NULL){
        PostorderDFS(root->left);
    }
    if (root -> right!=NULL){
        PostorderDFS(root->right);
    }
    cout<<root->data<<" ";
    return;
}

int main(){
    BstNode* root=NULL;
    cout<< findMin(root)<<endl;
    root=Insert(root,'F');
    root=Insert(root,'D');
    root=Insert(root,'B');
    root=Insert(root,'E');
    root=Insert(root,'A');
    root=Insert(root,'C');
    root=Insert(root,'J');
    root=Insert(root,'G');
    root=Insert(root,'I');
    root=Insert(root,'H');
    root=Insert(root,'K');
    Print(root);
    PreorderDFS(root);
    cout<<endl;
    InorderDFS(root);
    cout<<endl;
    PostorderDFS(root);
    cout<< findHeight(root)<<endl;

    return 0;
}
