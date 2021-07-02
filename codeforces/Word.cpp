#include <cctype>
#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char str[100];

    cin>>str;

    int uc=0, lc=0;
    for(int i = 0; i < strlen(str);i++)
    {
        if (isupper(str[i])) {
            uc++;
        } else {
            lc++;
        }
    }

    if (uc > lc) {
        for(int i = 0; i < strlen(str);i++)
        {
            str[i] = toupper(str[i]);
        }
    } else {
        for(int i = 0; i < strlen(str);i++)
        {
           str[i] = tolower(str[i]);
        }
    }

    cout << str;
    return 0;
}
