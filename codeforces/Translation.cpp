#include <iostream>
using namespace std;

int main(){
    string s;
    string t;
    string o;

    cin>>s;
    cin>>o;


    for(int i = s.length() - 1; i >= 0 ; i--) {
        t+=s[i];
    }
    if(o == t) {
        cout<<"YES";
    } else {
        cout<<"NO";
    }



    return 0;
}
