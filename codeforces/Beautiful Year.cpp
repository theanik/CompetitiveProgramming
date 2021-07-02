
#include <iostream>
#include <bits/stdc++.h>
using namespace std;


int countDistinctDigit(int n){
    int count = 0;
    int arr[10] = {0};

    while(n!=0){
        arr[n%10] = 1;
        n/=10;
    }

    for(int i = 0; i < 10;i++)
    {
        if(arr[i]){
            count++;
        }
    }
    return count;
}

int countDigit(int n)
{
    int count = 0;

    while(n!=0){
        count++;
        n/=10;
    }

    return count;
}


int getNextYear(int n){
    while(n < INT_MAX){
        int a = countDistinctDigit(n+1);
        int b = countDigit(n+1);
        if(a == b){
            return n +1;
        }else {
            n++;
        }
    }
    return -1;
}

int main(){
    int years;

    cin>>years;
    int res = getNextYear(years);

    cout<<res;

    return 0;
}


