#include <iostream>
using namespace std;

int main(){
    int a,b;
    int years = 0;
    cin>>a>>b;
    if(a <= 0 && b <= 0)
        return 0;
    while(true){
        a = a*3;
        b = b*2;
        years++;
        if(a > b){
            break;
        }
    }
    cout<<years;

    return 0;
}
