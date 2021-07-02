#include<iostream>

using namespace std;
int main(){

    int n;
    cin>>n;
    string res = "";
    bool tmp = false;
    for(int i = 1;i<=n;i++){
        if(i%2 != 0){
            if(i == 1){
                res += "I hate ";
            }else {
                res += " I hate ";
            }
        }else {
            res += " I love ";
        }

        if(i == n){
            res += "it";
        }else {
            res += "that";
        }
    }
    cout<<res;

    return 0;
}
