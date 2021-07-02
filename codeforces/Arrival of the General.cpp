
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int minIndex = 0, maxIndex = 0, minVal = INT_MAX, maxVal = 0, res = 0, x;
    for(int i = 0; i < n; i++){
        cin>>x;
        if(x > maxVal){
            maxVal = x;
            maxIndex = i;
        }

        if(x <= minVal){
            minVal = x;
            minIndex = i;
        }
    }

     res = ((n - 1) + maxIndex) - minIndex;
     if (minIndex < maxIndex){
        res = res - 1;
     }

    cout<<res;
    return 0;
}
