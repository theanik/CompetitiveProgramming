#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
    long long a,b,c,d;
    cin>>a>>b>>c>>d;
    long long arr[4] = {a,b,c,d};
    int count = 0;

    int n = sizeof(arr) / sizeof(arr[0]);
    sort(arr, arr + n);

    for(int i = 0; i < 3; i++){
        if(arr[i] == arr[i+1]){
            count++;
        }


    }
    cout<<count;

    return 0;
}
