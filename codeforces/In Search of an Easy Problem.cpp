
#include<iostream>

using namespace std;
int main(){

    int n;
    cin>>n;
    int a;
    bool tmp = false;
    for(int i = 0;i<n;i++){
        cin>>a;
        if(a==1){
            tmp = true;
            break;
        }
    }
    if(tmp == true)
        cout<<"HARD";
    else
        cout<<"EASY";

    return 0;
}
