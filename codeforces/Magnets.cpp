#include<iostream>

using namespace std;
int main(){

    int n;
    cin>>n;
    int a;
    int tmp = 0;
    int group = 0;
    for(int i = 0;i<n;i++){
        cin>>a;
        if(a!=tmp){
            group++;
        }

        tmp = a;
    }

    cout<<group;
}
