#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    getline(cin, s);

    string s2;
    char lastChar[1];
    int count = 0;

    for(int i = 1, j = 0;i < s.length()-1;i++){
        if(s[i] != ' ' && s[i] != ','){
            s2 += s[i];
        }
    }

    sort(s2.begin(), s2.end());

    for(int i = 0;i < s2.length();i++){
        if(lastChar[0] != s2[i]){
            count++;
            lastChar[0] = s2[i];
        }
    }

    cout<<count;

    return 0;
}
