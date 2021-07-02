
#include <stdio.h>

int main()
{
int* pc, c;
c = 5;
pc = &c;
c++;
printf("%d", *pc);
}
