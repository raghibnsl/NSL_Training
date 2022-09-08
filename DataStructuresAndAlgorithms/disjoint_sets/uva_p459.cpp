#include <bits/stdc++.h>
using namespace std;

int par[5]={0,0,2,0,2};

int find(int u){
    if (u==par[u]){
        return u;
    par[u]=find(par[u]);
    return par[u];
    }
}


int count_sub(char* args, int principle_case){
    for(int i=0;i<args.length();i++){
        int new_rep=find(i);
        if (new_rep==principle_case){
            continue;
        }
        else{
            return 0;
        }
    }
    return 1;
}

int main(){
    char args[2];
    int cases;
    scanf("%d", &cases);
    char space;
    for (int i=0;i<cases;i++){
        char a;
        scanf("%c\n", &a);
        int principle_case=find(int(a)-65);
        int counter=0;
        while (true){
            char u,v;
            scanf("%c",&u);
            if (u==NULL){
                break;
            }
            scanf("%c\n",&v);
            args={u,v}
            if count_sub(char* args, principle_case=principle_case){
                counter++;
            }
            }
        printf("%d\n",counter)

        }
    }


