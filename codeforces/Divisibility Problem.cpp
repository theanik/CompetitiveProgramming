#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;

    for(int i = 0; i < t; i++){
        int a, b,count = 0;
        cin>>a;
        cin>>b;

        if(a%b == 0) {
            count = 0;
        }else {
            count = b - (a%b);
        }
        cout<<count<<endl;
    }

    return 0;
}
