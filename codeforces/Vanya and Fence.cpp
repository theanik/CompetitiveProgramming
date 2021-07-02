#include<iostream>
using namespace std;

int main(){
    int n;cin>>n;
    int h;cin>>h;
    int res = 0;
    for(int i = 0;i < n;i++){
        int a;
        cin>>a;
        if(a>h){
            res+=2;
        }else{
            res+=1;
        }
    }

    cout<<res;

    return 0;

}
