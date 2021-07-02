
#include<iostream>

using namespace std;

int main(){
    string s;
    string a,b;
    cin>>a;
    cin>>b;

    for(int i = 0;i<a.length();i++)
    {
        if(a[i] == b[i])
            s += '0';
        else
            s += '1';
    }

    cout<<s;

    return 0;
}
