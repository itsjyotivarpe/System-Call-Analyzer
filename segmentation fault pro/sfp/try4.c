// stack overflow
// http://stackoverflow.com/questions/10242839/is-there-any-hard-wired-limit-on-recursion-depth-in-c/10242951#10242951
// soln : use tail recursion


#include <stdio.h>

unsigned long int add(unsigned long int n)
{
    return (n == 0) ? 0 : n + add(n-1); 
}

int main()
{
    printf("result : %lu \n", add(1000000));
    return 0;
}
