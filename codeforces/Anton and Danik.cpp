#include<iostream>

using namespace std;

int main(){
    string s;
    int a=0,b=0,n;
    cin>>n;
    cin>>s;

    for(int i = 0;i<n;i++)
    {
        if(s[i] == 'A')
            a++;
        else if(s[i] == 'D')
            b++;
    }

    if(a > b)
        cout<<"Anton";
    else if(b > a)
        cout<<"Danik";
    else if(a == b)
        cout<<"Friendship";

    return 0;
}
