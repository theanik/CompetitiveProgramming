#include <iostream>
using namespace std;

int main(){
    long long n;
    int tmp;

    cin>>n;
    int p = 0;

    while(n!=0){
        tmp = n%10;
        if(tmp == 4 || tmp == 7){
           p++;
        }
        n = n/10;
    }

    if(p == 4 || p == 7){
        cout<<"YES";
    } else {
        cout<<"NO";
    }

    return 0;
}
