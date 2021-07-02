#include<iostream>
using namespace std;

int main(){

    int s,a,b,remain = 0, max = 0;
    cin>>s;
    for(int i = 1;i<=s;i++){
        cin>>a;
        cin>>b;
        remain=remain + (b - a);

        if(max < remain) {
             max = remain;
        }
    }
    cout<<max;
}
