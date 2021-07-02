#include<iostream>
using namespace std;

int main(){
    int n;cin>>n;
    int res = 0;
    for(int i = 0;i < n;i++){
        int a;
        int b;
        cin>>a;
        cin>>b;
        if((a+1)<b){
            res+=1;
        }
    }

    cout<<res;

    return 0;

}

